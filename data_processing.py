import urllib.request, json
import itertools
import json
import requests
import sys
import urllib.request
import concurrent.futures

import logging as log

''' This is meant to process url concurrency, possibly more to come.'''

''' The section on concurency I got from the documentation, I still don;t full understand it.'''
# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def concurrent_requests(url_list):

    list_of_json = []

    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in url_list}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            print(url)
            try:
                #data = future.result()
                print(url)
                request_url = requests.get(url)

                json_return = request_url.json()

                list_of_json.append(json_return)

                #url_return = handle_tour_json(json_return)


            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))




    tour_results_return = handle_tour_json(list_of_json[0]) # returns the api call results from ticketmaster

    return tour_results_return

# retrieves the venue name, ticket url link or no result string for the artist query.
def handle_tour_json(json_dict):

    info_list = []

    try:

        artist = json_dict["_embedded"]['events'][0]
        print(artist['url']) # ticket infor url
        venue = artist["_embedded"]['venues'][0] # Gets venue
        print(venue['name'])
        info_list.append(artist['url'])
        info_list.append(venue['name'])

        return info_list


    except Exception as e:

        log.error("problem", e)

        no_artist_found = "Sorry, that artist is not playing Minnesoata at this time."

        ## return an empty list if no results found

        info_list.append(no_artist_found)
        log.info(info_list)

        return info_list
