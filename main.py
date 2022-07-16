import cv2
import time
import os
import PIL

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
    im = PIL.open(r"C:\Users\hubba\documents\GitHub\SSTV-and-Data-Transmission\AMEA.png")


takePic()
imageProcessing()