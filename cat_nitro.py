import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat-Nitro")

# Clock
clock = pygame.time.Clock()

# Cat setup
cat = pygame.Rect(WIDTH // 2, HEIGHT - 100, 50, 50)
cat_speed = 5

# Nitro Boost
nitro_active = False
nitro_timer = 0

# Obstacles
obstacles = [pygame.Rect(random.randint(0, WIDTH - 50), -50, 50, 50) for _ in range(5)]
obstacle_speed = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and cat.left > 0:
        cat.x -= cat_speed
    if keys[pygame.K_RIGHT] and cat.right < WIDTH:
        cat.x += cat_speed
    if keys[pygame.K_SPACE]:  # Activate Nitro
        nitro_active = True
        nitro_timer = pygame.time.get_ticks()

    # Nitro mechanics
    if nitro_active:
        cat_speed = 10
        if pygame.time.get_ticks() - nitro_timer > 2000:  # 2 seconds boost
            nitro_active = False
            cat_speed = 5

    # Move obstacles
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacle.y = -50
            obstacle.x = random.randint(0, WIDTH - 50)

    # Collision detection
    for obstacle in obstacles:
        if cat.colliderect(obstacle):
            print("Game Over!")
            running = False

    # Drawing everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, cat)  # Cat
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)  # Obstacles

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
