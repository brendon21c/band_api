# todo get images and return
from keys import keys
import urllib.request
import requests
import json

# either download images, serve from your own server

# or get URLs for images (e.g from flikr ) have links to images <img src="whatever the external url is">

def get_photos_for_band(band):
    key = keys['FLICKR KEY']
    bandSpacing = band.replace(' ', '%20')
    flickerSearchURL = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&text={}&format=json&nojsoncallback=1'.format(key, bandSpacing)
    print (flickerSearchURL)
        #Search flickr for cat pictures
    flickrResponse = urllib.request.urlopen(flickerSearchURL)
        #get json back
    flickrResponseJSONString = flickrResponse.read().decode('UTF-8')
    flickrResponseJson = json.loads(flickrResponseJSONString)
        #Get first json object ('photos') which contains another json object ('photo') which is an json array; each
        # element represents one photo. Take element 0
    firstResponsePhoto = flickrResponseJson['photos']['photo'][0]
    secret = firstResponsePhoto['secret']
    id = firstResponsePhoto['id']
    server = firstResponsePhoto['server']
    farm = firstResponsePhoto['farm']

    #print(jsonforphoto)  #Just checking we get the JSON we expect
        #TODO add error handing

    fetchPhotoURL = 'https://farm%s.staticflickr.com/%s/%s_%s_m.jpg' % (farm, server, id, secret)
    print(fetchPhotoURL)   #Again, just checking
    return fetchPhotoURL
        #Or, maybe you want lots of cat pictures? This fetches the first 5

        #for cat in range(0, 5):
            #jsonforphoto = flickrResponseJson['photos']['photo'][cat]
            #deal with this in the following way. vvvvvvv

            #Extract the secret, server, id and farm; which you need to construct another URL to request a specific photo
            #https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg



            #Reference: http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests

            # catPicFileNameJpg = 'cat' + str(cat) + '.jpg'
            # catPicFileGif = 'cat' + str(cat) + '.gif'

            #Read the response and save it as a .jpg. Use shutil to copy the stream of bytes into a file
            #What does 'with' mean? http://preshing.com/20110920/the-python-with-statement-by-example/
            # resp = requests.get(fetchPhotoURL, stream=True)
            # with open(catPicFileNameJpg, 'wb') as out_file:
            #     shutil.copyfileobj(resp.raw, out_file)
            # del resp


            #Flickr returns a jpg. Tkinter displays gif. Use pillow to convert the JPG to GIF
            #Reference https://pillow.readthedocs.org/handbook/tutorial.html
            # Image.open(catPicFileNameJpg).save(catPicFileGif)
            #
            # #Add PictureImage to GUI
            # _catPic = PhotoImage(file=catPicFileGif)
            # _catPicLabel = Label(self, image=_catPic)
            # _catPicLabel.image = _catPic
            # _catPicLabel.grid()
    # https://github.com/minneapolis-edu/HelloFlikrGUI/blob/master/FlickrGUI.py
