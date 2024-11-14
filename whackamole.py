import pygame
import random

# Constants
GRID_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 16
SCREEN_WIDTH = GRID_WIDTH * GRID_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * GRID_SIZE


def main():
    try:
        pygame.init()

        # Load mole image
        mole_image = pygame.image.load("mole.png")

        # Set up the screen and other objects
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        # Initial mole position
        mole_x, mole_y = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole was clicked
                    if pygame.Rect(mole_x, mole_y, GRID_SIZE, GRID_SIZE).collidepoint(event.pos):
                        # Move the mole to a random new square
                        mole_x = random.randrange(0, GRID_WIDTH) * GRID_SIZE
                        mole_y = random.randrange(0, GRID_HEIGHT) * GRID_SIZE

            # Clear the screen
            screen.fill("light green")

            # Draw the grid
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))

            # Draw the mole
            screen.blit(mole_image, (mole_x, mole_y))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
