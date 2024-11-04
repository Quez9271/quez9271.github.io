from PIL import Image, ImageDraw, ImageFilter

def create_header():
    img = Image.open("header_moto.png")

    im_a = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(im_a)
    draw.ellipse([(-10000,-10000),(15000,600)],fill=255)
    im_a = im_a.filter(ImageFilter.GaussianBlur(200))

    img_al = img.copy()
    img_al.putalpha(im_a)

    img_al.save("header.png")

def trimming(i):
    img = Image.open('images/n'+str(i)+'.png')
    im_a = img.crop((3,51,1199,945))
    im_a.save('images/n'+str(i)+'.png')

trimming(1)
trimming(2)
trimming(3)
trimming(4)