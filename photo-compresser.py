# This will Compress your photos into lower sizes while the quality same.
import PIL
from PIL import Image
from tkinter.filedialog import *
fl=askopenfilenames()
img = Image.open(fl[0])
img.save("result.jpg", "JPEG", optimize = True, quality = 10)