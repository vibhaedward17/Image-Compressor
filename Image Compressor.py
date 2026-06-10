import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = PIL.Image.open(file_path)
myWidth, myHeight = img.size

img = img.resize((myWidth, myHeight), PIL.Image.LANCZOS)

img = img.convert("RGB")  

save_path = asksaveasfilename()
img.save(save_path + "compressed.jpg")