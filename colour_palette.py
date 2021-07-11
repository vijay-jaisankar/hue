import requests
import json
import numpy as np
import pandas as pd 
from unsplash_keys import access_key
from imageio import imread 
from skimage.transform import resize 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from colorit import *


_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'

def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)

def getRandomImageLink(query = []) -> str:

    query_string = "&query="
    for i in range(len(query)):
        query_string += query[i]
        if i != (len(query) - 1):
            query_string += ","
    
    request_string = "https://api.unsplash.com/photos/random/?client_id="+access_key+""+query_string
    r = requests.get(request_string)
    x = r.json()
    link = (x["urls"]["raw"])
    return link

def preProcessImageReturnDataframe(dimensions = (300,300), query = []):
    image_link = getRandomImageLink(query=query)
    img = imread(image_link)
    img = resize(img, dimensions)
    
    data = pd.DataFrame(img.reshape(-1,3), columns = ["Red","Green","Blue"])
    return data 

def getKMeansModel(num_clusters = 3, random_state = 42):
    kmeans_model = KMeans(
    n_clusters= num_clusters,
    random_state= random_state
    )
    
    return kmeans_model 

def getHexValues(num_clusters = 3, random_state = 42,dimensions = (300,300), query=[]) -> list:
    df = preProcessImageReturnDataframe(dimensions=dimensions, query=query)
    model = getKMeansModel(num_clusters=num_clusters,random_state=random_state)
    cluster_list = model.fit_predict(df)
    cluster_centers = model.cluster_centers_
    
    list_of_colours = []
    for i in cluster_centers:
        temp_list = [int(x*255) for x in i]
        list_of_colours.append(tuple(temp_list))
    
    list_of_hex_values = []
    for i in list_of_colours:
        list_of_hex_values.append(triplet(i,UPPERCASE))
    
    return list_of_colours, list_of_hex_values


if __name__ == "__main__":
    
    print("How many clusters do you want?")
    num_clusters = int(input())
    print("Enter your search parameters, separated by commas")
    param_string = str(input())
    query = param_string.split(",")
    
    listRGB, listHex = getHexValues(num_clusters = num_clusters, random_state = 5, query=query)
    
    init_colorit()
    for i in range(len(listRGB)):
        print(background(listHex[i],listRGB[i]))

    

    