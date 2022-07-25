from logging.config import IDENTIFIER
import cv2
import time
import os
import PIL
import pysstv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageStat

from pysstv import sstv
from pysstv.color import Robot36

import winsound

import sys

import math

def robot36Header():
    filename = 'Robot36AudioHeader.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

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
    Deos = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))) * 0.3950913977
    return Deos

def imageProcessing(Deos):
    
    img = Image.open('AMEA.png')

    myFont = ImageFont.truetype('arial.ttf', 22)

    #Black Image: 0.0 Deos
    #Dark Grey Image: 26.0760322482 Deos
    #Grey Image: 46.22569353090001 Deos
    #Light Grey Image: 72.3017257791 Deos
    #White Image: 100.00000000011728 Deos

    if Deos >= 0 and Deos <= 25:
        colorChoice = (255,255,255)
    elif Deos >= 26 and Deos <= 50:
        colorChoice = (255,255,225)
    elif Deos >= 51 and Deos <= 75:
        colorChoice = (0,0,0)
    elif Deos >= 76 and Deos <= 101:
        colorChoice = (0,0,0)
    else:
        #colorChoice = (255,0,0)
        pass
    I1 = ImageDraw.Draw(img)
 
    I1.text((30, 30), "KI5UXW Data Transmission", fill=colorChoice, font=myFont, anchor=None, spacing=8, alight='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False)

    I2 = ImageDraw.Draw(img)

    I2.text((30, 60), "The A.M.E.A. Project", fill=colorChoice, font=myFont, anchor=None, spacing=8, alight='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False)
 
# Display edited image

    img.show()
 
# Save the edited image
    img.save("AMEA.png")

def ConvSSTV():
    baseImage = Image.open('AMEA.png')
    baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
    sstv = Robot36(baseImage, 44100, 16)
    sstv.write_wav('transmission.wav')

def AudioPlay():
    filename = 'transmission.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

def IDAudioPlay():
    filename = 'IntroductionMorseCode.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

def dataSplitter(thing):
    thing = str(thing)
    return [char for char in thing]
    #From https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/

def dataConversion(number):
    if number < 10 and number > 0:
        number = round(number, 2)
        number = "+" + str(number)
    elif number < 100 and number > 0:
        number = round(number, 1)
        number = "+" + str(number)
    elif number < 1000 and number > 0:
        number = round(number, 0)
        number = "+" + str(number)
    elif number > -10 and number < 0:
        number = round(number, 2)
        number = str(number)
    elif number > -100 and number < 0:
        number = round(number, 1)
        number = str(number)
    elif number > -1000 and number < 0:
        number = round(number, 0)
        number = str(number)
    else:
        number = str(number)
        print("Number outside of bounds.")
    return number

def transmitSSTVPicture():
    takePic()
    lightLevel = lightAnalysis()
    print(str(lightLevel), "Deos")
    imageProcessing(lightLevel)
    ConvSSTV()
    robot36Header()
    AudioPlay()
    return lightLevel

def transmitSSTVData(dataChosen):
    workingNumber = dataConversion(dataChosen)
    transmissionList = dataSplitter(workingNumber)
    print(transmissionList)
    for character in transmissionList:
        if character == '1':
            baseImage = Image.open('One.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '2':
            baseImage = Image.open('Two.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '3':
            baseImage = Image.open('Three.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '4':
            baseImage = Image.open('Four.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '5':
            baseImage = Image.open('Five.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '6':
            baseImage = Image.open('Six.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '7':
            baseImage = Image.open('Seven.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '8':
            baseImage = Image.open('Eight.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '9':
            baseImage = Image.open('Nine.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '0':
            baseImage = Image.open('Zero.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '.':
            baseImage = Image.open('Decimal.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '-':
            baseImage = Image.open('Negative.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        elif character == '+':
            baseImage = Image.open('Positive.jpg')
            baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
            sstv = Robot36(baseImage, 44100, 16)
            sstv.write_wav('data.wav')
            filename = 'data.wav'
            robot36Header()
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        time.sleep(0.25)

Deos = transmitSSTVPicture()
transmitSSTVData(Deos)
print("Program Complete!")