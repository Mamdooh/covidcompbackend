import numpy as np 
import cv2 
from datetime import date
from classes.up import sendtoFTP
from classes.up import whoname
from io import BytesIO
import os
from classes.up import sendData


def read_color(imageFrame,barcode_info):

        # Convert the imageFrame in 
        # BGR(RGB color space) to 
        # HSV(hue-saturation-value) 
        # color space 
        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

        # Set range for brown color and 
        # define mask 
        brown_lower = np.array([10, 150, 20], np.uint8) 
        brown_upper = np.array([20, 220, 200], np.uint8) 
        brown_mask = cv2.inRange(hsvFrame, brown_lower, brown_upper) 

        # Set range for green color and 
        # define mask 
        # B G R
        green_lower = np.array([25, 52, 72], np.uint8)
        green_upper = np.array([102, 255, 255], np.uint8)

        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 

        # Morphological Transform, Dilation 
        # for each color and bitwise_and operator 
        # between imageFrame and mask determines 
        # to detect only that particular color 
        kernal = np.ones((5, 5), "uint8") 
        
        # For brown color 
        brown_mask = cv2.dilate(brown_mask, kernal) 
        res_brown = cv2.bitwise_and(imageFrame, imageFrame, 
                                                        mask = brown_mask) 
        # For green color 
        green_mask = cv2.dilate(green_mask, kernal) 
        res_green = cv2.bitwise_and(imageFrame, imageFrame, 
                                                                mask = green_mask) 
        
################################################################################################################################
        # Creating contour to track brown color 
        contours, hierarchy = cv2.findContours(brown_mask, 
                                                                                cv2.RETR_TREE, 
                                                                                cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
                area = cv2.contourArea(contour) 
                if(area > 10000): 
                        x, y, w, h = cv2.boundingRect(contour) 
                        imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                                                        (x + w, y + h), 
                                                                        (0, 180, 255), 2) 

                        BName = whoname(barcode_info)
                        img_name = BName + " - INFECTED (Access Denied)"
                        retval, buffer = cv2.imencode('.jpg', imageFrame)
                        sendtoFTP(img_name,buffer)

################################################################################################################################
        # Creating contour to track green color 
        contours, hierarchy = cv2.findContours(green_mask, 
                                                                                cv2.RETR_TREE, 
                                                                                cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
                area = cv2.contourArea(contour) 
                if(area > 10000): 
                        x, y, w, h = cv2.boundingRect(contour) 
                        imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                                                        (x + w, y + h), 
                                                                        (0, 255, 0), 2) 
                        
                        cv2.putText(imageFrame, "Green Colour", (x, y), 
                                                cv2.FONT_HERSHEY_SIMPLEX, 
                                                1.0, (0, 255, 0)) 

                        BName = whoname(barcode_info)
                        img_name = BName + " - HEALTHY (Access Granted)"
                        retval, buffer = cv2.imencode('.jpg', imageFrame)
                        sendtoFTP(img_name,buffer)

################################################################################################################################
        return imageFrame
