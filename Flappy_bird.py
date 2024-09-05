import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GROUND_HEIGHT = 100
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_WIDTH = 50
PIPE_SPACING = 200
PIPE_SPEED = 3
PIPE_HEIGHT = random.randint(50, 300)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_image = pygame.image.load("bird.png")
bird_image = pygame.transform.scale(bird_image, (50, 50))
pipe_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_image.fill((0, 128, 0))

# Bird initialization
bird_x = 100
bird_y = HEIGHT // 2
bird_velocity = 0

# Pipes
pipes = []

# Score
score = 0

# Game Over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP_STRENGTH

    # Move the bird
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Check for collisions
    if bird_y <= 0:
        bird_y = 0
    elif bird_y >= HEIGHT - GROUND_HEIGHT:
        bird_y = HEIGHT - GROUND_HEIGHT
        game_over = True

    # Generate pipes
    if len(pipes) == 0 or WIDTH - pipes[-1][0] > PIPE_SPACING:
        pipe_height = random.randint(50, 300)
        pipes.append([0, pipe_height])

    # Move pipes
    for pipe in pipes:
        pipe[0] += PIPE_SPEED

    # Remove off-screen pipes
    if pipes[0][0] > WIDTH:
        pipes.pop(0)

    # Check for pipe collisions
    for pipe in pipes:
        if (
            bird_x + bird_image.get_width() > pipe[0]
            and bird_x < pipe[0] + PIPE_WIDTH
            and (bird_y < pipe[1] or bird_y + bird_image.get_height() > pipe[1] + PIPE_SPACING)
        ):
            game_over = True

    # Update the score
    if pipes[0][0] + PIPE_WIDTH < bird_x:
        score += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the bird
    screen.blit(bird_image, (bird_x, bird_y))

    # Draw the pipes
    for pipe in pipes:
        screen.blit(pipe_image, (pipe[0], 0))
        screen.blit(pipe_image, (pipe[0], pipe[1] + PIPE_SPACING))

    # Draw the ground
    pygame.draw.rect(screen, BLUE, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control game speed
    pygame.time.Clock().tick(30)

# Game over screen
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, (0, 0, 0))
screen.blit(game_over_text, (150, 250))
pygame.display.flip()

# Wait for a few seconds before closing the game
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
sys.exit()
