import urllib.request, json



def get_band_schedule():

    TM_key = 'xqbpUW8lmN8nnoX3UHO7suHosVMf8oBF'

    band = "lil wayne"

    url = "https://app.ticketmaster.com/discovery/v2/events.json?attractionId=K8vZ917Gku7&countryCode=CA&apikey=xqbpUW8lmN8nnoX3UHO7suHosVMf8oBF"

    response = urllib.request.urlopen(url)

    data = json.loads(response.read())

    print(data)
