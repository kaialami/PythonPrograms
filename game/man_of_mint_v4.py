import pygame, sys, random
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.colour = colour 
        self.velocity = 3
        self.vertical = 7
        self.jumpCount = 250
        self.isJump = False
        self.airborne = False
        self.isLeft = False

        # mint man 
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        # his top hat
        self.tophat = pygame.Surface((22, 35))
        self.tophat.fill(black)
        self.tophat_rect = self.tophat.get_rect(center = (self.x, self.y - 48))
        self.brim = pygame.Surface((self.width + 12, 6))
        self.brim.fill(black)
        self.brim_rect = self.brim.get_rect(topleft = (self.x - 26, self.y - self.height//2))
        # his fancy gun
        self.gun = pygame.Surface((34, 10))
        self.gun.fill(black)
        self.gun_rect_right = self.gun.get_rect(topleft = (self.x + 6, self.y - 4))
        self.gun_rect_left = self.gun.get_rect(topright = (self.x - 6, self.y - 4))
        self.gun_handle = pygame.Surface((8, 12))
        self.gun_handle.fill(black)
        self.gun_handle_rect_left = self.gun_handle.get_rect(topright = (self.x -6, self. y))
        self.gun_handle_rect_right = self.gun_handle.get_rect(topright = (self.x + 14, self. y))
    
    def move_x(self, right = 1):
        self.rect.x += self.velocity * right
        self.tophat_rect.x += self.velocity * right
        self.brim_rect.x += self.velocity * right
        self.gun_rect_left.x += self.velocity * right
        self.gun_rect_right.x += self.velocity * right
        self.gun_handle_rect_left.x += self.velocity * right
        self.gun_handle_rect_right.x += self.velocity * right
    
    def jump(self):
        self.rect.y -= self.vertical
        self.tophat_rect.y -= self.vertical
        self.brim_rect.y -= self.vertical
        self.gun_rect_left.y -= self.vertical
        self.gun_rect_right.y -= self.vertical
        self.gun_handle_rect_left.y -= self.vertical
        self.gun_handle_rect_right.y -= self.vertical
        self.jumpCount -= 5

    def fall(self):
        self.rect.y += self.vertical
        self.tophat_rect.y += self.vertical
        self.brim_rect.y += self.vertical
        self.gun_rect_left.y += self.vertical
        self.gun_rect_right.y += self.vertical
        self.gun_handle_rect_left.y += self.vertical
        self.gun_handle_rect_right.y += self.vertical

    def create_bullet(self):
        return Bullet(self.rect.x + 10, self.rect.y + 30, right)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, right=1):
        super().__init__()
        self.x = x
        self.y = y
        self.right = right
        self.gun_vel = 15
        self.image = pygame.Surface((20, 8))
        self.image.fill(white)
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def update(self):
        self.rect.x += self.gun_vel * self.right
        if self.rect.x >= screen_width + 200 or self.rect.x <= -200:
            self.kill()




# colours
black = (0,0,0)
white = (255,255,255)
mint = (23,202,138)
green = (3,192,40)
orange = (255,46,46)
darkblue = (18,40,70)
gray = (58,58,58)
colour = mint

# screen
screen_width = 650
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Man of Mint")
screen.fill(darkblue)

# variables
run = True
clock = pygame.time.Clock()
floor = 530
floor_surface = pygame.Surface((screen_width, floor))
floor_surface.fill(gray)
floor_rect = floor_surface.get_rect(topleft = (0, floor))
paused = False

def update():
    screen.fill(darkblue)
    screen.blit(floor_surface, floor_rect)
    bullet_group.draw(screen)
    player_group.draw(screen)
    screen.blit(man.tophat, man.tophat_rect)
    screen.blit(man.brim, man.brim_rect)
    if not man.isLeft:
        screen.blit(man.gun, man.gun_rect_right)
        screen.blit(man.gun_handle, man.gun_handle_rect_right)
    elif man.isLeft:
        screen.blit(man.gun, man.gun_rect_left)
        screen.blit(man.gun_handle, man.gun_handle_rect_left)
    pygame.display.flip()

man = Player(screen_width // 2, 500, 40, 60, mint)
player_group = pygame.sprite.Group()
player_group.add(man)
bullet_group = pygame.sprite.Group()

while run:
    if not man.isLeft:
        right = 1
    if man.isLeft:
        right = -1
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and not paused:
            if not man.airborne:
                if event.key == pygame.K_SPACE:
                    man.isJump = True
        if event.type == pygame.KEYUP and not paused:
            if event.key == pygame.K_SPACE:
                man.isJump = False
                man.airborne = True
                man.jumpCount = 250
        if event.type == pygame.MOUSEBUTTONDOWN and not paused:
            bullet_group.add(man.create_bullet())
        if event.type == pygame.KEYDOWN and paused:
            if event.key == pygame.K_SPACE:
                paused = False
                man.jumpCount = 250
                man.score = 0
                man.x = screen_width//2
                man.y = 500
            

    if not paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and man.rect.x + man.width < screen_width:
            man.isLeft = False
            right = 1
            man.move_x(right)
        if keys[pygame.K_a] and man.rect.x > 0:
            man.isLeft = True
            right = -1
            man.move_x(right)
        if keys[pygame.K_SPACE] and man.rect.y == floor - man.height:
            man.isJump = True
        
        # jump
        if man.isJump:
            man.jump()
            if man.jumpCount <= 0:
                man.isJump = False
                man.jumpCount = 250
        if not man.isJump and not man.rect.y == floor - man.height:
            man.fall()
        if man.rect.y + man.height >= floor:
            man.airborne = False
        
        

    bullet_group.update()
    update()

pygame.quit()