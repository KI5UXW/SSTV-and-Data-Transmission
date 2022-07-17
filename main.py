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
from pysstv.color import Robot36

import winsound

import struct, sys

from PIL import ImageFont

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
    I2.text((30, 46), "The A.M.E.A. Project", fill=(0, 0, 0), font=None, anchor=None, spacing=8, alight='left', direction=None, features=None, language=None, stroke_width=3, stroke_fill=None, embedded_color=False)
 
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
imageProcessing()
ConvSSTV()
AudioPlay()