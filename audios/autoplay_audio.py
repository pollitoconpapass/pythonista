import pygame
from io import BytesIO


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path) # if you pass the file and not the path: .load(BytesIO(file))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        