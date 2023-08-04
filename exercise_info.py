import pygame
import pygame_widgets
from ui_element import UIElement, create_surface_with_text
from wrap_text import wrap_text, message_display, textvars
from game_state import GameState, ChangeGamestate, game_state
from icon import Icon


BLUE = (106, 159, 181)

def exercise_info(screen):

    screen.fill(BLUE)

    return_button_image = pygame.transform.scale(pygame.image.load('return_button_image.png'),(30,30))
    return_button = pygame_widgets.Button(screen, 20, 20, 30, 30, inactiveColour = (106, 159, 181), hoverColour = (57, 96, 113), pressedColour = (39, 64, 75), image = return_button_image, fontSize = 17, onClick = ChangeGamestate, onClickParams = (game_state, GameState.MAIN))


    while True:
        if game_state['state'] != GameState.EXERCISE:
            return game_state['state']
        message_display(screen, 'Calibri', textvars['normal'], (0,0,0), [310,50], 'How Exercise affects your Heart')
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,110], " - Regular exercise is an important way to lower your risk of heart disease. Exercising for 30 minutes or more on most days can help you lose weight, improve your cholesterol, and even lower your blood pressure by as many as five to seven points.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,200], " - Just as exercise strengthens other muscles in your body, it helps your heart muscle become more efficient and better able to pump blood throughout your body. This means that the heart pushes out more blood with each beat, allowing it to beat slower and keep your blood pressure under control.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,290], " - Physical activity also allows better blood flow in the small blood vessels around your heart. Clogs in these arteries can lead to heart attacks.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,360], " - Exercise also increases your levels of HDL cholesterol, the 'good' cholesterol that lowers heart disease risk by flushing the artery-clogging LDL or 'bad' cholesterol out of your system.")

        events = pygame.event.get()
        for event in events:
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit()
        return_button.draw()
        return_button.listen(events)
        Icon(pygame.transform.scale(pygame.image.load('healthy_exercises.jpeg'),(380,300)), (320,440)).draw(screen)
        pygame.display.flip()
