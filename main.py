import pygame
import random
import pygame.freetype
from pygame.rect import Rect
from enum import Enum
from sys import exit
from ui_element import UIElement, create_surface_with_text
from toolbar import Toolbar
from toolbar import Divider
from icon import Icon
import pygame_widgets
import textwrap
from food_info import food_info
from exercise_info import exercise_info
from smoke_info import smoke_info
from age_info import age_info
from game_state import ChangeGamestate, GameState, game_state
from cholesterol import create_cholesterol, cholesterol_equation, convert_chol_to_bpm
from datetime import datetime

BLUE = (106, 159, 181)
WHITE = (245, 245, 245)
heartimg = pygame.image.load('images/svgheart.svg')
smallimg = pygame.transform.scale(heartimg, (255, 425))

def main():
    pygame.init()

    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Personal Project - Heart Simulator')

    while True:
        if game_state['state'] == GameState.TITLE:
            game_state['state'] = title_screen(screen)

        if game_state['state'] == GameState.MAIN:
            game_state['state'] = play_level(screen)

        if game_state['state'] == GameState.FOOD:
            game_state['state'] = food_info(screen)

        if game_state['state'] == GameState.EXERCISE:
            game_state['state'] = exercise_info(screen)

        if game_state['state'] == GameState.SMOKE:
            game_state['state'] = smoke_info(screen)

        if game_state['state'] == GameState.AGE:
            game_state['state'] = age_info(screen)

        if game_state['state'] == GameState.QUIT:
            pygame.quit()
            return

def title_screen(screen):

    start_btn = UIElement(
        center_position=(512, 612),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=GameState.MAIN,
    )
    quit_btn = UIElement(
        center_position=(512, 712),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    title1 = create_surface_with_text(text = "Exploring the Effects of",font_size = 40, text_rgb = WHITE, bg_rgb = BLUE)
    title1_rect = title1.get_rect(center = (512, 90))

    title2 = create_surface_with_text(text = "Lifestyle Factors on Heart Health",font_size = 40, text_rgb = WHITE, bg_rgb = BLUE)
    title2_rect = title2.get_rect(center = (512, 130))

    while True:
        mouse_up = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            screen.fill(BLUE)
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit()


        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        screen.blit(title1, title1_rect)
        screen.blit(title2, title2_rect)
        screen.blit(smallimg,(370,150))


        pygame.display.flip()

def empty():
    pass

def play_level(screen):

    toolbar = Toolbar(1024, 250)

    small_heart = Icon(pygame.transform.scale(heartimg, (186, 310)), (150,120))
    big_heart = Icon(pygame.transform.scale(heartimg, (200, 333)), (150,120))


    icons = [
        Icon(pygame.transform.scale(pygame.image.load('images/bad_food.svg'),(50,50)), (79,575)),
        Icon(pygame.transform.scale(pygame.image.load('images/good_food.png'),(50,50)), (179,575)),

        Icon(pygame.transform.scale(pygame.image.load('images/no_exercise.svg'),(50,50)), (309,575)),
        Icon(pygame.transform.scale(pygame.image.load('images/exercise.svg'),(50,50)), (409,575)),

        Icon(pygame.transform.scale(pygame.image.load('images/no-smoking.svg'),(50,50)), (558,575)),
        Icon(pygame.transform.scale(pygame.image.load('images/smoke.svg'),(50,50)), (658,575)),

        Icon(pygame.transform.scale(pygame.image.load('images/baby.png'),(50,50)), (795,575)),
        Icon(pygame.transform.scale(pygame.image.load('images/old_man.svg'),(54,54)), (892,575)),

        Icon(pygame.transform.scale(pygame.image.load('images/pygame_blood.png'),(420,200)), (561,150))
    ]

    screen_divider = Divider(5, 768)

    factors = [
        pygame_widgets.Button(screen, 104, 685, 100, 20, inactiveColour = (106, 159, 181), hoverColour = (57, 96, 113), pressedColour = (39, 64, 75), text = 'Food', fontSize = 17, onClick = ChangeGamestate, onClickParams = (game_state, GameState.FOOD)),
        pygame_widgets.Button(screen, 334, 685, 100, 20, inactiveColour = (106, 159, 181), hoverColour = (57, 96, 113), pressedColour = (39, 64, 75), text = 'Exercise', fontSize = 17, onClick = ChangeGamestate, onClickParams = (game_state, GameState.EXERCISE)),
        pygame_widgets.Button(screen, 583, 685, 100, 20, inactiveColour = (106, 159, 181), hoverColour = (57, 96, 113), pressedColour = (39, 64, 75), text = 'Smoking', fontSize = 17, onClick = ChangeGamestate, onClickParams = (game_state, GameState.SMOKE)),
        pygame_widgets.Button(screen, 820, 685, 100, 20, inactiveColour = (106, 159, 181), hoverColour = (57, 96, 113), pressedColour = (39, 64, 75), text = 'Age', fontSize = 17, onClick = ChangeGamestate, onClickParams = (game_state, GameState.AGE))
    ]

    sliders = [
        pygame_widgets.Slider(screen, 104, 650, 100, 5, handleRadius = 10),
        pygame_widgets.Slider(screen, 334, 650, 100, 5, handleRadius = 10),
        pygame_widgets.Slider(screen, 583, 650, 100, 5, handleRadius = 10),
        pygame_widgets.Slider(screen, 820, 650, 100, 5, handleRadius = 10),
    ]
    cholesterols = []

    keys = [
        Icon(pygame.transform.scale(pygame.image.load('cholesterol.png'),(31,30)), (805,22)),
        Icon(pygame.transform.scale(pygame.image.load('images/blood_cell.png'),(50,51)), (800,55))
    ]


    cholesterol_key = create_surface_with_text(text = "- cholesterol molecules",font_size = 15,text_rgb = WHITE,bg_rgb = BLUE)
    blood_cell_key = create_surface_with_text(text = "- blood cells",font_size = 15,text_rgb = WHITE,bg_rgb = BLUE)

    cholesterol_key_rect = cholesterol_key.get_rect(center = (930,30))
    blood_cell_key_rect = blood_cell_key.get_rect(center= (900,75))



    heart_selection = 0
    old_time = datetime.now()

    bpm = 60

    while True:

        if game_state['state'] != GameState.MAIN:
            return game_state['state']
        screen.fill(BLUE)
        toolbar.update()
        toolbar.draw(screen)
        screen_divider.update()
        screen_divider.draw(screen)
        for icon in icons:
            icon.draw(screen)
        for key in keys:
            key.draw(screen)
        events = pygame.event.get()
        for event in events:
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit()

        for slider in sliders:
            slider.listen(events)
            slider.draw()
        for factor in factors:
            factor.listen(events)
            factor.draw()
        s_food = sliders[0].getValue()
        s_exercise = sliders[1].getValue()
        s_smoking = sliders[2].getValue()
        s_age = sliders[3].getValue()
        cholesterol_count = cholesterol_equation(s_food, s_exercise, s_smoking, s_age)

        cholesterol_difference = cholesterol_count - len(cholesterols)
        if cholesterol_difference > 0:
            for i in range(cholesterol_difference):
                cholesterols.append(create_cholesterol())
        if cholesterol_difference < 0:
            cholesterols = cholesterols[0:cholesterol_count]

        for cholesterol in cholesterols:
            cholesterol.draw(screen)

        if heart_selection == 0:
            big_heart.draw(screen)
        else:
            small_heart.draw(screen)


        current_time = datetime.now()
        time_difference = current_time - old_time
        if heart_selection == 1:
            bpm = convert_chol_to_bpm(cholesterol_count)
            if time_difference.total_seconds() * 1000 >= 1/(bpm/60)*1000:
                heart_selection = (heart_selection + 1)%2
                old_time = current_time

        else:
            if time_difference.total_seconds() * 1000 >= 100:
                heart_selection = (heart_selection + 1)%2
                old_time = current_time
        rhr = create_surface_with_text(text = "Resting Heart Rate: " + str(round(bpm)) + " bpm",font_size = 25, text_rgb = WHITE, bg_rgb = BLUE)
        rhr_rect = rhr.get_rect(center = (240, 70))
        screen.blit(rhr, rhr_rect)
        screen.blit(cholesterol_key, cholesterol_key_rect)
        screen.blit(blood_cell_key, blood_cell_key_rect)
        pygame.display.flip()



main()
