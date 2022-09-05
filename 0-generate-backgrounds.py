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

    r = random.randint(40,200)
    g = random.randint(40,200)
    b = random.randint(40,200)
    rgb = (r,g,b)

    date_string = time.strftime("%Y-%m-%d-%H_%M_%S")

    img = Image.new('RGB', (width, height), color='black')
    imgDraw = ImageDraw.Draw(img)
    imgDraw.multiline_text((-12, -5), censored, font = font, fill=rgb)
    img.save('output/background-' + str(how_many) + '_' + date_string + '.png')

    how_many -=1
