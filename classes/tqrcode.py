#import libraries
import cv2
import numpy as np
import time
from pyzbar import pyzbar
from classes.tcolor import read_color


def read_barcodes(frame):
    mask = cv2.inRange(frame,(0,0,0),(200,200,200))
    thresholded = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    inverted = thresholded # black-in-white


    barcodes = pyzbar.decode(inverted)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(inverted, (x, y),(x+w, y+h), (0, 255, 0), 2)
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        #cv2.putText(inverted, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3 here if qrcode was found excute
        #time.sleep(1)
        tFrame = read_color(frame,barcode_info)
        #cv2.imshow('Color reader', tFrame)
        
    return inverted