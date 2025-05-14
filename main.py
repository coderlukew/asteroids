import pygame
from constants import *
from player import Player

def main():
    # Initialize the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)
        screen.fill((0, 0, 0))  # Fill the screen with black
        player.draw(screen)  # Draw the player
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 FPS
        dt = clock.tick(60) / 1000.0

    pygame.quit()
    


if __name__ == "__main__":
    main()