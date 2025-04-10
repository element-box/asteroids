import pygame

from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid 
from asteroidfield import AsteroidField

# TODO:
# Add a scoring system
# Implement multiple lives and respawning
# Add an explosion effect for the asteroids
# Add acceleration to the player movement
# Make the objects wrap around the screen instead of disappearing
# Add a background image
# Create different weapon types
# Make the asteroids lumpy instead of perfectly round
# Make the ship have a triangular hit box instead of a circular one
# Add a shield power-up
# Add a speed power-up
# Add bombs that can be dropped

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Shot.containers = (shots,updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("Black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        # Player collision
        for ast in asteroids:
            if ast.collision(player):
                print("Game Over!")
                return
            
        for ast in asteroids:
            for shot in shots:
                if ast.collision(shot):
                    ast.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000 # milliseconds to seconds




if __name__ == "__main__":
    main()