import pygame
from collections import Counter

gridDisplay = pygame.display.set_mode((600, 600))
pygame.display.get_surface().fill((200, 200, 200))  # background

#each digit represents 30 surface area pixels
board = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1],
]

def createSquare(x, y, width, height, color):
    pygame.draw.rect(gridDisplay, color, [x, y, width, height ])



def visualizeGrid():
    y = 0  # we start at the top of the screen
    for row in board:
        cntRow = Counter(row)
        
        wall_height = 10
        wall_step = 10
        if(cntRow[0] == 0):
            path_step = 600/cntRow[1]
        else:
            path_step = (600 - (cntRow[1]*10)) / cntRow[0]

        x = 0# for every row we start at the left of the screen again
        for item in row:
            if item == 0:
                createSquare(x, y, (600 - (cntRow[1]*10)) / cntRow[0],30,(255, 255, 255))
                x += path_step
            else:
                createSquare(x, y, 10,10,(0, 0, 0))
                x += wall_step

             # for ever item/number in that row we move one "step" to the right
        
        y += 10   # for every new row we move one "step" downwards
    pygame.display.update()


visualizeGrid()  # call the function    
while True:
    pass  # keeps the window open so you can see the result.