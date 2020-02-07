import pygame
from Functions import  *
import collections
#class to for cell info
 

#creating the grid stae 
gridState =[[cell() for j  in range(33) ] for i in range(20)]
# Define some colors
BLACK = (26, 8, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (169, 169, 169)  
ALICE_BLUE = (240, 248, 255)


 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 15
HEIGHT = 15
 
# This sets the margin between each cell
MARGIN = 3
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
 # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid= []

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [600, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("PATH FINDER ")
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
# Loop until the user clicks the close button.
done = False
startSet  = False
endSet = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
intiGrid(grid,gridState, screen)

# -------- Main Program Loop -----------
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

                if(grid[row][column] == 0 and gridState[row][column].isWalled == False ): # making the walls toggable 
                    grid[row][column] = 1
                    gridState[row][column].isWalled = True
                    print("Click ", pos, "Grid coordinates: ", row, column)

                else:
                    grid[row][column] = 0
                    gridState[row][column].isWalled = False

            if (  20 <= row <= 23  and  13 <= column <= 18 ):
               ResetGrid(grid, gridState,screen)

            if (  20 <= row <= 23  and  0 <= column <= 5 ):
               Startbutton(event, grid,gridState)
            if (  20 <= row <= 23  and  6 <= column <= 12 ):
               Endbutton(event, grid,gridState)
            if (  24 <= row <= 26  and  0 <= column <= 5 ):
               start = ReturnStartState(gridState)
               path = BFS(grid,gridState, start, screen)

            if (  24 <= row <= 26  and  7 <= column <= 12 ):
               start = ReturnStartState(gridState)
               DFS(grid,gridState, start, screen)
               
               drawPath(grid, path)
               
                  
            print("Click ", pos, "Grid coordinates: ", row, column)
            


 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    
#add new color state while the grid changes 
    updateGrid(grid,screen)
    



            

 
    # Limit to 60 frames per second
    #button art
  
    









    StartButt = button( screen, 'Start', 5,370,100,50, GREEN, RED)
    EndButt = button( screen, 'End', 120 ,370 ,100,50, GREEN, RED)
   
    button( screen,'RESET', 235,370,100,50,GREEN,RED)
    QuitButt = button( screen, 'quit', 350 ,370 ,100,50, GREEN, RED,)

    BFSButt = button( screen, 'BFS', 5 ,430 ,100,50, GREEN, RED)
    DFSButt = button( screen, 'DFS', 120 ,430 ,100,50, GREEN, RED)
    unButt = button( screen, 'Un', 235 ,430 ,100,50, GREEN, RED)

   
   
   

    

    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()