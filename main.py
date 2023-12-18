# Rectangle Collision Challenge 
import pygame 
import random

# Define colors 
Grey = [128, 128, 128] 
White = [255, 255, 255] 
Blue = [0, 0, 255] 

# Wall Class 
class Wall():
    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y
        self.w = w 
        self.h = h 
    def drawWall(self, screen):
        pygame.draw.rect(screen, Grey, [self.x, self.y, self.w, self.h]) 

# Player Class
class Player():
    def __init__(self, x, y, w, h): 
        self.x = x 
        self.y = y 
        self.w = w
        self.h = h
    def drawPlayer(self, screen):
        pygame.draw.rect(screen, Blue, [self.x, self.y, self.w, self.h]) 

# Collision Function 
def rectCollision(rect1, rect2): 
   if rect1.x < rect2.x + rect2.w and rect1.y < rect2.y + rect2.h and rect1.x + rect1.w > rect2.x and rect1.y + rect1.h > rect2.y:
       return -1



# List of walls
walls = [] 
walls.append(Wall(100, 20, 20, 430))
walls.append(Wall(100, 0, 500, 20)) 
walls.append(Wall(580, 20, 20, 430)) 
walls.append(Wall(100, 430, 500, 20))  
walls.append(Wall(200, 50, 100, 15)) 
walls.append(Wall(400, 250, 15, 100)) 
walls.append(Wall(300, 50, 100, 15)) 
walls.append(Wall(500, 75, 15, 100)) 
walls.append(Wall(150, 300, 100, 15))

# Player 
player = Player(150, 200, 20, 20)

# Main function 
def main():
    pygame.init() 
    # Canvas
    size = (700, 500)
    screen = pygame.display.set_mode(size) 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Main Program Loop 
    while not done:
        # Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
        # Check Key Pressed for Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x += -2 
        elif keys[pygame.K_RIGHT]:
            player.x += 2 
        elif keys[pygame.K_UP]:
            player.y += -2     
        elif keys[pygame.K_DOWN]:
            player.y += 2   

        # Collision   
        for i in range (len(walls)):
            if rectCollision(player, walls[i]) == -1:
                player.x = 150 
                player.y = 200

        screen.fill(White)
        for i in range(len(walls)):
            walls[i].drawWall(screen) 
        player.drawPlayer(screen)
 
        pygame.display.flip()
 
        # --- Limit frames
        clock.tick(60)

    # Close window
    pygame.quit()  

main()