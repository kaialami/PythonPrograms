import sys
import pygame
import pygame.freetype
pygame.init()

# colours
black = (0,0,0)
white = (255,255,255)
mint = (23,202,138)
green = (3,192,40)
orange = (255,46,46)
darkblue = (18,40,70)
colour = mint


winWidth = 700
winHeight = 700
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Man of Mint")
win.fill((18,40,70))
colour = mint

x = 50
y = 500
width = 40
height = 60
vel = 10
vertical = 30
floor = 500
left = False
boost = False
isJump = False
alreadyJump = False
jumpCount = 50
run = True
bulletX = x
bulletY = y + 10
bulletShoot = bulletX
projectileClock = 0
shoot = False
inMotion = False
bulletVel = 30
bulletCount = 0


platBegin = (winWidth // 2 + 20, winHeight // 2 + 20)
platEnd = (winWidth - 50, winHeight // 2 + 20)

def redraw():
    win.fill(darkblue)
    # ground
    pygame.draw.rect(win, green, (0, 500 + height, winWidth, winHeight - 500 + height)) 
    # bullet
    if shoot:
        pygame.draw.rect(win, white, (bulletShoot, bulletY + 15, 10, 10))
    if not shoot:
        pygame.draw.rect(win, white, (bulletX, y + 10, 10, 10))
    # mint man
    pygame.draw.rect(win, colour, (x, y, width, height))
    # top hat
    pygame.draw.rect(win, black, (x + 10, y - 30, 20, 30))
    pygame.draw.rect(win, black, (x - 5, y, width + 8 , 7))
    # gun
    if left:
        pygame.draw.rect(win, black, (x - 12, y + 15, 25, 10))
    else:
        pygame.draw.rect(win, black, (x + width - 9, y + 15, 25, 10))
    
    pygame.display.update()


while run:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            run = True
        if event.type == pygame.MOUSEBUTTONUP:
            run = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                colour = orange
                vel = 15
                boost = True
            if not alreadyJump:
                if event.key == pygame.K_z:
                    isJump = True
            if event.key == pygame.K_x and not inMotion:    
                shoot = True
                if left:
                    neg = -1
                else:
                    neg = 1
                bulletStart = bulletX
                bulletShoot = bulletX
                bulletY = y
                inMotion = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                colour = mint
                vel = 10
                boost = False
            if event.key == pygame.K_z:
                isJump = False
                alreadyJump = True
                jumpCount = 45
            if event.key == pygame.K_x:
                projectileClock = 0
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left = True
        x -= vel
        if x <= 0:
            x = 0
    if keys[pygame.K_RIGHT]:
        left = False
        x += vel
        if x >= winWidth - width:
            x = winWidth - width
    if keys[pygame.K_z] and y == floor:
        isJump = True
    if keys[pygame.K_x] and not inMotion:
        shoot = True
        if left:
            neg = -1
        else:
            neg = 1
        bulletShoot = bulletX
        bulletY = y
        inMotion = True

    
    # jump
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

    bulletX = x + 10

    if shoot and inMotion:
        bulletShoot += bulletVel * neg
        if bulletShoot < 0 or bulletShoot > winWidth + 10:
            inMotion = False
            shoot = False
        bulletCount += 1
    

    # shoot
    # if shoot:
    #     bulletShoot = bulletX
    #     if left:
    #         neg = -1
    #         bulletShoot += bulletVel * neg
    #     else:
    #         neg = 1
    #         bulletX += bulletVel * neg
    #     projectileClock += 1
        
    redraw()


pygame.quit()
