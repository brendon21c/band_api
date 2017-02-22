#source reference "http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search"
from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen
import urllib.request
import os
from http.cookiejar import CookieJar
import json
from photo import Photo

#can pass band name as arguement from web app textbox?
class BandPhotoAPI:
    #use arguement instead of hard coded variable
    def __init__(self, query):
        self.photo = self.queryForPhoto(query)
    def get_soup(self, url,header):
        return BeautifulSoup(urlopen(urllib.request.Request(url,headers=header)),'html.parser')

    def queryForPhoto(self, query):
    #query = raw_input("query image")# you can change the query for the image  here

        #part of saving the image to a file so it is commented out incase
        #we want to use the code for saving to a file (might be useful)
        #image_type="ActiOn"
        query= query.split()
        query='+'.join(query)
        url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
        #print (url)
        #add the directory for your image here
        DIR="Pictures"
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        }
        soup = self.get_soup(url,header)


        ActualImages=[]# contains the link for Large original images, type of  image
        for a in soup.find_all("div",{"class":"rg_meta"}, limit = 1):
            link , Type =json.loads(a.text)["ou"] ,json.loads(a.text)["ity"]
            bandPhoto = Photo(link,Type)
        return bandPhoto
'''
part of getting and saving the image to a file from the url
so it is commented out incase we want to use the code
(might be useful, it works, needs tweeks now that i made it a class)
note to self: some of the imports are not useful without this code
'''
            #ActualImages.append((link,Type))

# print  ("there are total" , len(ActualImages),"images")
# #makes a folder with the name of the search query(band)
# if not os.path.exists(DIR):
#             os.mkdir(DIR)
# DIR = os.path.join(DIR, query.split()[0])
#
# if not os.path.exists(DIR):
#             os.mkdir(DIR)
# ###save images to band folder
# for i , (img , Type) in enumerate( ActualImages):
#
#     try:
#         req = urllib.request.Request(img, headers=header)
#         raw_img = urlopen(req).read()
#
#         cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
#         print (cntr)
'''
#need to use this if we are going to save the image as a file.
#we can probably save the url to the database but you risk the image not being available
#since the data in the datbase has limited usefulness (once the tour date is over
it is no longer applicable) we can probably get away with saving the url
'''
#         if len(Type)==0:
#             f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
#         else :
#             f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')
#
#
#         f.write(raw_img)
#         f.close()
#     except Exception as e:
#         print ("could not load : "+img)
#         print (e)
