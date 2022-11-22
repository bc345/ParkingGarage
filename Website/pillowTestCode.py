# -*- coding: utf-8 -*-
"""
Python Pillow Code to generate an image
"""


from PIL import Image, ImageDraw, ImageFont

text1 = 'Testing'
img_name = 'ParkingGarageOne.png'
color = 'dark_blue'

background = Image.open('DjangoFlow.png')
foreground = Image.open('test.png')

colors = {
        'dark_blue':{'c':(27,53,81)}
        }

def add_color(image,c,transparency):
    color = Image.new('RGB', image.size,c)
    mask = Image.new('RGBA',image.size, (0,0,0,transparency))
    return Image.composite(image,color,mask).convert('RGB')

def add_text(img,color,text1,text2,logo=False,font='Roboto-Bold.ttf',font-size=75):
    draw = ImageDraw.draw(img)
    
    p_font = color['p_font']
    s_font = color['s_font']
    
    img_w, img_h = img.size
    height = img_h // 3
    font = ImageFont.truetype(font,size=font_size)
    
    if logo == False:
        ceter_text(img,font,text1,text2,p_font,s_font)
    else:
        text1_offset = (img_w // 4, height)
        text2_offset = (img_w // 4, height + img_h // 5)
        draw.text(text1_offset, text1, fill=p_font, font=font)
        draw.text(text2_offset, text2, fill=s_font, font=font)
    return img

def write_image(background,color,text1,text2,foreground=''):
    background = add_color(background,color['c'],25)
    if not foreground:
        add_text(background,color,text1,text2)
    else:
        add_text(background,color,text1,text2,logo=True)
        add_logoo(background,foreground)
    return background

if __name__ == '__main__'
    background = write_image(background,colors[color],text1,text2, foreground=foreground)
    background.save(img_name)
    
