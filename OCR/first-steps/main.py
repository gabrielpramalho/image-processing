from email.mime import image
import pytesseract as tess
import argparse
import cv2 as cv

tess.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

text = tess.image_to_string(image)
print(text)
cv.imshow('img', image)

cv.waitKey(0)