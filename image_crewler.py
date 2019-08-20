import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
image = Image.open(r"")  # enter file path in ""
image_to_data = pytesseract.image_to_string(image)

# image to data with only numbers
# delete if don't need to replace all the sepchar
replacements1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','\'',',','\\','\"',';','.','!',':','\r','\t','=','+','/','\\\\','>','<','&','#','§','“','‘','»','°','%','*']
replacements2 = ['(',')','[',']','{','}','|']
replacements3 = ['-','_','~']
for r in replacements1:
    image_to_data = image_to_data.replace(r, '')
for i in replacements2:
    image_to_data = image_to_data.replace(i, ' ')
for k in replacements3:
    image_to_data = image_to_data.replace(k, '—')

print(image_to_data)