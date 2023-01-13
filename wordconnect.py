import PIL.Image
import pygame as py
from pygame.locals import *
import math

py.init()
screen = py.display.set_mode((1000, 500))
screen.fill((255, 255, 255))
letters = ["l", "o"]
correct_words = []
input_rect = py.Rect(200, 200, 140, 32)
score_count = 0
i = -1
working = True
list_images = {'a': "hellop/Platformer-word-game-master/images/Letters/1.png", 'b': "hellop/Platformer-word-game-master/images/Letters/9.png",
                'c': "hellop/Platformer-word-game-master/images/Letters/19.png",
              'd': "hellop/Platformer-word-game-master/images/Letters/15.png", 'e': "hellop/Platformer-word-game-master/images/Letters/26.png",
                'f': "hellop/Platformer-word-game-master/images/Letters/23.png",
              'g': "hellop/Platformer-word-game-master/images/Letters/18.png", 'h': "hellop/Platformer-word-game-master/images/Letters/2.png",
                'i': "hellop/Platformer-word-game-master/images/Letters/7.png",
              'j': "hellop/Platformer-word-game-master/images/Letters/12.png", 'k': "hellop/Platformer-word-game-master/images/Letters/3.png",
                'l': "hellop/Platformer-word-game-master/images/Letters/16.png",
              'm': "hellop/Platformer-word-game-master/images/Letters/28.png", 'n': "hellop/Platformer-word-game-master/images/Letters/25.png",
                'o': "hellop/Platformer-word-game-master/images/Letters/22.png",
              'p': "hellop/Platformer-word-game-master/images/Letters/0.png", 'q': "hellop/Platformer-word-game-master/images/Letters/6.png",
                'r': "hellop/Platformer-word-game-master/images/Letters/17.png",
              's': "hellop/Platformer-word-game-master/images/Letters/20.png", 't': "hellop/Platformer-word-game-master/images/Letters/13.png",
                'u': "hellop/Platformer-word-game-master/images/Letters/21.png",
              'v': "hellop/Platformer-word-game-master/images/Letters/24.png", 'w': "hellop/Platformer-word-game-master/images/Letters/11.png",
                'x': "hellop/Platformer-word-game-master/images/Letters/10.png",
              'y': "hellop/Platformer-word-game-master/images/Letters/4.png", 'z': "hellop/Platformer-word-game-master/images/Letters/14.png"}
coord = []
entered = []

word = ""
mystery_letter = ""
mystery_number = 3
score = 0
rect_pressed = False
on = True
pressed = False


def background(x,y,z, c):
    bg_image = py.image.load("hellop/flat-design-copy-space-winter-background_52683-48883.jpeg")
    bg_image = py.transform.scale(bg_image, (1000, 500))
    table = py.Surface((420,c))
    table.set_alpha(128)
    table.fill((x,y,z))
    screen.blit(bg_image, (0, 0))
    screen.blit(table, (300, 25))

def place(n):
    global on
    global coord

    if on == True:
        a = 0
        adding = (2 * 3.14) / n
        for i in range(0, n):
            im = py.image.load(list_images[letters[i]])
            im = py.transform.scale(im, (35, 35))
            screen.blit(im,((480 + 130 * math.cos(a), 300 + 130 * math.sin(a))) )
            if len(coord) < len(letters):
                coord.append((480 + 130 * math.cos(a), 300 + 130 * math.sin(a)))
            a += adding

def lines():
    if entered != []:
        for cd in range(len(entered) - 1):
            py.draw.line(screen, (34, 153, 153), (entered[cd][0]+ 20, entered[cd][1] + 20), (entered[cd + 1][0] + 20, entered[cd + 1][1]+  20),width = 3 )
def near(x, y):
    z = []
    for i in range(len(x)):
        z.append((math.sqrt(pow(x[i][0] - y[0], 2)) + math.sqrt(pow(x[i][1] - y[1], 2))))

    return x[z.index(min(z))]


def show():
    global word

    adding = 30
    subtraction = 15
    for i in range(len(word)):
        im = py.image.load(list_images[word[i]])
        im = py.transform.scale(im, (25, 25))
        screen.blit(im, (500 + (adding * i) - (subtraction * len(word)), 90))


def mystery(input):
    if pressed == True:
        py.draw.rect(screen, (30, 212, 212), input_rect)
        font = py.font.Font(None, 32)

        if rect_pressed == True:
            py.draw.rect(screen, (95, 204, 0), input_rect)
            text_pressed = font.render(input, True, (255, 255, 255))
            if input != "":
                screen.blit(text_pressed, input_rect)


def mysterybutton(x):
    if x == True:
        image = py.image.load("hellop/question.png")
        image = py.transform.scale(image, (50, 50))
        screen.blit(image, (0,0))

def submit(x):
    if x == True:
        image = py.image.load("hellop/arrow1.png")
        image_submit = py.transform.scale(image, (50, 50))
        screen.blit(image_submit, (850, 340))

def score_show(x):
    font = py.font.Font(None, 50)
    if x == True:
        text = font.render(f"score: {score}", True, (0,0,0))
        screen.blit(text, (800, 50))
    if x == False:
        text1 = font.render("game over", True, (0,0,0))
        text = font.render(f"score: {score}", True, (0,0,0))
        screen.blit(text1, (500, 100))
        screen.blit(text, (500, 250))

run = True
background(255,255,255, 100)
place(len(letters))
mysterybutton(working)
submit(working)
start = ()
clock = py.time.Clock()
while run:
    if working == True:
        clock.tick()
        mouse = py.mouse.get_pos()

        for ev in py.event.get():
            if ev.type == QUIT:
                py.quit()
            if ev.type == KEYDOWN:
                if mystery_number != 0 and ev.unicode not in letters and rect_pressed == True  and mystery_number != 0:
                    if ev.unicode != '\r':
                        letters.append(ev.unicode)
                        mystery(ev.unicode)
                        coord = []
                        mystery_number -= 1


            if ev.type == MOUSEBUTTONDOWN:
                if 850< mouse[0] < 950 and  340< mouse[1] < 390:
                    background(255,255,255,400)
                    on = False
                    working = False
                elif 0 < mouse[0] < 50 and 0 < mouse[1] < 50:
                    i += 1
                    if i % 2 == 0:
                        pressed = True
                        print(pressed)
                    else:
                        pressed = False
                        print(pressed)
                if input_rect.collidepoint(mouse) and pressed== True:
                    rect_pressed = True

                mystery("")

                if on == True and 300 < mouse[0] < 700 and 25 < mouse[1] < 475:

                    start = near(coord, mouse)
                    if start not in entered:

                        word += letters[coord.index(start)]
                        entered.append(start)
                    else:
                        word = ""
                        entered = []

                if pressed == False:

                    background(255, 255, 255, 450)
                    place(len(letters))
                    mysterybutton(working)
                    score_show(working)
                    submit(working)
                    if ev.type == KEYDOWN:
                        if mystery_number != 0 and ev.unicode not in letters and rect_pressed == True:

                            if ev.unicode != '\r':
                                letters.append(ev.unicode)
                                mystery(ev.unicode)


        if start != ():
            background(255,255,255, 450)
            mysterybutton(working)
            place(len(letters))
            submit(working)
            score_show(working)
            py.draw.line(screen, (34, 153, 153), (start[0] + 20, start[1] + 20), (mouse[0] + 20, mouse[1] + 20), width=5)
            lines()
            show()
            if len(word) == len(letters) and word not in correct_words:
                start= ()
                entered = []
                background(201, 47, 4, 450)
                mysterybutton(working)
                score_show(working)
                place(len(letters))
                show()
                print(word)
                word = ""

            elif word in correct_words:
                score += 1
                start= ()
                entered = []
                background(235, 235, 35, 450)
                mysterybutton(working)
                score_show(working)
                place(len(letters))
                show()
                print(word)
                word = ""


    score_show(working)
    py.display.update()
