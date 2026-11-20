import pygame, random

pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
player = pygame.Rect(180, 450, 40, 40)
blocks = []
score = 0
running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player.x -= 6
    if keys[pygame.K_RIGHT]: player.x += 6
    player.clamp_ip(screen.get_rect())

    if random.random() < 0.03:
        blocks.append(pygame.Rect(random.randint(0, 360), -30, 30, 30))
    for b in blocks:
        b.y += 5
    blocks = [b for b in blocks if b.y < 500]

    if any(player.colliderect(b) for b in blocks):
        print("Game over! Score:", score)
        running = False
    score += 1

    screen.fill((20, 20, 30))
    pygame.draw.rect(screen, (80, 200, 120), player)
    for b in blocks:
        pygame.draw.rect(screen, (220, 80, 80), b)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
