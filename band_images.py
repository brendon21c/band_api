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
    flickerSearchURL = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&sort=relevance&text={}&format=json&nojsoncallback=1'.format(key, bandSpacing)
    print (flickerSearchURL)
        #Search flickr for cat pictures
    flickrResponse = requests.get(flickerSearchURL)
        #get json back
    #flickrResponseJSONString = flickrResponse.read().decode('UTF-8')
    flickrResponseJson = flickrResponse.json()
        #Get first json object ('photos') which contains another json object ('photo') which is an json array; each
        # element represents one photo. Take element 0
    try:
        firstResponsePhoto = flickrResponseJson['photos']['photo'][0]
        print(firstResponsePhoto)
        secret = firstResponsePhoto['secret']
        id = firstResponsePhoto['id']
        server = firstResponsePhoto['server']
        farm = firstResponsePhoto['farm']

        #print(jsonforphoto)  #Just checking we get the JSON we expect
            #TODO add error handing

        fetchPhotoURL = 'https://farm%s.staticflickr.com/%s/%s_%s_m.jpg' % (farm, server, id, secret)
        print(fetchPhotoURL)   #Again, just checking
        return fetchPhotoURL
    except KeyError:
        pass
