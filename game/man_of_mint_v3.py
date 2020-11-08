import pygame, sys, random
pygame.init()

# colours
black = (0,0,0)
white = (255,255,255)
mint = (23,202,138)
green = (3,192,40)
orange = (255,46,46)
darkblue = (18,40,70)
gray = (58,58,58)
colour = mint

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
SPAWNENEMY = pygame.USEREVENT
pygame.time.set_timer(SPAWNENEMY, 1300)
enemylist = []
enemylist_rects = []
enemy_x = [50, 150, 200, 600, 500, 450]
enemy_y = [500, 300, 200, 350]
game_font = pygame.font.SysFont('bahnschrift', 30)
paused = False


def update_display():
    screen.fill(darkblue)
    screen.blit(floor_surface, floor_rect)
    screen.blit(man.bullet, man.bullet.get_rect(center = (man.bulletShoot, man.bulletY + 1)))
    screen.blit(man.image, man.image_rect)
    screen.blit(man.tophat, man.tophat_rect)
    screen.blit(man.brim, man.brim_rect)
    if not man.isLeft:
        screen.blit(man.gun, man.gun_rect_right)
        screen.blit(man.gun_handle, man.gun_handle_rect_right)
    elif man.isLeft:
        screen.blit(man.gun, man.gun_rect_left)
        screen.blit(man.gun_handle, man.gun_handle_rect_left)
    if len(enemylist) > 0:
        screen.blit(enemylist[-1].image, enemylist_rects[-1])
    screen.blit(score_display()[0], score_display()[1])
    if paused:
        screen.blit(game_over()[0], game_over()[1])
        screen.blit(game_over()[2], game_over()[3])
    # screen.blit(enemy1.image, enemy1.image_rect)

    pygame.display.update()

def player_collision(player, enemy):
    return player.colliderect(enemy)

def bullet_hit(bullet, enemy):
    return bullet.colliderect(enemy)
    
def create_enemy():
    new_enemy = Enemy(random.choice(enemy_x), random.choice(enemy_y), 40, 60, orange)
    enemylist.append(new_enemy)
    new_enemy_rect = new_enemy.image.get_rect(center = (new_enemy.x, new_enemy.y))
    return new_enemy_rect

def score_display():
    score_surface = game_font.render(f'Score: {man.score}', True, white)
    score_rect = score_surface.get_rect(center = (screen_width // 2, 50))
    return score_surface, score_rect

def game_over():
    game_over_surface = game_font.render('GAME OVER', True, white)
    game_over_rect = game_over_surface.get_rect(center = (screen_width//2, screen_height//2 - 40))
    restart = game_font.render('Press SPACE to restart', True, white)
    restart_rect = restart.get_rect(center = (screen_width//2, screen_height//2 + 10))
    return game_over_surface, game_over_rect, restart, restart_rect

class Player():
    def __init__(self, x, y, width, height, colour):
        # mint man's variables
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
        self.gun_vel = 15
        self.isShoot = False
        self.bulletTimer = 600
        self.bulletStart = self.x
        self.bulletY = self.y
        self.bulletShoot = self.bulletStart
        self.inMotion = False
        self.timeElapsed = 0
        self.score = 0

        # mint man himself
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.colour)
        # his top hat
        self.tophat = pygame.Surface((22, 35))
        self.tophat.fill(black)
        self.brim = pygame.Surface((self.width + 12, 6))
        self.brim.fill(black)
        # his fancy gun
        self.gun = pygame.Surface((34, 10))
        self.gun.fill(black)
        self.gun_handle = pygame.Surface((8, 12))
        self.gun_handle.fill(black)
        # bullet
        self.bullet = pygame.Surface((10, 10))
        self.bullet.fill(white)

    def update_rects(self):
        self.image_rect = self.image.get_rect(center = (self.x, self.y))
        self.tophat_rect = self.tophat.get_rect(center = (self.x, self.y - 48))
        self.brim_rect = self.brim.get_rect(topleft = (self.x - 26, self.y - self.height//2))
        self.gun_rect_right = self.gun.get_rect(topleft = (self.x + 6, self.y - 4))
        self.gun_rect_left = self.gun.get_rect(topright = (self.x - 6, self.y - 4))
        self.gun_handle_rect_left = self.gun_handle.get_rect(topright = (self.x -6, self. y))
        self.gun_handle_rect_right = self.gun_handle.get_rect(topright = (self.x + 14, self. y))
        # self.bullet_rect = self.bullet.get_rect(center = (self.bulletStart, self.y))

    def move_x(self, right = 1):
        self.x += self.velocity * right
    
    def jump(self):
        self.y -= self.vertical
        self.jumpCount -= 5

    def fall(self):
        self.y += self.vertical

    def shoot(self, right):
        self.bulletShoot += man.gun_vel * right
    
class Enemy():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(colour)
    
    def destroy_rect(self):
        self.image = pygame.Surface((0, 0))

    def update_rects(self):
        self.image_rect = self.image.get_rect(center = (self.x, self.y))
    

man = Player(screen_width // 2, 500, 40, 60, mint)
enemy1 = Enemy(500, 500, 40, 60, orange)
enemylist.append(enemy1)
enemylist_rects.append(enemy1.image.get_rect(center = (enemy1.x, enemy1.y)))
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
        if event.type == pygame.MOUSEBUTTONDOWN and not man.isShoot and not paused:
            if man.isLeft:
                neg = -1
            if not man.isLeft:
                neg = 1
            man.isShoot = True
            man.inMotion = True
            man.bulletShoot = man.x
            man.bulletY = man.y
        if event.type == SPAWNENEMY and not paused:
            enemylist_rects.append(create_enemy())
        
        if event.type == pygame.KEYDOWN and paused:
            if event.key == pygame.K_SPACE:
                paused = False
                man.jumpCount = 250
                man.score = 0
                man.x = screen_width//2
                man.y = 500

    man.update_rects()
    if not paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and man.x + man.width // 2 < screen_width:
            man.isLeft = False
            right = 1
            man.move_x(right)
        if keys[pygame.K_a] and man.x - man.width // 2 > 0:
            man.isLeft = True
            right = -1
            man.move_x(right)
        if keys[pygame.K_SPACE] and man.y == floor - man.height // 2:
            man.isJump = True
        
        # jump
        if man.isJump:
            man.jump()
            if man.jumpCount <= 0:
                man.isJump = False
                man.jumpCount = 250
        if not man.isJump:
            man.fall()
        if man.y + man.height // 2 >= floor:
            man.y = floor - man.height // 2
            man.airborne = False
        
        # shoot
        if not man.isShoot:
            man.bulletY = man.y
            man.bulletShoot = man.x
        if man.isShoot and man.inMotion:
            man.shoot(neg)
            man.timeElapsed += 1
            if man.timeElapsed > 40:
                man.isShoot = False
                man.inMotion = False
                man.timeElapsed = 0
            if bullet_hit(man.bullet.get_rect(center = (man.bulletShoot, man.bulletY + 1)), enemylist_rects[-1]):
                man.score += 1
                enemylist[-1].destroy_rect()
                enemylist_rects.append(enemylist[-1].image.get_rect(center = (enemylist[-1].x, enemylist[-1].y)))
                man.isShoot = False
                man.inMotion = False
                man.timeElapsed = 0


    man.update_rects()
    # deth
    if player_collision(man.image_rect, enemylist_rects[-1]):
        paused = True

    if len(enemylist) > 5:
        enemylist.remove(enemylist[0])
        enemylist_rects.remove(enemylist_rects[0])


    man.update_rects()
    screen.blit(enemylist[-1].image, enemylist_rects[-1])
    update_display()
    score_display()

pygame.quit()