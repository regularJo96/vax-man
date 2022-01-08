#Pacman in Python with PyGame
#https://github.com/hbokmann/Pacman
  
import pygame
import time
import random

exited = {"pinky":False,"inky":False,"clyde":False,"blinky":True}
inside = []

# coordinate pairs of intersections in the map


intersections = [
    [17, 19, ["down","right"]  ],
    [17, 79, ["up","down","right"]  ],
    [17, 259, ["up","right"]  ],
    [17, 319, ["down","right"]  ],
    [17, 559, ["up","right"]  ],
    [77, 139, ["down","right"]  ],
    [77, 259, ["up","down","left"]  ],
    [77, 319, ["up","left","right"]  ],
    [77, 379, ["down","right"]  ],
    [77, 499, ["up","down","right"]  ],
    [77, 559, ["up","left","right"]  ],
    [137, 79, ["left","right","down"]  ],
    [137, 139, ["up","left","right"] ],
    [137, 199, ["down","right"] ],
    [137, 319, ["up","left","down"] ],
    [137, 379, ["up","left","right"] ],
    [137, 439, ["down","right"] ],
    [137, 499, ["up","left","right"] ],
    [197, 199, ["left","right","down"] ],
    [197, 319, ["up","right"] ],
    [257, 19, ["down","left"]  ],
    [257, 79, ["up","left","right"]  ],
    [257, 139, ["down","left"] ],
    [257, 199, ["up","left","right"] ],
    [257, 499, ["down","left"] ],
    [257, 559, ["up","left","right"] ],
    [317, 19, ["down","right"]  ],
    [317, 79, ["up","left","right"]  ],
    [317, 139, ["down","right"] ],
    [317, 199, ["up","left","right"] ],
    [317, 499, ["down","right"] ],
    [317, 559, ["up","left","right"] ],
    [377, 199, ["left","right","down"] ],
    [377, 319, ["up","left"] ],
    [437, 79, ["left","right","down"]  ],
    [437, 139, ["up","left","right"] ],
    [437, 199, ["down","left"] ],
    [437, 319, ["up","down","right"] ],
    [437, 379, ["up","left","right"] ],
    [437, 439, ["down","left"] ],
    [437, 499, ["up","left","right"] ],
    [497, 139, ["down","left"] ],
    [497, 259, ["up","down","right"] ],
    [497, 319, ["up","left","right"] ],
    [497, 379, ["down","left"] ],
    [497, 499, ["up","down","left"] ],
    [497, 559, ["up","left","right"] ],
    [557, 19, ["down","left"]  ],
    [557, 79, ["up","down","left"]  ],
    [557, 259, ["up","left"] ],
    [557, 319, ["down","left"] ],
    [557, 559, ["up","left"] ]
]

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
purple = (255,0,255)
yellow   = (255,255,0)

Trollicon=pygame.image.load('images/pacman_avi_right.png')
pygame.display.set_icon(Trollicon)

#Add music
pygame.mixer.init()
pygame.mixer.music.load('loop.mp3')
pygame.mixer.music.play(-1, 0.0)

# This class represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y,width,height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
  
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

# This creates all the walls in room 1
def setupRoomOne(all_sprites_list):
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list=pygame.sprite.RenderPlain()
     
    # This is a list of walls. Each is in the form [x, y, width, height]
    walls = [ [0,0,6,600],
              [0,0,600,6],
              [0,600,606,6],
              [600,0,6,606],
              [300,0,6,66],
              [60,60,186,6],
              [360,60,186,6],
              [60,120,66,6],
              [60,120,6,126],
              [180,120,246,6],
              [300,120,6,66],
              [480,120,66,6],
              [540,120,6,126],
              [120,180,126,6],
              [120,180,6,126],
              [360,180,126,6],
              [480,180,6,126],
              [180,240,6,126],
              [180,360,246,6],
              [420,240,6,126],
              [240,240,42,6],
              [324,240,42,6],
              [240,240,6,66],
              [240,300,126,6],
              [360,240,6,66],
              [0,300,66,6],
              [540,300,66,6],
              [60,360,66,6],
              [60,360,6,186],
              [480,360,66,6],
              [540,360,6,186],
              [120,420,366,6],
              [120,420,6,66],
              [480,420,6,66],
              [180,480,246,6],
              [300,480,6,66],
              [120,540,126,6],
              [360,540,126,6]
            ]
     
    # Loop through the list. Create the wall, add it to the list
    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)
         
    # return our new list
    return wall_list

def setupGate(all_sprites_list):
      gate = pygame.sprite.RenderPlain()
      gate.add(Wall(282,242,42,2,white))
      all_sprites_list.add(gate)
      return gate

# This class represents the ball        
# It derives from the "Sprite" class in Pygame
class Block(pygame.sprite.Sprite):
     
    # Constructor. Pass in the color of the block, 
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image,color,[0,0,width,height])
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect = self.image.get_rect() 

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):

    # Set speed vector
    change_x=0
    change_y=0

    identity = None
    filename = None

    # Constructor function
    def __init__(self,x,y, filename, identity):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
   
        # Set height, width
        self.setImage(filename)
        self.filename = filename
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y

        self.identity = identity

    def setImage(self, filename):
        self.image = pygame.image.load(filename).convert()

    # Clear the speed of the player
    def prevdirection(self):
        self.prev_x = self.change_x
        self.prev_y = self.change_y

    # Change the speed of the player
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y
          
    # Find a new position for the player
    def update(self,walls,gate):
        # Get the old position, in case we need to go back to it
        
        old_x=self.rect.left
        new_x=old_x+self.change_x
        prev_x=old_x+self.prev_x
        self.rect.left = new_x
        
        old_y=self.rect.top
        new_y=old_y+self.change_y
        prev_y=old_y+self.prev_y

        # Did this update cause us to hit a wall?
        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.left=old_x
        else:
            self.rect.top = new_y

            # Did this update cause us to hit a wall?
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                # Whoops, hit a wall. Go back to the old position
                self.rect.top=old_y

        if gate != False:
          gate_hit = pygame.sprite.spritecollide(self, gate, False)
          if gate_hit:
            self.rect.left=old_x
            self.rect.top=old_y

#Inheritime Player klassist
class Ghost(Player):
    direction = None

    def changeDirection(self, directions):
        prevDirection = self.direction
        self.direction = directions[random.randint(0,len(directions)-1)]

    def move(self):
        if(self.direction == "left"):
            self.rect.move_ip(-15,0)
        elif(self.direction == "down"):
            self.rect.move_ip(0,15)
        elif(self.direction == "up"):
            self.rect.move_ip(0,-15)
        elif(self.direction == "right"):
            self.rect.move_ip(15,0)
    
    def atIntersection(self):
        for intersection in intersections:
            if(self.rect.x == intersection[0] and self.rect.y == intersection[1]):
                self.changeDirection(intersection[2])
                return True
        return False
    def getW(self):
        return self.rect.left
    def getH(self):
        return self.rect.top
    def getImage(self):
        return self.filename


# Call this function so the Pygame library can initialize itself
pygame.init()
  
# Create an 606x606 sized screen
screen = pygame.display.set_mode([606, 606])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'RenderPlain.'


# Set the title of the window
pygame.display.set_caption('Pacman')

# Create a surface we can draw on
background = pygame.Surface(screen.get_size())

# Used for converting color maps and such
background = background.convert()
  
# Fill the screen with a black background
background.fill(black)



clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 24)

#default locations for Pacman and monstas
w = 303-16 #Width
p_h = (7*60)+19 #Pacman height
m_h = (4*60)+19 #Monster height
b_h = (3*60)+19 #Binky height
i_w = 303-16-32 #Inky width
c_w = 303+(32-16) #Clyde width

def startGame():
    time_elapsed = 0
    seconds = int(time.time())
    all_sprites_list = pygame.sprite.RenderPlain()

    block_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoomOne(all_sprites_list)

    gate = setupGate(all_sprites_list)

    p_turn = 0
    p_steps = 0

    b_turn = 0
    b_steps = 0

    i_turn = 0
    i_steps = 0

    c_turn = 0
    c_steps = 0


    # Create the player paddle object
    Pacman = Player( w, p_h, "images/pacman_avi_right.png", identity="pacman")
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)
    
    Blinky=Ghost( w, b_h, "images/Blinky.png", identity="blinky")
    Blinky.direction = "right"
    monsta_list.add(Blinky)
    all_sprites_list.add(Blinky)

    Pinky=Ghost( w, m_h, "images/Pinky.png", identity="pinky")
    monsta_list.add(Pinky)
    inside.append(Pinky)
    all_sprites_list.add(Pinky)
    
    Inky=Ghost( i_w, m_h, "images/Inky.png", identity="inky")
    monsta_list.add(Inky)
    inside.append(Inky)
    all_sprites_list.add(Inky)
    
    Clyde=Ghost( c_w, m_h, "images/Clyde.png", identity="clyde")
    monsta_list.add(Clyde)
    inside.append(Clyde)
    all_sprites_list.add(Clyde)

    # Draw the grid
    for row in range(19):
        for column in range(19):
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                block = Block(yellow, 4, 4)

                # Set a random location for the block
                block.rect.x = (30*column+6)+26
                block.rect.y = (30*row+6)+26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                if b_collide:
                    continue
                elif p_collide:
                    continue
                else:
                    # Add the block to the list of objects
                    block_list.add(block)
                    all_sprites_list.add(block)

    bll = len(block_list)

    score = 0

    done = False

    i = 0

    while done == False: 
        #keep track of the time elapsed
        if(int(time.time()) > seconds):
            seconds = time.time()
            time_elapsed = time_elapsed + 1
            if(time_elapsed%5 == 0 and time_elapsed != 0):
                if(len(inside)>0):
                    monsta = inside.pop()
                    if(monsta.identity == "clyde"):
                        monsta.rect.x -= 32
                        monsta.rect.y -= 60
                        monsta.direction = "right"
                        exited["clyde"] = True
                    if(monsta.identity == "inky"):
                        monsta.rect.x += 32
                        monsta.rect.y -= 60
                        monsta.direction = "left"
                        exited["inky"] = True
                    if(monsta.identity == "pinky"):
                        monsta.rect.y -= 60
                        monsta.direction = "left"
                        exited["pinky"] = True

            if(time_elapsed%30 == 0 and time_elapsed != 0):
                duplicate_virus(monsta_list,all_sprites_list)

        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Pacman.setImage("images/pacman_avi_left.png")
                    Pacman.changespeed(-30,0)
                if event.key == pygame.K_RIGHT:
                    Pacman.setImage("images/pacman_avi_right.png")
                    Pacman.changespeed(30,0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0,-30)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0,30)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(30,0)
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(-30,0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0,30)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0,-30)
            
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
    
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        

        Pacman.update(wall_list,gate)

        for ghost in monsta_list:
            
            # the if check is inside3 the atIntersection function, 
            # if the ghost is at an intersection, it chooses a random 
            # direction to go
            ghost.atIntersection()
            ghost.move()

            # returned = ghost.changespeed(one,False,0,0,len(one)-1)
            # p_turn = returned[0]
            # p_steps = returned[1]
            # Pinky.changespeed(one,False,p_turn,p_steps,len(one)-1)
            # Pinky.update(wall_list,False)


        # See if the Pacman block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)
        
        # Check the list of collisions.
        if len(blocks_hit_list) > 0:
            score +=len(blocks_hit_list)
        
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
    
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.fill(black)
            
        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)

        score_text=font.render("Score: "+str(score)+"/"+str(bll), True, red)
        screen.blit(score_text, [10, 10])

        time_text=font.render("Time Elapsed: "+str(time_elapsed), True, red)
        screen.blit(time_text, [200, 10])

        time_text=font.render("virus load: "+str(len(monsta_list)), True, red)
        screen.blit(time_text, [422, 10])

        #removes the sprite that collided with the player; vaccinates the ghost
        monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, True)

        if score == 209:
            doNext("Congratulations, you won!",145,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate)
        
        if len(monsta_list) >= 128:
            doNext("Game Over",235,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
        
        pygame.display.flip()
        
        clock.tick(10)

def doNext(message,left,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate):
  while True:
      # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
          if event.key == pygame.K_RETURN:
            del all_sprites_list
            del block_list
            del monsta_list
            del pacman_collide
            del wall_list
            del gate
            startGame()

      #Grey background
      w = pygame.Surface((400,200))  # the size of your rect
      w.set_alpha(10)                # alpha level
      w.fill((128,128,128))           # this fills the entire surface
      screen.blit(w, (100,200))    # (0,0) are the top-left coordinates

      #Won or lost
      text1=font.render(message, True, white)
      screen.blit(text1, [left, 233])

      text2=font.render("To play again, press ENTER.", True, white)
      screen.blit(text2, [135, 303])
      text3=font.render("To quit, press ESCAPE.", True, white)
      screen.blit(text3, [165, 333])

      pygame.display.flip()

      clock.tick(10)

def duplicate_virus(monsta_list,all_sprites_list):
    add_monstas = []
    for monsta in monsta_list:
        if(exited[monsta.identity]):
            ghost = Ghost(monsta.getW(), monsta.getH(), monsta.getImage(), monsta.identity)
            ghost.direction = monsta.direction
            add_monstas.append(ghost)
    for monsta in add_monstas:
        directions = ["left","right","up","down"]
        monsta_list.add(monsta)
        all_sprites_list.add(monsta)

startGame()

pygame.quit()
