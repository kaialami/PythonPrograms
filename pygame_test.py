import sys
import pygame
import pygame.freetype
pygame.init()

winWidth = 700
winHeight = 700
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Man of Mint")
win.fill((18,40,70))
colour = (23,202,138)
font = pygame.font.Font("freesansbold.ttf", 20)
text = font.render('MAN OF MINT', True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (winWidth // 2, winHeight + 20)

x = 50
y = 500
width = 40
height = 60
vel = 10
boost = False
isJump = False
jumpCount = 10
run = True

platBegin = (winWidth // 2 + 20, winHeight // 2 + 20)
platEnd = (winWidth - 50, winHeight // 2 + 20)

def redraw():
    win.fill((18,40,70))
    pygame.draw.rect(win, (3,192,40), (0, 500 + height, winWidth, winHeight - 500 + height))
    pygame.draw.rect(win, colour, (x, y, width, height))
    win.blit(text, textRect)
    pygame.display.update()


while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            colour = (255,46,46)
            vel = 15
            boost = True
        if event.type == pygame.MOUSEBUTTONUP:
            colour = (23,202,138)
            vel = 10
            boost = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= vel
        if x <= 0:
            x = 0
    if keys[pygame.K_d]:
        x += vel
        if x >= winWidth - width:
            x = winWidth - width
    if not isJump:
        # if keys[pygame.K_w]:
        #     y -= vel
        #     if y <= 0:
        #         y = 0
        # if keys[pygame.K_s]:
        #     y += vel
        #     if y >= winHeight - height:
        #         y = winHeight - height
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= jumpCount ** 2 * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redraw()
    

pygame.quit()
