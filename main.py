#!usr/bin/env
import pygame
from pygame.sprite import _Group


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Замість зображення використовуємо кольоровий прямокутник
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))   # Задаємо колір
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    clock = pygame.time.Clock()

    running = True

if __name__ == "__main__":
    main()