import numpy
from PIL import Image

#Grab all of the pixels inside of the image and convert them to a numpy array
image = Image.open("image.jpg").convert('L')
pixels = numpy.array(image)



def pixel(x, y):
    #Get the pixel at the specified location
    return pixels[y,x]




