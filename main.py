import pygame
import random
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPEED = 1


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, bottom: bool) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bottom = bottom
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(pygame.image.load('assets/pipe.png'), (self.width, self.height))

        if self.bottom:
            self.image = pygame.transform.rotozoom(self.image, 180, 1)

    def move(self):
        self.rect.x -= SPEED
        if self.rect.right <= 0:
            self.kill()

    def draw(self, surface):
        self.move()
        surface.blit(self.image, self.rect)


class Runtime:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Flappy birds by Ivan Ivanov')
        self.img_background = pygame.image.load('assets/background.jpg')
        self.pipes = pygame.sprite.Group()
        pygame.time.set_timer(25, 5500)

    def setup(self):
        pass

    def spawn_pipes(self):
        height_gap = random.randint(100, 300)
        height_top_pipe = random.randint(50, (SCREEN_HEIGHT - height_gap) - 50)
        height_bottom_pipe = 800 - height_gap - height_top_pipe
        bottom_pipe_y = 800 - height_bottom_pipe
        self.pipes.add(
            Pipe(600, 0, 65, height_top_pipe, False),
            Pipe(600, bottom_pipe_y, 65, height_bottom_pipe, True)
        )

    def draw(self, surface: object) -> None:

        self.screen.fill((255, 255, 255))

        for pipe in self.pipes:
            pipe.draw(surface)

    def run(self):

        running = True
        clock = pygame.time.Clock()
        self.spawn_pipes()

        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == 25:
                    self.spawn_pipes()

            self.draw(self.screen)

            pygame.display.update()


if __name__ == '__main__':
    g = Runtime()
    g.setup()
    g.run()
