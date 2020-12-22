import sys
import cv2 
import pytesseract
from PIL import Image

img = Image.open("C:/Users/Saikian/Downloads/Assignment/2.JPG")  
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
print(pytesseract.image_to_string(img))