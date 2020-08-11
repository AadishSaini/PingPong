import pygame
from settings import *

# player1 class
class p1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/paddle_l.png")
        self.rect = self.image.get_rect()
        self.rect.center = (20, 310)
        self.x_vel = 0
        self.y_vel = 0

    # events of player
    def event(self):
        # key list
        keys = pygame.key.get_pressed()
        # w pressed
        if keys[pygame.K_w]:
            self.y_vel = -10
            self.rect.y += self.y_vel
        # s pressed
        if keys[pygame.K_s]:
            self.y_vel = 10
            self.rect.y += self.y_vel

        # Boundaries
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


# Player2 class
class p2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/paddle_r.png")
        self.rect = self.image.get_rect()
        self.rect.center = (830 + 8, 310)
        self.x_vel = 0
        self.y_vel = 0

    # events
    def event(self):
        # key list
        keys = pygame.key.get_pressed()
        # up key pressed
        if keys[pygame.K_UP]:
            self.y_vel = -10
            self.rect.y += self.y_vel
        # down key pressed
        if keys[pygame.K_DOWN]:
            self.y_vel = 10
            self.rect.y += self.y_vel

        # Boundaries
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


# Ball class
class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pl1 = p1()
        self.pl2 = p2()
        self.x_vel = 5
        self.y_vel = -5

    # update(MOVEMENT OF BALL WITH UP AND DOWN BOUNDARIES)
    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        if self.rect.top == 0:
            self.y_vel *= -1
        if self.rect.bottom == HEIGHT:
            self.y_vel *= -1


class collision:
    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col
