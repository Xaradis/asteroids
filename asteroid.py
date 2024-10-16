import pygame
import random
from circleshape import *
from constants import *

#asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
#draw
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
#update   
    def update(self, dt):
        self.position += self.velocity * dt
#split
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
#creating splits
            split_one = self.velocity.rotate(random_angle)
            split_two = self.velocity.rotate(-random_angle)
#new radius after split
            new_radius = self.radius - ASTEROID_MIN_RADIUS
#new asteroids
#1
            Ast_one = Asteroid(self.position.x, self.position.y, new_radius)
            Ast_one.velocity = split_one * 1.2
#2
            Ast_two = Asteroid(self.position.x, self.position.y, new_radius)
            Ast_two.velocity = split_two * 1.2
            



