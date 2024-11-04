import pygame
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pong")
doExit = False
clock = pygame.time.Clock()
p1x = 20; p1y = 200 #player 1
p2x = 660; p2y = 200 #player 2
bx = 350; by = 250 #ball position
bVx = 15; bVy = 15 #ball velocity
WHITE = (255,255,255)
p2score = 0; p1score = 0 #score

while not doExit: #event queue stuff
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    # Game logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: p1y -= 10
    if keys[pygame.K_s]: p1y += 10
    if keys[pygame.K_p]: p2y -= 10
    if keys[pygame.K_l]: p2y += 10
    
    bx += bVx
    by += bVy
    if bx < 0 or bx > 700:
        bVx *= -1
    if bx < 0:
        p2score += 1
    if bx > 700:
        p1score += 1
    if by < 0 or by + 20 > 500:
        bVy *= -1
    if bx < p1x +30 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
    if bx > p2x - 5 and by + 20 > p2y and by < p2y + 100:
        bVx *= -1
    # Render section
    screen.fill((0,0,0))
    
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1score), 1,(WHITE))
    screen.blit(text, (250,50))
    text = font.render(str(p2score), 1,(WHITE))
    screen.blit(text, (420,50))
    

    pygame.draw.line(screen,(WHITE), [349, 0], [349, 500], 5)
    pygame.draw.rect(screen,(WHITE), (p1x, p1y, 20, 100), 2)
    pygame.draw.rect(screen,(WHITE), (p2x, p2y, 20, 100), 2)
    pygame.draw.circle(screen,(WHITE), (bx, by), 5)
    pygame.display.flip()
pygame.quit() #when game is done close down pygame
