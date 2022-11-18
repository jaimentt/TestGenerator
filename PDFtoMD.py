from PIL import Image
from pdf2image import convert_from_path
import pytesseract


Pdf_file_path = 'testPdf.pdf' #your file path

Images = convert_from_path(Pdf_file_path, dpi=100)

Counter=1
for page in Images:
       idx= "image_"+str(Counter)+".jpg" ##or ".png"
       page.save(idx, 'JPEG')
       Counter += 1

file=Counter-1
output= 'test.md' #where you want to save and file name
f=open(output, "w")


for j in range(1,file):
    idx= "image_"+str(j)+".jpg" ##or ".png"
    print (idx)         
    text=str(pytesseract.image_to_string(Image.open(idx)))
    f.write(text)
f.close()