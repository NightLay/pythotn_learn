
import pygame
import random

from os import path
img_dir = path.join(path.dirname(__file__), 'img')

oso = 2
WIDTH = 750
HEIGHT = 500
FPS = 60

# define colors

BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# initialize pygame and create windowцыы
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 65))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 10
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
  
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedx = -8
        if keystate[pygame.K_s]:
            self.speedx = 8
        self.rect.y += self.speedx
        if self.rect.bottom < 65:
            self.rect.bottom = 65
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 
    def shoot(self):  
        if oso > 0:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
        else: 
            attack = Atak(self.rect.centerx, self.rect.bottom)
            all_sprites.add(attack)
            attaks.add(attack) 
player = Player

#  ww
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NightLay's game! ")
clock = pygame.time.Clock()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = random.randrange(10, 60)
        self.image = pygame.Surface((a,  a))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = -1000#random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(400, 1000)
        self.speedx = random.randrange(1, 8)
        self.speedy = random.randrange(-6, 6)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(-40, -10)
            self.rect.y = random.randrange(0, 600)
            self.speedy = random.randrange(-3, 3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx  = x
        self.rect.centery = y
        self.speedx = random.randrange (-12, -10)
        self.speedy = random.randrange(-1, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # kill if it moves  off the top of the scr
        if self.rect.bottom < 0:
            self.kill()    



class Atak(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx  = x
        self.rect.centery = y
        self.speedx = random.randrange(-12, -10)
        self.speedy = random.randrange(-1, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # kill if it moves  off the top of the screen 
        if self.rect.bottom < 0 or self.rect.left < 0 or self.rect.right < 0 :
            self.kill()


background = pygame.image.load(path.join(img_dir, 'starfield.png' )).convert()
background_rect = background.get_rect()



all_sprites = pygame.sprite.Group()
player = Player()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
attaks = pygame.sprite.Group()
all_sprites.add(player)            
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
# Game loopццыыцццыфыц
qwerty = True
while qwerty:
    all_sprites.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            qwerty = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                oso *= -1
                player.shoot()    
    all_sprites.update
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        qwerty = False
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits = pygame.sprite.groupcollide(mobs, attaks, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    #all_sprites.update()

    # Draw / render 
    screen.fill(GREEN)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()