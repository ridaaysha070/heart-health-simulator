import pygame

class Button:

    def __init__(self, image, position, action):

        self._image = image
        self._rect = image.get_rect(topleft=position)
        self._action = action

    def draw(self, screen):
        screen.blit(self._image, self._rect)

    def event_handler(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    self._action()
