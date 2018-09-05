import pygame
import random

pygame.init()
pygame.font.init()

window_width = 1100
window_height = 600
dividing_bar_y = 36
dividing_bar_height = 6

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Donkey X Ball")
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Arial Bold', 22)
small_font = pygame.font.SysFont('Arial Bold', 15)

ball_hit_sound = pygame.mixer.Sound('quick_fart_x.wav')
lost_ball_sound = pygame.mixer.Sound('toilet_flushing.wav')
music = pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play(-1)
