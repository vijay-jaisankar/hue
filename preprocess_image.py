import numpy as np
import pandas as pd 

# To read the image 
from imageio import imread 

# Preprocessing the image
from skimage.transform import resize 

import matplotlib.pyplot as plt 


image_link  = "https://images.unsplash.com/photo-1625480963923-7c5b0de97624?ixid=MnwyNDU5MDV8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjU5OTY1MTY&ixlib=rb-1.2.1"
img = imread(image_link)

img = resize(img, (300,300))

data = pd.DataFrame(img.reshape(-1,3), columns = ["Red","Green","Blue"])

print(data)