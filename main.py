#!usr/bin/env
import pygame
from pygame.sprite import Group
import random


# Ініціалізація параметрів сітки (ігрового поля)
count_cells = 20
cell_size = 20
grid_width = count_cells
grid_height = count_cells
screen_width = grid_width * cell_size
screen_height = grid_height * cell_size

# Встановлення кольорів
BLACK = (0, 0, 0)
RED = (0, 255, 0)
GREEN = (255, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))



def draw_grid():
    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen, BLACK, (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen, BLACK, (0, y), (screen_width, y))


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Замість зображення використовуємо кольоровий прямокутник
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill((0, 128, 255))   # Задаємо колір
        self.rect = self.image.get_rect()
        self.rect.topleft = (cell_size * 10, cell_size * 10)

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


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Замість зображення використовуємо кольоровий прямокутник
        self.image = pygame.Surface((50, 50))
        self.image.fill((128, 0, 255))   # Задаємо колір
        self.rect = self.image.get_rect()
        self.rect.topleft = (175, 175)


def main():
    pygame.init()

    # screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Змійка")
    all_sprites = pygame.sprite.Group()
    snake = Snake()
    all_sprites.add(snake)
    # Встановлення FPS
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        all_sprites.update(keys)

        screen.fill((255, 255, 255))
        draw_grid()
        all_sprites.draw(screen)  # Малюємо спрайт (прямокутник)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()