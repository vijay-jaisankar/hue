import requests
import json

from unsplash_keys import access_key


request_string = "https://api.unsplash.com/photos/random/?client_id="+access_key

r = requests.get(request_string)

#print(r.json())

x = r.json()

link = (x["urls"]["raw"])
print(link)