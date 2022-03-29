import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode()
pygame.display.set_caption("maze runner")
background = pygame.image.load("img.png")
logo = pygame.image.load("rp.png")
pygame.display.set_icon(logo)
playerIMG = pygame.image.load("pro2.png")
# wallIMG = pygame.image.load("img.png")

# time

playerIMGx = 64
playerIMGy = 64

screenSize = screen.get_size()
xAxis = screenSize[0]
yAxis = screenSize[1]

PLx = xAxis / 2
PLy = 0.8 * yAxis
changex = 0
changey = 0

stack = []
start_ticks = pygame.time.get_ticks()  # starter tick

WLx = 10
WLy = 10
changeWx = 0
changeWy = 0

enemy1 = pygame.image.load("img.png")
enemy2 = pygame.image.load("img.png")
enemy3 = pygame.image.load("img.png")

en1x = random.randint(400, 600)
en2x = random.randint(600, 800)
en3x = random.randint(800, 900)

en1y = 50
en2y = 50
en3y = 50


def player(x, y):
    screen.blit(playerIMG, (PLx, PLy))


# def wall(x, y):
#     screen.blit(wallIMG, (x, y))


# def create_wall(y):
#     x = int(0.3 * xAxis)
#     y = int(0.7 * yAxis)
#     val = random.randrange(x, y, 10);
#     WLx = val
#     WLy = y
#     wall(WLx, WLy)

def isCollideSinglePt(enx,eny):
    arr_row_inc=[0,50,0,50]
    arr_col_inc=[0,0,50,50]
    for i in range(0,4):
        x=arr_row_inc[i]+PLx
        y=arr_col_inc[i]+PLy
        if enx<=x and x<=enx+120 and eny<=y and y<=eny+60:
            return True

    return False


def isCollide ():
    if isCollideSinglePt(en1x,en1y) or isCollideSinglePt(en2x,en2y) or isCollideSinglePt(en3x,en3y):
        return True
    #Shantanu
    # if PLx<=en1x and en1x<=PLx+64 and PLy<=en1y and en1y<=PLy+64:
    #     return True
    # if PLx<=en2x and en2x<=PLx+64 and PLy<=en2y and en2y<=PLy+64:
    #     return True
    # if PLx<=en3x and en3x<=PLx+64 and PLy<=en3y and en3y<=PLy+64:
    #     return True

    #Bhargav
    # if PLx >= en1x and PLx <= en1x+120 and PLy >= en1y and PLy <= en1y + 60:
    #     return True
    # if PLx >= en2x and PLx <= en2x+120 and PLy >= en2y and PLy <= en2y + 60:
    #     return True
    # if PLx >= en3x and PLx <= en3x+120 and PLy >= en3y and PLy <= en3y + 60:
    #     return True
    #
    # if PLx+64 >= en1x and PLx+64 <= en1x+120 and PLy >= en1y and PLy <= en1y + 60:
    #     return True
    # if PLx+64 >= en2x and PLx+64 <= en2x+120 and PLy >= en2y and PLy <= en2y + 60:
    #     return True
    # if PLx >= en3x and PLx <= en3x+120 and PLy >= en3y and PLy <= en3y + 60:
    #     return True
    #
    # if PLx >= en1x and PLx <= en1x+120 and PLy >= en1y and PLy <= en1y + 60:
    #     return True
    # if PLx >= en2x and PLx <= en2x+120 and PLy >= en2y and PLy <= en2y + 60:
    #     return True
    # if PLx >= en3x and PLx <= en3x+120 and PLy >= en3y and PLy <= en3y + 60:
    #     return True
    return False

def check(x, y):
    global PLx
    if x > xAxis * 0.7:
        PLx = xAxis * 0.7
    if x < xAxis * 0.3:
        PLx = xAxis * 0.3
    global PLy
    if y < yAxis * 0.45:
        PLy = yAxis * 0.45
    if y > yAxis * 0.8:
        PLy = yAxis * 0.8


incValue = 0.5

running = True

while running:
    if isCollide() :
        running = False
    screen.fill((231, 123, 23))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            stack.append(event.key)
        elif event.type == pygame.KEYUP:
            stack.remove(event.key)

        if len(stack) != 0:
            key = stack.pop()
            stack.append(key)
            if key == pygame.K_RIGHT:
                changex = 0.5
                changey = 0
            elif key == pygame.K_LEFT:
                changex = -0.5
                changey = 0
            elif key == pygame.K_DOWN:
                changex = 0
                changey = 0.5
            elif key == pygame.K_UP:
                changex = 0
                changey = -0.5
        # if len(stack) == 0:
        #     changex = 0
        #     changey = 0
    PLx += changex
    PLy += changey
    check(PLx, PLy)
    player(PLx, PLy)

    en1y += 0.5
    en2y += 0.5
    en3y += 0.5

    if en1y >= yAxis:
        en1x = random.randint(400,450)
        en1y = -random.randint(90,100)

    if en2y >= yAxis:
        en2x = random.randint(650,700)
        en2y = -random.randint(160,180)

    if en3y >= yAxis:
        en3x = random.randint(850,900)
        en3y = -random.randint(200,210)

    screen.blit(enemy1,(en1x,en1y))
    screen.blit(enemy2, (en2x, en2y))
    screen.blit(enemy3, (en3x, en3y))


    # if isCollide() :
    #     running = False
    # changeWx = 0.1
    # changeWy = 0
    # WLx += changeWx
    # WLy += changeWy
    # wall(WLx,WLy)

    # seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    # if seconds > 30:
    #     incValue += 0.1
    #     start_ticks = pygame.time.get_ticks()

    pygame.display.update()
