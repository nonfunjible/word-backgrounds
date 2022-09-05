from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
from better_profanity import profanity
import time

width = 2000
height = 2000
number_of_words = 2400
number_of_characters = 300
font = ImageFont.truetype(r'cour.ttf', 48)
make_color = lambda : (random.randint(50, 255), random.randint(50, 255), random.randint(50,255))

how_many = int(input("How many? "))

while how_many > 0:

    def list_of_words():
        words = []
        for i in range(number_of_words):
            words.append(random.choice(open("pwd.txt").read().split()))
        return(" ".join(words))

    wrapper = textwrap.TextWrapper(width=number_of_characters)
    value = str(list_of_words())
    wrapped = wrapper.fill(text=value)

    censored = profanity.censor(wrapped, "")

    img = Image.new("RGB", (width, height), (0,0,0)) # scrap image
    draw = ImageDraw.Draw(img)
    img2 = Image.new("RGB", (width, height), (0,0,0)) # final image

    fill = " o "
    x = 0
    w_fill, y = draw.textsize(fill)
    x_draw, x_paste = 0, 0
    for c in censored:
        w_full = draw.textsize(fill+c)[0]
        w = w_full - w_fill     # the width of the character on its own
        draw.text((x_draw,0), fill+c, make_color())
        iletter = img.crop((x_draw+w_fill, 0, x_draw+w_full, y))
        img2.paste(iletter, (x_paste, 0))
        x_draw += w_full
        x_paste += w

    date_string = time.strftime("%Y-%m-%d-%H_%M_%S")
    img2.save('output/background-' + str(how_many) + '_' + date_string + '.png')

    how_many -=1

