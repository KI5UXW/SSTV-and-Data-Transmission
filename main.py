import cv2
import time
import os
import PIL
from PIL import Image
from PIL import ImageDraw

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
    I1.text((28, 36), "KI5UXW Testing Image", fill=(0, 0, 0))
 
# Display edited image
    img.show()
 
# Save the edited image
    img.save("AMEA.png")

takePic()
imageProcessing()