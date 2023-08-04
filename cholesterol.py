import pygame
from icon import Icon
import random


INITIAL_CHOLESTEROL = 30

def create_cholesterol():

    cholesterol_x_coordinate = random.randint(561, 946)
    c = random.randint(3,4)
    if c == 3:
        cholesterol_y_coordinate = random.randint(170, 193)

    if c == 4:
        cholesterol_y_coordinate = random.randint(277, 305)

    return Icon(pygame.transform.scale(pygame.image.load('cholesterol.png'),(31,30)), (cholesterol_x_coordinate, cholesterol_y_coordinate))

def cholesterol_equation(food, exercise, smoking, age):
    cholesterol_count = (- food - exercise + smoking + age) + INITIAL_CHOLESTEROL
    if cholesterol_count < 5:
         cholesterol_count = 5
    return cholesterol_count

def convert_chol_to_bpm(cholesterol_count):
    bpm = ((60 * (cholesterol_count - 5))/223)+60
    return bpm
