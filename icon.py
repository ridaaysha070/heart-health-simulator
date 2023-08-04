import pygame

class Icon:
    def __init__(self, image, position):
        self.image = image
        self.rect = image.get_rect(topleft=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
