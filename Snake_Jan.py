# Mohammad Jan
# Tuesday Nov. 24 2020
# V.1
# Basic classic Snake game using pygame

##### IMPORTS

import pygame
import random
import sys

##### GLOBAL VERIABLES

Screen_Width = 480
Screen_Height = 480

Gridsize = 20
Grid_Width = Screen_Height / Gridsize
Grid_Height = Screen_Width / Gridsize

Up = (0,-1)
Down = (0,1)

Left = (-1,0)
Right = (1,0)

##### CLASSES

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((Screen_Width/2),(Screen_Height/2))]
        self. direction = random.choice([Up, Down, Left, Right])
        self.color = (17, 24, 47)
    
    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
    
    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0] + (x*Gridsize))% Screen_Width), (cur[1] + (y*Gridsize))% Screen_Height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        self.length = 1
        self.positions = [((Screen_Width /2),(Screen_Height/2))]
        self.direction = random.choice([Up, Down, Left, Right])
        
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0],p[1]), (Gridsize, Gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)
    
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(Up)
                elif event.key == pygame.K_DOWN:
                    self.turn(Down)
                elif event.key == pygame.K_LEFT:
                    self.turn(Left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(Right)   

class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, Grid_Width -1) * Gridsize, random.randint(0, Grid_Height-1) * Gridsize)
    
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (Gridsize, Gridsize))
        pygame.draw.rect(surface, self.color,r)
        pygame.draw.rect(surface, (93,216,228), r ,1) 
    
##### CLASS INIT

snake = Snake()
food = Food()

##### FUNCTIONS

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Screen_Width, Screen_Height), 0,32)
    
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)
    

    
    myfont = pygame.font.SysFont('monospace', 16)
    
    score = 0
    
    while True:
        clock.tick(15) #frames per second
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render('Score{0}'.format(score), 1, (0 ,0, 0))
        screen.blit(text, (5,10))
        
        pygame.display.update()

def draw_grid(surface):
    for y in range(0, int(Grid_Height)):
        for x in range(0, int(Grid_Width)):
            if (x+y) %2 == 0:
                r = pygame.Rect((x*Gridsize, y*Gridsize), (Gridsize, Gridsize))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                r = pygame.Rect((x*Gridsize, y*Gridsize), (Gridsize, Gridsize))
                pygame.draw.rect(surface, (84,194, 205), r)
                
##### MAIN CODE

main()