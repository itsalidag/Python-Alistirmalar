
from pyzbar import pyzbar
from Pillow import Image
import cv2


camera = cv2.VideoCapture(0)
ret, frame = camera.read()

while ret:
    ret, frame = camera.read()
    cv2.imshow("me",frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        print(barcode_text)
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame