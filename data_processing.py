import urllib.request, json
import itertools
import json
import requests
import sys
import urllib.request
import concurrent.futures

''' This is meant to process url concurrency, possibly more to come.'''


# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def concurrent_requests(url_list):

    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in url_list}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                #data = future.result()
                print(url)
                request_url = requests.get(url)
                json_return = request_url.json() # TODO need to get specific information from here.

                url_return = handle_tour_json(json_return)

                return url_return


            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))


def handle_tour_json(json_dict):

    info_list = []

    try:


        # I want this to loop over the whole json and return a record if it finds MN as the
        # stateCode, its not working.
        states = [state["name"] for state in json_dict["_embedded"]['events']
                    if state[0]["_embedded"]['venues']["state"]["stateCode"] == "IL"]

        print(states)



    except Exception as e:

        print("problem", e)


    artist = json_dict["_embedded"]['events'][0] # Gets Artist
    print(artist['name'])
    venue = artist["_embedded"]['venues'][0] # Gets venue
    print(venue['name'])
    info_list.append(artist['name'])
    info_list.append(venue['name'])

    return info_list
