import sys
from turtle import Screen
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    clock = pygame.time.Clock()
    dt = 0 
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    
    Asteroid.containers = (updatable, drawable, asteroids)
 
    
    while True:
        log_state()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        #update everything    
        updatable.update(dt)  # Update all updatable sprites
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            
           
        # draw everything
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()  # Update the display
        
        
        dt = clock.tick(60) / 1000  

if __name__ == "__main__":
    main()
