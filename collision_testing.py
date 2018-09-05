import pygame
import random
import os

width = 800
height = 600
fps = 30

BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Testing')
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Arial Bold', 22)

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "glasspaddle2.png")).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.ox = (width / 2) - self.rect.center[0]
        self.oy = (height / 2) - self.rect.center[1]

        self.image.set_colorkey(BLACK)
        self.rect.center = (width / 2, height /2)
        self.y_speed = 5
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5

        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5

        self.rect.x += self.speedx
        self.rect.y += self.speedy


class GameBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "ball.png")).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (width / 2, height /2)

    def update(self):
        pass


all_sprites = pygame.sprite.Group()
random_sprites = pygame.sprite.Group()


player = Player()
ball = GameBall()
all_sprites.add(player)
random_sprites.add(ball)
# Game Loop
running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update()
    screen.fill((120, 120, 120))
    all_sprites.draw(screen)
    random_sprites.draw(screen)

    collide = pygame.sprite.spritecollide(ball, all_sprites, False, pygame.sprite.collide_mask)
    if collide:
        scoretext = myfont.render("HIT!", 1, (100, 100, 100))
        screen.blit(scoretext, (5, 12))


    pygame.display.flip()

pygame.quit()
