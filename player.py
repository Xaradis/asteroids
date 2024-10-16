import pygame
from circleshape import *
from constants import *
from bullet import *


class Player(CircleShape):
    def __init__(self, x, y):
#calling parent constructor        
        super().__init__(x, y, PLAYER_RADIUS)
#rotation field
        self.rotation = 0
#shoot CD
        self.PLAYER_SHOOT_COOLDOWN = 0
#method for rotation
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
#method for moving
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
#update?
    def update(self, dt):
#decrease timer per dt
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            self.PLAYER_SHOOT_COOLDOWN -= dt
#ensure timer doesn't go below 0
        if self.PLAYER_SHOOT_COOLDOWN < 0:
            self.PLAYER_SHOOT_COOLDOWN = 0
#Key press updates       
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.PLAYER_SHOOT_COOLDOWN == 0:  
            self.shoot(dt)
            self.PLAYER_SHOOT_COOLDOWN = 0.3
#triangle method
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
#overriding draw
    def draw(self, screen):
        color = (255, 255, 255)  #white color
        pygame.draw.polygon(screen, color, self.triangle(), 2) #draw
#creating shoot method    
    def shoot(self, SHOT_RADIUS):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

        
        


    