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


def main():
    pass

if __name__ == "__main__":
    main()