import pygame
import random

# 1. Setup
pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
P_SIZE = 30
E_SIZE = 20
P_X, P_Y = W // 2 - P_SIZE // 2, H - 40

# 2. Game objects & state
player = pygame.Rect(P_X, P_Y, P_SIZE, P_SIZE)
enemies = [pygame.Rect(random.randint(0, W - E_SIZE), 20, E_SIZE, E_SIZE) for _ in range(5)]
bullets = []
score = 0
running = True

# 3. Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # Player movement
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    player.x = max(0, min(W - P_SIZE, player.x))

    # Shooting
    if keys[pygame.K_SPACE] and not bullets:
        bullets.append(pygame.Rect(player.centerx - 2, player.top, 4, 10))

    # Update enemies/bullets
    [b.move_ip(0, -7) for b in bullets]
    bullets = [b for b in bullets if b.bottom > 0]
    [e.move_ip(random.choice([-2, 2]), 1) for e in enemies]

    # Collision detection
    for b in bullets[:]:
        for e in enemies[:]:
            if b.colliderect(e):
                bullets.remove(b)
                enemies.remove(e)
                enemies.append(pygame.Rect(random.randint(0, W - E_SIZE), 20, E_SIZE, E_SIZE))
                score += 1
                break

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), player)
    [pygame.draw.rect(screen, (255, 0, 0), e) for e in enemies]
    [pygame.draw.rect(screen, (255, 255, 255), b) for b in bullets]
    pygame.display.flip()
    clock.tick(60)

# 4. Cleanup
pygame.quit()
