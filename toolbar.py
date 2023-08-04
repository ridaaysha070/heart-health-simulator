import pygame

DARKBLUE = (77,129,151)
class Toolbar:
    def __init__(self, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill(DARKBLUE)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,768)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def click(pos):
        pass

class Divider:
    def __init__(self, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill(DARKBLUE)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (510, 519)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def click(pos):
        pass
