import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'

img = Image.open("ocr-a-font-sample.png")
text=pytesseract.image_to_string(img)
print(text)