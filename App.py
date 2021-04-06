#import libraries
import cv2
import numpy as np
from pyzbar import pyzbar
from classes.tcolor import read_color
from classes.tqrcode import read_barcodes
from classes.up import sendtoFTP
from classes.up import sendData
from io import BytesIO


def main():

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()