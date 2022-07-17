import cv2
import time
import os
import PIL
import pysstv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageStat


import unittest
from io import BytesIO
from itertools import islice
import mock
from mock import MagicMock
import hashlib

from pysstv import sstv
from pysstv.sstv import SSTV
from pysstv.tests.common import load_pickled_asset
from pysstv.color import Robot36

import winsound

import struct, sys

import math

def takePic():
    # initialize the camera
    # If you have multiple camera connected with 
    # current device, assign a value in cam_port 
    # variable according to that
    cam_port = 0
    cam = cv2.VideoCapture(0)
  
    # reading the input using the camera
    result, image = cam.read()
  
    # If image will detected without any error, 
    # show result
    if result:
  
        # showing result, it take frame name and image 
        # output
        cv2.imshow("AMEA", image)
        
        #Enable script below to show the image while running the program.
        #time.sleep(5)
  
        # saving image in local storage
        cv2.imwrite("AMEA.png", image)
  
        # If keyboard interrupt occurs, destroy image 
        # window
        cv2.destroyWindow("AMEA")
  
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

def lightAnalysis():
    #Flashlight in front of camera: 247.43088462912542 (Approximately 250 Units)
    #Finger covering camera: 3.6265194813513904 (Approximately 0 Units)
    im = Image.open('AMEA.png')
    stat = ImageStat.Stat(im)
    r,g,b = stat.mean
    Deos = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    return Deos

def imageProcessing(Deos):
    
    img = Image.open('AMEA.png')

    myFont = ImageFont.truetype('arial.ttf', 15)

    I1 = ImageDraw.Draw(img)
 
    I1.text((30, 36), "KI5UXW Experimental Data Transmission", fill=(0, 0, 0), font=myFont, anchor=None, spacing=8, alight='left', direction=None, features=None, language=None, stroke_width=1, stroke_fill=None, embedded_color=False)

    I2 = ImageDraw.Draw(img)

    I2.text((30, 46), "The A.M.E.A. Project", fill=(0, 0, 0), font=myFont, anchor=None, spacing=8, alight='left', direction=None, features=None, language=None, stroke_width=1, stroke_fill=None, embedded_color=False)
 
# Display edited image

    img.show()
 
# Save the edited image
    img.save("AMEA.png")

def ConvSSTV():
    baseImage = Image.open('AMEA.png')
    baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
    sstv = Robot36(baseImage, 44100, 16)
    #for freq, msec in sstv.gen_freq_bits():
        #sys.stdout.write(struct.pack('ff', freq, msec))
    sstv.write_wav('transmission.wav')

def AudioPlay():

    filename = 'transmission.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)


    

takePic()
lightLevel = lightAnalysis()
#print(str(lightLevel), "Deos")
imageProcessing(lightLevel)
ConvSSTV()
AudioPlay()