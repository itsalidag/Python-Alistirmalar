# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:04:31 2020

@author: alida
"""

import cv2
from pyzbar import pyzbar
import time
from PIL import Image

info = pyzbar.decode(Image.open("img.png"))
viki = pyzbar.decode(Image.open("vikipedi.jpeg"))
print(viki)

prices = {"9786052498095" : 8}
from playsound import playsound
def beep():
    playsound(r"C:\Users\alida\Desktop\biodiversity-starter\biodiversity_starter\beep-07.mp3")

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcodes = []
        a = 0
        x, y , w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        barcodes.append(barcode_text)
        if len(barcodes) > a:
            beep()
            a +=1
        print(barcode_text)
        print(prices[barcode_text])
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame

def main():
    camera = cv2.VideoCapture(1)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        time.sleep(5)
        frame = read_barcodes(frame)
        cv2.imshow('Barcode reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

main()