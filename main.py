import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *

def main():
#trying to initialize pygame
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
#pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#fps time object?
    Clock_instance = pygame.time.Clock()

    
#creating draw and upd sprite group for player(triangle)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
#player centering
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
#creating sprite group for asteroid
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
#asteroid field spawning
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
#bullets shot
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
#infinite while loop for game
    while True:
#for closing game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
    #update player inputs
        for obj in updatable:
            obj.update(dt)  
    #render player
        for obj in drawable:
            obj.draw(screen)
    #check for collisions
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                pygame.quit()
            for shot in shots:
                if shot.collisions(asteroid):
                    shot.kill()
                    asteroid.split()
                
        pygame.display.flip()
        dt = Clock_instance.tick(60) / 1000









if __name__ == "__main__":
    main()