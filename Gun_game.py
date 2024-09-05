import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gun Game")

# Load images
bird_image = pygame.image.load("bird.png")
bird_image = pygame.transform.scale(bird_image, (50, 50))
gun_image = pygame.image.load("gun.png")
gun_image = pygame.transform.scale(gun_image, (50, 50))

# Bird initialization
bird_x = random.randint(50, WIDTH - 50)
bird_y = random.randint(50, HEIGHT - 50)

# Gun initialization
gun_x = WIDTH // 2
gun_y = HEIGHT - 50

# Score
score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click hit the bird
            if (
                bird_x < event.pos[0] < bird_x + bird_image.get_width()
                and bird_y < event.pos[1] < bird_y + bird_image.get_height()
            ):
                bird_x = random.randint(50, WIDTH - 50)
                bird_y = random.randint(50, HEIGHT - 50)
                score += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the bird
    screen.blit(bird_image, (bird_x, bird_y))

    # Draw the gun
    gun_x, _ = pygame.mouse.get_pos()
    screen.blit(gun_image, (gun_x, gun_y))

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
