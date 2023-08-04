import pygame
import pygame_widgets
from ui_element import UIElement, create_surface_with_text
from wrap_text import wrap_text, message_display, textvars
from game_state import GameState, ChangeGamestate, game_state
from icon import Icon


BLUE = (106, 159, 181)

def age_info(screen):

    screen.fill(BLUE)

    return_button_image = pygame.transform.scale(pygame.image.load('return_button_image.png'),(30,30))
    return_button = pygame_widgets.Button(screen, 20, 20, 30, 30, inactiveColour = (106, 159, 181), hoverColour = (57, 96, 113), pressedColour = (39, 64, 75), image = return_button_image, fontSize = 17, onClick = ChangeGamestate, onClickParams = (game_state, GameState.MAIN))


    while True:
        if game_state['state'] != GameState.AGE:
            return game_state['state']
        message_display(screen, 'Calibri', textvars['normal'], (0,0,0), [340,50], 'How Age affects your Heart')
        message_display(screen, 'Calibri', textvars['medium'], (0,0,0), [65,130], "Aging is a non-modifiable risk factor for heart disease, much like sex and family history. Aging can cause changes in the heart and blood vessels - for example, as you get older, your heart can't beat as fast during physical activity or times of stress as it did when you were younger. They become less flexible, making it harder for blood to move through them easily. Fatty deposits called plaques also collect along your artery walls and slow the blood flow from the heart. These things, along with poor nutrition and exercise habits, can increase your risk of heart disease. Add other risk factors — such as high blood pressure, smoking, and diabetes — and it's likely that you will have a greater risk for a heart attack.")

        events = pygame.event.get()
        for event in events:
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit()
        return_button.draw()
        return_button.listen(events)
        Icon(pygame.transform.scale(pygame.image.load('age_stats.png'),(397,300)), (310,430)).draw(screen)
        pygame.display.flip()
