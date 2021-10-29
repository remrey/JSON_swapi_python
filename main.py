import json
import requests
import os, ssl
import time
from collections import defaultdict
from characters import Character
from urllib.request import urlopen


# Solving the Certificate Verification Problem for Python 3.6 and later versions.
# if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
#     ssl._create_default_https_context = ssl._create_unverified_context


# 1_) READING JSON from WEB
url = "https://swapi.dev/api/films/?format=json"
# response = urlopen(url).read()
# obj = json.loads(response)
obj = requests.get(url).json()

try:
    with open('sw_files.json', 'w') as file:
        json.dump(obj["results"],file,indent = 2)
except Error:
    print(Error)


#1.a_) Accessing url's inside the JSON

# First find out how many movies in the list.
n_mov = obj['count']
print(f"There are total of {n_mov} movies in this list")

# Second, define a function for reading the characters on the movies.
def read_characters(urls, chars):
    for url in urls:
        r = requests.get(url)
        obj = r.json()
        # If the object is already in the file, it will skip.
        if obj["name"] in chars:
            print("Duplicate found... Skipping {}".format(obj["name"]))
            continue

        temp = Character(obj)
        chars[obj["name"]] = temp.jsonEncoder()
        time.sleep(r.elapsed.total_seconds())
        print("Got package: {} in {}...".format(temp.name, r.elapsed.total_seconds()))


chars = {}

# Third, we access to the function from main.
for k,i in enumerate(obj["results"]):
    t1 = time.perf_counter()
    read_characters(i["characters"], chars)
    t2 = time.perf_counter()
    print("---- Package : {} took {} seconds ----".format(i["title"],t2-t1))



# Dumping everything to a local database as json.
with open('chars.json', 'w') as file:
    # json.dump([ob.__dict__ for ob in chars], file, indent = 2)
    json.dump(chars, file, indent = 2)


# # 2_) READING JSON from a FILE
# with open('example.json', 'r') as myfile:
#     data = json.load(myfile)
#
# print(data, type(data))
