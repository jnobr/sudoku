import random as rnd
import pygame
from pygame.locals import *
import copy

pygame.font.init()

font1 = pygame.font.SysFont("arial", 20)


answer_grid = []
xcord = 0
ycord = 0
val = 0
solved = 0
allblanks = 0

black = (0, 0, 0)
white = (200, 200, 200)
red = (255,0,0)
height = 270
width= 270

grid = [ [7,4,1,2,3,5,8,9,6],
         [8,9,6,7,1,4,3,5,2],
         [5,2,3,9,6,8,1,4,7],
         [2,3,8,6,4,9,5,7,1],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9]
        ]

def create_grid():
    global grid
    grid[0] = rnd.sample(range(1,10),9)


    templist = []

    #generating a random line of 9 numbers from 1 to 9
    grid[0] = rnd.sample(range(1,10),9)

    templist = grid[0][:]

    grid[1][2] = templist.pop()
    grid[1][1] = templist.pop()
    grid[1][0] = templist.pop()

    for i in range(3,9):
        grid[1][i] = templist[i-3]

    #shifting the first line by 3 digits to form the secon line

    templist = grid[1][:]

    grid[2][2] = templist.pop()
    grid[2][1] = templist.pop()
    grid[2][0] = templist.pop()

    for i in range(3,9):
        grid[2][i] = templist[i-3]

    #shifting the second line by 3 digits to form third line


    templist = grid[2][:]

    grid[3][0] = templist.pop()

    for i in range(1,9):
        grid[3][i] = templist[i-1]

    #shifting third line by 1 digit to form 4th line



    templist = grid[3][:]

    grid[4][2] = templist.pop()
    grid[4][1] = templist.pop()
    grid[4][0] = templist.pop()

    for i in range(3,9):
        grid[4][i] = templist[i-3]

    #shifting fourth line

    templist = grid[4][:]

    grid[5][2] = templist.pop()
    grid[5][1] = templist.pop()
    grid[5][0] = templist.pop()

    for i in range(3,9):
        grid[5][i] = templist[i-3]

       #shifting fifth line
        

    templist = grid[5][:]

    grid[6][0] = templist.pop()

    for i in range(1,9):
        grid[6][i] = templist[i-1]

    #shifting sixth line 
        

    templist = grid[6][:]

    grid[7][2] = templist.pop()
    grid[7][1] = templist.pop()
    grid[7][0] = templist.pop()

    for i in range(3,9):
        grid[7][i] = templist[i-3]

    #shifting seventh line

    templist = grid[7][:]
    grid[8][2] = templist.pop()
    grid[8][1] = templist.pop()
    grid[8][0] = templist.pop()

    for i in range(3,9):
        grid[8][i] = templist[i-3]
     
    #shifting eigth line

    global answer_grid
    answer_grid = copy.deepcopy(grid)
    

def remove_numbers():
    global grid,allblanks
    for i in range(9):
        for y in range(9):
            if rnd.randint(1,2) == 2:
                grid[i][y] = 0
                allblanks +=1

def print_grid_to_console():       
    for i in range(9):
        for y in range(9):
            print(grid[i][y], end = ' ')

        print("\n")

def get_cord(pos):

    global xcord
    global ycord

    ycord = pos[1]//30
    xcord = pos[0]//30


def highlightbox():
    for i in range(2):
        pygame.draw.line(screen, red, (xcord * 30 , (ycord + i)*30), (xcord * 30 + 30 , (ycord + i)*30), 1)
        pygame.draw.line(screen, red, ( (xcord + i) * 30 , ycord * 30), ((xcord + i) * 30, ycord * 30 + 30 ), 1)


def main():
    global screen,clock,val,solved,answer_grid,allblanks
    global xcord
    global ycord
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    screen.fill(white)




    val = 0
    run = True

    create_grid()
    remove_numbers()


    while run:

        drawGrid(30)
        drawGrid(90)
        highlightbox()
        addNumber()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                get_cord(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    val = 1
                if event.key == pygame.K_2:
                    val = 2                    
                if event.key == pygame.K_3:
                    val = 3
                if event.key == pygame.K_4:
                    val = 4
                if event.key == pygame.K_5:
                    val = 5
                if event.key == pygame.K_6:
                    val = 6
                if event.key == pygame.K_7:
                    val = 7
                if event.key == pygame.K_8:
                    val = 8
                if event.key == pygame.K_9:
                    val = 9
                if event.key == pygame.K_LEFT:
                    if xcord > 0:
                        xcord -= 1
                    
                if event.key == pygame.K_RIGHT:
                    if xcord < 8:
                        xcord += 1
                    
                if event.key == pygame.K_UP:
                    if ycord > 0:
                        ycord -= 1
                    
                if event.key == pygame.K_DOWN:
                    if ycord < 8:
                        ycord += 1

            if val != 0 :
                if val == answer_grid[ycord][xcord]:
                    draw_val()
                    solved +=1

            if solved == allblanks:
                run = False
            

                    
                
                    



##            elif val != 0 and [xcord,ycord] in active_square:
##                    text1 = font1.render(" ", 1, (0, 0, 0))
##                    screen.blit(text1, (xcord * 30 + 5, ycord * 30 + 5))
##                    #draw_val()
##                    active_square.remove([xcord,ycord])
##            else:
##                    text1 = font1.render(" ", 1, (0, 0, 0))
##                    screen.blit(text1, (xcord * 30 + 5, ycord * 30 + 5))
                
                    

                

                
        pygame.display.update()


def drawGrid(z):
    blockSize = z #Set the size of the grid block
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            if blockSize == 30:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen,black, rect, 1)
            else:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen,black, rect, 2)
                


def addNumber():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[j][i] != 0:

                text1 = font1.render(str(grid[j][i]), 1, (0, 0, 0))
                screen.blit(text1, (i * 30 + 5 , j * 30 + 5 ))
            else:
                text1 = font1.render(" ", 1, (0, 0, 0))
                screen.blit(text1, (i * 30 + 5 , j * 30 + 5 ))
                

def draw_val():
    global val
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (xcord * 30 + 5, ycord * 30 + 5))
    val = 0

main()           

