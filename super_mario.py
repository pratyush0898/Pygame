import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario")

white = (255, 255, 255)

mario_image = pygame.image.load("mario.png")
mario_rect = mario_image.get_rect()

mario_x = 100
mario_y = 400
mario_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_x -= mario_speed
    if keys[pygame.K_RIGHT]:
        mario_x += mario_speed

    screen.fill(white)
    screen.blit(mario_image, (mario_x, mario_y))
    pygame.display.update()
