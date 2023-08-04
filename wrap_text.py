import pygame
import textwrap

textvars = {'large':[90,22,90], 'medium':[22,90,30], 'normal':[28,130,40], 'small':[20,100,20]}

def wrap_text(message, wraplimit):
    return textwrap.fill(message, wraplimit)

def message_display(screen, myfont, textvars, color, xy,message):
    font_object = pygame.font.SysFont(myfont,textvars[0])
    message = wrap_text(message,textvars[1])
    for part in message.split('\n'):
         rendered_text = font_object.render(part, True, (color))
         screen.blit(rendered_text,(xy))
         xy[1] += textvars[2]
