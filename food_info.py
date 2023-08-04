import pygame
import pygame_widgets
from ui_element import UIElement, create_surface_with_text
from wrap_text import wrap_text, message_display, textvars
from game_state import GameState, ChangeGamestate, game_state
from icon import Icon

BLUE = (106, 159, 181)

def food_info(screen):

    screen.fill(BLUE)

    return_button_image = pygame.transform.scale(pygame.image.load('return_button_image.png'),(30,30))
    return_button = pygame_widgets.Button(screen, 20, 20, 30, 30, inactiveColour = (106, 159, 181), hoverColour = (57, 96, 113), pressedColour = (39, 64, 75), image = return_button_image, fontSize = 17, onClick = ChangeGamestate, onClickParams = (game_state, GameState.MAIN))


    while True:
        if game_state['state'] != GameState.FOOD:
            return game_state['state']
        message_display(screen, 'Calibri', textvars['normal'], (0,0,0), [320,50], 'How Food affects your Heart')
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,110], "Poor diet is one of the leading risk factors for heart disease. What you eat and drink impacts several heart disease risk factors, including blood pressure, cholesterol, weight and diabetes risk.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,170], "How to reduce your risk of heart disease with healthy eating:")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,210], "1. Limit fried fast food and processed foods.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,240], "2.  Replace energy from saturated fats (like butter) with healthy unsaturated fats from seeds and plants like  olive oil, avocado, sunflower, soybean and sesame.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,290], "3. Increase the variety of plant foods – eat more veggies, fruits and wholegrain cereals.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,320], "4. Trim all visible fat from meat and remove skin from poultry.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,350], "5. Eat legumes regularly – like baked beans (reduced salt), soybeans, lentils and tofu.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,380], "6. Snack on a handful of nuts on most days of the week (especially walnuts and almonds).")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,410], "7. Eat oily fish at least once per week.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,440], "8. Reduce your salt intake – replace salt at the table and in cooking with herbs and spices. ")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [65,470], "9. Choose unflavoured milk, yoghurt and cheese.")
        message_display(screen, 'Calibri', textvars['small'], (0,0,0), [140,710], "Healthy eating plate made up of 1/2 vegetables, 1/4 carbohydrates and 1/4 protein.")


        events = pygame.event.get()
        for event in events:
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit()
        return_button.draw()
        return_button.listen(events)
        Icon(pygame.transform.scale(pygame.image.load('healthy_food.png'),(209,200)), (412,500)).draw(screen)
        pygame.display.flip()
