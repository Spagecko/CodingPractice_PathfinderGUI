class cell:
    row = 0 
    col = 0
    isWalled = False
    visted = False
    colorState = 0;
    isStartingPoint =  False
    isEndingPoint = False

    def __init__(self):
        row = 0 
        col = 0
        isWalled = False
        visted = False
        colorState = 0;
        isStartingPoint =  False
        isEndingPoint = False

import time
import collections
import pygame

def StartState(gridState):
     for row in range(20):
         for column in range(33):
             if(gridState[row][column].isStartingPoint  == True):
                 return True
     return False

def EndState(gridState):
     for row in range(20):
         for column in range(33):
             if(gridState[row][column].isEndingPoint  == True):
                 return True
       
     return False



def ResetStartState(gridState):
     for row in range(20):
         for column in range(33):
             if(gridState[row][column].isStartingPoint  == True):
                 gridState[row][column].isStartingPoint = False
     

def Inti2d(gridState):
     for row in range(20):
         for column in range(33):
              gridState[row][column].row = row
              gridState[row][column].col = column

def ReturnStartState(gridState):
     for row in range(20):
         for column in range(33):
             if(gridState[row][column].isStartingPoint  == True):
              
               return column, row
    
     return 0


                 
     



def ResetEndState(gridState):
     for row in range(20):
         for column in range(33):
             if(gridState[row][column].isEndingPoint  == True):
                 gridState[row][column].isEndingPoint  = False

def ResetWallState(gridState):
     for row in range(20):
         for column in range(33):
             if(gridState[row][column].isWalled  == True):
                 gridState[row][column].isWalled  = False


    






#intilizes the grid
def intiGrid(grid, gridState,screen):

   
    for row in range(20):
    # Add an empty array that will hold each cell
    # in this row
        grid.append([])
        for column in range(33):
            grid[row].append(0) 
    updateGrid(grid,screen)   
    gridState =[[cell() for j  in range(33) ] for i in range(20)]
    Inti2d(gridState) # sets the rows and cols 
#updates the graphic of the grid

def ResetGrid(grid, gridState,screen):

   
    for row in range(20):
    # Add an empty array that will hold each cell
    # in this row
       
        for column in range(33):
            grid[row][column] = 0

    ResetStartState(gridState)
    ResetEndState(gridState)
    ResetWallState(gridState)
   
    # sets the rows and cols 
#updates the graphic of the grid

    


def updateGrid(grid,screen):
    WIDTH = 15
    HEIGHT = 15
    MARGIN = 3
    GREY = (169, 169, 169)
    PURPLE = (160, 13, 173)
    YELLOWGREEN = (153,186,0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    for row in range(20):
        for column in range(33):
            WHITE = (255, 255, 255)
            color = WHITE
            if grid[row][column] == 1:
                color = GREY
            if grid[row][column] == 2:
                color = PURPLE
            if grid[row][column] == 3:
                color = YELLOWGREEN
            if grid[row][column] == 4:
                color = GREEN
            if grid[row][column] == 5:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])


#basic button template


def button(gameDisplay,msg,x,y,w,h,ic,ac,):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
  #  if click[0] == 1 and action != None:
  #          action()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface  = myfont.render(msg, False ,( 0,0,0))
    gameDisplay.blit(textsurface,(x,y))
# buttons that will trigger a action

#each button will require different parameters 

#this function will prompt the user to choose Start which will be colored  orange 
def Startbutton (event,grid, gamestate ):
    WIDTH = 15
    HEIGHT = 15
    MARGIN = 3
    print("Choose a starting pos")
    done =  False
    if( StartState(gamestate) == False):
        while not done:
         for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
            
                if ( column < 33 and row < 20): # cheecks if the click is within the constrints of the grid 

                    if(grid[row][column] == 0 and gamestate[row][column].isWalled == False ): # making the walls toggable 
                        grid[row][column] = 2
                        gamestate[row][column].isStartingPoint = True
                        
                        
                        done = True
                    

                    else:
                        print("invalid start")
                    
                        done = True
    else:
        print("can't set starting point")

         
  
 #this function will prompt the user to choose Start which will be colored  Purple 
def Endbutton (event,grid, gamestate ):
    WIDTH = 15
    HEIGHT = 15
    MARGIN = 3
    print("Choose a ending pos")
    done =  False
    if( EndState(gamestate) == False):
        while not done:
         for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
            
                if ( column < 33 and row < 20): # cheecks if the click is within the constrints of the grid 

                    if(grid[row][column] == 0 and gamestate[row][column].isWalled == False ): # making the walls toggable 
                        grid[row][column] = 3
                        gamestate[row][column].isEndingPoint = True
                        
                        
                        done = True
                    

                    else:
                        print("invalid Ending")
                    
                        done = True
    else:
        print("can't set Ending point")
  
 #this function will reset the state of the gameboard to all 0s  
def Resetbutton( grid, gamestate,screen):
    intiGrid(grid,gamestate,screen)



def BFSbutton(gameDisplay,msg,x,y,w,h,ic):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and action != None:
            action()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface  = myfont.render(msg, False ,( 0,0,0))
    gameDisplay.blit(textsurface,(x,y))

def DFSbutton(gameDisplay,msg,x,y,w,h,ic):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and action != None:
            action()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface  = myfont.render(msg, False ,( 0,0,0))
    gameDisplay.blit(textsurface,(x,y))

def BFS(grid,gridState, start, screen):
    queue = collections.deque([[start]])
    seen = set([start])
   
    while queue:
       
        path = queue.popleft()
        
        
        x, y = path[-1]
       
        #gridState[y][x].visted  == True
      #  updateGrid(grid,screen)
       # time.sleep(.300)
        if gridState[y][x].isEndingPoint == True :
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < 33 and 0 <= y2 < 20 and (x2, y2) not in seen and gridState[y][x].isWalled == False :
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
                if(grid[y][x] !=1 ):
                    grid[y][x] = 4
                   # gridState[y][x].visted  == True

def DFS(grid,gridState, start, screen):
    stack = deque()
    stack.append(start)

    while stack:

        x , y = stack.pop()
        if (gridState[y][x].isEndingPoint == True):
            print("yes")

        if(gridState[y][x].visted  != True):
            gridState[y][x].visted  = True
                
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    if 0 <= x2 < 33 and 0 <= y2 < 20 and (x2, y2) not in seen and gridState[y][x].isWalled == False :
                        stack.append([x,y])



    

    
    
   



                

def drawPath(grid, path):

      while len(path) !=0:
        x,y =  path.pop()
        grid[y][x] = 5 #change the grid state to 5 
        print(x,y)
       