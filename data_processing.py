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

''' With the apis handling the url proccessing I am not sure how to handle concurency.'''
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

                process_image(url) # process band photos and return to web app.


            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
