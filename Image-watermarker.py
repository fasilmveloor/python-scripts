# This simple script will watermark any image. You can set the Text, location, and Font.
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
def watermark_img(img_path,res_path, text, pos):
    img = Image.open(img_path)
    wm = ImageDraw.Draw(img)
    col= (9, 3, 10)
    wm.text(pos, text, fill=col)
    img.show()
    img.save(res_path)
img = 'initial.jpg'
watermark_img(img, 'result.jpg','fasilmveloor', pos=(1, 0))