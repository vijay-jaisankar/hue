import numpy as np
import pandas as pd 

# Conversion Constants
_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'


# To read the image 
from imageio import imread 

# Preprocessing the image
from skimage.transform import resize 

# To plot things, if the need arises
import matplotlib.pyplot as plt 

# Clustering algorithm
from sklearn.cluster import KMeans

def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)



image_link  = "https://images.unsplash.com/photo-1625480963923-7c5b0de97624?ixid=MnwyNDU5MDV8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjU5OTY1MTY&ixlib=rb-1.2.1"
img = imread(image_link)

img = resize(img, (300,300))

data = pd.DataFrame(img.reshape(-1,3), columns = ["Red","Green","Blue"])

#print(data)

# Define the Model
n_clusters = 3
random_state_fixed = 42

kmeans_model = KMeans(
    n_clusters= n_clusters,
    random_state= random_state_fixed
)

# Fit the model

cluster_list = kmeans_model.fit_predict(data)
#print(cluster_list)

# Get cluster centers

cluster_centers = kmeans_model.cluster_centers_
#print(cluster_centers)

# Get colours

list_of_colours = []
for i in cluster_centers:
    temp_list = [int(x*255) for x in i]
    list_of_colours.append(tuple(temp_list))

# print(list_of_colours)

# Conversion of the RGB triplet into Hex code


list_of_hex_values = []
for i in list_of_colours:
    list_of_hex_values.append(triplet(i,UPPERCASE))

print(list_of_hex_values)
