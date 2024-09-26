#!usr/bin/env
import pygame
from pygame.sprite import Group


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Замість зображення використовуємо кольоровий прямокутник
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))   # Задаємо колір
        self.rect = self.image.get_rect()
        # self.rect.center = (400, 300)
        self.rect.topleft = (175, 175)

    def update(self, keys):
        step = self.rect.width

        # Для керування напрямом руху спрайту'
        directions = {
            pygame.K_LEFT: (-step, 0),
            pygame.K_RIGHT: (step, 0),
            pygame.K_UP: (0, -step),
            pygame.K_DOWN: (0, step)
        }

        for key, (dx, dy) in directions.items():
            if keys[key]:
                self.rect.x += dx
                self.rect.y += dy


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    # Встановлення FPS
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        all_sprites.update(keys)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)  # Малюємо спрайт (прямокутник)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()