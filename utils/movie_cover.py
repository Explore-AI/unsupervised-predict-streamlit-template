from PIL import Image, ImageDraw, ImageFont

def cover(movie_name):

    # get an image
    base = Image.open('resources/app_images/IMG.PNG').convert('RGBA')
    # Get the light colour of the image
    txt = Image.new('RGBA', base.size, (255,255,255,255))
    # Select the font that will be used on the image
    fnt = ImageFont.truetype('resources/image_styles/FreeMono.ttf', 20)
    # Get a drawing context
    draw = ImageDraw.Draw(txt)
    # draw text, half opacity
    draw.text((10,10), movie_name, font=fnt, fill='black')
    # draw text, full opacity

    output = Image.alpha_composite(base, txt)

    return output.save('resources/app_images/flie1.png')