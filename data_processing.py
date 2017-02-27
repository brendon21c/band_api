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

    info_list = []
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

            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                #print('%r page is %d bytes' % (url, len(data)))
                json_return = request_url.json() # TODO need to get specific information from here.

                print(type(json_return))
                artist = json_return["_embedded"]['events'][0] # Gets Artist
                print(artist['name'])
                # print(type(artist))
                # print(len(artist))
                venue = artist["_embedded"]['venues'][0] # Gets venue
                print(venue['name'])
                info_list.append(artist['name'])
                info_list.append(venue['name'])
                # print(type(venue))
                # print(len(venue))

    return info_list
