import cv2
import time
import os
import PIL
import pysstv
from PIL import Image
from PIL import ImageDraw

import unittest
from io import BytesIO
from itertools import islice
import mock
from mock import MagicMock
import hashlib

from pysstv import sstv
from pysstv.sstv import SSTV
from pysstv.tests.common import load_pickled_asset

from playsound import playsound

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

def imageProcessing():
    
    img = Image.open('AMEA.png')
 
    
    I1 = ImageDraw.Draw(img)
 
# Add Text to an image
    I1.text((30, 36), "KI5UXW Experimental Data Transmission", fill=(0, 0, 0))

    I2 = ImageDraw.Draw(img)
 
# Add Text to an image
    I2.text((30, 46), "The A.M.E.A. Project", fill=(0, 0, 0))
 
# Display edited image
    img.show()
 
# Save the edited image
    img.save("AMEA.png")

def ConvSSTV():
    baseImage = Image.open('AMEA.png')
    s = SSTV(baseImage, 48000, 16)
    s.VIS_CODE = 0x00
    s.SYNC = 7
    s.write_wav('transmission.wav')

def AudioPlay():
    playsound('transmission.wav')


    

takePic()
imageProcessing()
ConvSSTV()
AudioPlay()