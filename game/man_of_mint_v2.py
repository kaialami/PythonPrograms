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
text = font.render("'MAN OF MINT'", True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (winWidth // 2, winHeight + 20)

x = 50
y = 500
width = 40
height = 60
vel = 10
vertical = 45
floor = 500
boost = False
isJump = False
alreadyJump = False
jumpCount = 50
run = True

# colours
black = (0,0,0)
white = (255,255,255)
mint = (23,202,138)
green = (3,192,40)
orange = (255,46,46)
darkblue = (18,40,70)
colour = mint

platBegin = (winWidth // 2 + 20, winHeight // 2 + 20)
platEnd = (winWidth - 50, winHeight // 2 + 20)

def redraw():
    win.fill(darkblue)
    pygame.draw.rect(win, green, (0, 500 + height, winWidth, winHeight - 500 + height))
    pygame.draw.rect(win, colour, (x, y, width, height))
    win.blit(text, textRect)
    pygame.display.update()


while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            run = True
        if event.type == pygame.MOUSEBUTTONUP:
            run = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                colour = orange
                vel = 15
                boost = True
            if not alreadyJump:
                if event.key == pygame.K_SPACE:
                    isJump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                colour = mint
                vel = 10
                boost = False
            if event.key == pygame.K_SPACE:
                isJump = False
                alreadyJump = True

    if isJump:
        y -= vertical
        jumpCount -= 5
        if jumpCount <= 0:
            isJump = False
            jumpCount = 50
    if not isJump:
        y += vertical
    if y > floor:
        y = floor
        alreadyJump = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= vel
        if x <= 0:
            x = 0
    if keys[pygame.K_d]:
        x += vel
        if x >= winWidth - width:
            x = winWidth - width
    if keys[pygame.K_SPACE] and y == floor:
        isJump = True

    redraw()
    

pygame.quit()
