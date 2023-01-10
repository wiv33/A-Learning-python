import pytesseract

from PIL import Image
from cv2 import cv2
import numpy as np
import requests

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

imread = cv2.imread('kcaptcha_image.jpg')

cv2.imshow('img', imread)
cv2.waitKey(0)
img = Image.fromarray(imread)
img.show('tt')
print(pytesseract.image_to_string(imread))
#
# print(pytesseract.image_to_data(img))
