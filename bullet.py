import pygame
from circleshape import *
from constants import *
#asteroid class
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
#draw
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2) #draw
    
    def update(self, dt):
        self.position += self.velocity * dt