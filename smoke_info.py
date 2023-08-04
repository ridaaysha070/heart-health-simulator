import pygame
import pygame_widgets
from ui_element import UIElement, create_surface_with_text
from wrap_text import wrap_text, message_display, textvars
from game_state import GameState, ChangeGamestate, game_state
from icon import Icon


BLUE = (106, 159, 181)

def smoke_info(screen):

    screen.fill(BLUE)

    return_button_image = pygame.transform.scale(pygame.image.load('return_button_image.png'),(30,30))
    return_button = pygame_widgets.Button(screen, 20, 20, 30, 30, inactiveColour = (106, 159, 181), hoverColour = (57, 96, 113), pressedColour = (39, 64, 75), image = return_button_image, fontSize = 17, onClick = ChangeGamestate, onClickParams = (game_state, GameState.MAIN))


    while True:
        if game_state['state'] != GameState.SMOKE:
            return game_state['state']
        message_display(screen, 'Calibri', textvars['normal'], (0,0,0), [300,50], 'How Smoking affects your Heart')
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,130], "Cigarette smoke is a toxic mix of more than 7,000 chemicals and, when inhaled, can interfere with important processes in the body that keep it functioning normally. One of these processes is the delivery of oxygen-rich blood to your heart and the rest of your body.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,220], "Research has shown that smoking increases blood pressure, heart rate, tightens arteries, and can cause an irregular heart rhythm, all of which make it hard for your heart to work.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,280], "When you smoke, you also put others at risk. About 40,000 people die of heart and blood vessel diseases caused by secondhand smoke. ")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,350], "Why should one quit smoking? According to the American Heart Association, smoking is the most important preventable cause of death in the United States. Once you decide to quit, you are already on your way to a healthier heart and a reduced risk of heart disease.")

        events = pygame.event.get()
        for event in events:
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit()
        return_button.draw()
        return_button.listen(events)
        Icon(pygame.transform.scale(pygame.image.load('smoke_information.png'),(300,300)), (360,430)).draw(screen)
        pygame.display.flip()
