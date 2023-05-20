from PIL import Image
from pytesseract import pytesseract
import numpy as np

pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
filename = 'tes.jpg'
img1 = np.array(Image.open(filename))

text = pytesseract.image_to_string(img1)
print(text)