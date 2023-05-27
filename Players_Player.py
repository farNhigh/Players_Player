import os
import time
import datetime
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
import pygame_gui
import locale

# SIZE PARAMETERS
window_size = width, height = (600, 600)
button_size1 = b_width, b_height = (150, 50)
button_size2 = b_width, b_height = (80, 50)
margin = 15

# LOAD AUDIO FILE
mixer.init()
mixer.music.set_volume(0.5)
pygame.init()
pygame.display.set_caption("Players' Player")
window_surface = pygame.display.set_mode(window_size)

# INITIALIZE UI
gradient_surface = pygame.Surface((width, height))
for y in range(height):
    r = int((255 * y) / height)
    g = int((255 * y) / height)
    b = 0
    gradient_surface.fill((r, g, b), (0, y, width, 1))
manager = pygame_gui.UIManager(window_size)

# Load the image
image1 = pygame.image.load("uk_flag.png")
image2 = pygame.image.load("ro_flag.png")
image3 = pygame.image.load("Players_Player.png")

# Resize the image to 64x64 pixels
image1 = pygame.transform.scale(image1, (60, 45))
image2 = pygame.transform.scale(image2, (60, 45))
image3 = pygame.transform.scale(image3, (80, 80))

# Initial position of the image
image1_x = 30
image1_y = 125
image2_x = 100
image2_y = 125
image3_x = 505
image3_y = 420

# CREATE GUI WIDGETS
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 360), button_size1),
                                           text="Play",
                                           manager=manager)
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 407), button_size1),
                                            text="Pause",
                                            manager=manager)
stop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 454), button_size1),
                                           text="Stop",
                                           manager=manager)
browse_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 501), button_size1),
                                             text="Browse",
                                             manager=manager)
language_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 70), button_size1),
                                              text="Change Language",
                                              manager=manager)
about_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((505, 501), button_size2),
                                             text="About",
                                             manager=manager)
clock = pygame.time.Clock()

# STATE PARAMETERS
is_running = True
is_pause = False
file_path = None
language = "English"  # Default language is English

play_button.disable()
pause_button.disable()
stop_button.disable()

def select_file():
    global file_path
    root1 = tk.Tk()
    root1.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        mixer.music.load(file_path)
        play_button.enable()

def show_about():
    if language == "English":
        messagebox.showinfo("About", "This software was created by Ionut-Alexandru VIZUROIU.\nContact alexandru.vizuroiu@gmail.com for further info.")
    if language == "Romanian":
        messagebox.showinfo("Despre", "Acest software a fost creat de Ionut-Alexandru VIZUROIU.\nPentru mai multe informații: alexandru.vizuroiu@gmail.com.")

# Function to update the language
def update_language():
    global language
    if language == "English":
        play_button.set_text(text="Play")
        pause_button.set_text(text="Pause")
        stop_button.set_text(text="Stop")
        browse_button.set_text(text="Browse")
        language_button.set_text(text="Change Language")
        about_button.set_text(text="About")
    elif language == "Romanian":
        play_button.set_text(text="Cântă")
        pause_button.set_text(text="Pauză")
        stop_button.set_text(text="Oprește")
        browse_button.set_text(text="Încarcă")
        language_button.set_text(text="Schimbă Limba")
        about_button.set_text(text="Despre")

# Function to handle language change events
def handle_language_change():
    global language
    if language == "English":
        language = "Romanian"
    else:
        language = "English"
    update_language()

# APP DURATION
is_running = True
while is_running:

    if language == "English":
        # update display
        time_delta = clock.tick(60) / 900.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    pause_button.enable()
                    stop_button.enable()
                    play_button.set_text(text="Playing")
                    pause_button.set_text(text="Pause")
                    stop_button.set_text(text="Stop")
                    if is_pause:
                        pygame.mixer.music.unpause()
                        is_pause = False
                        pause_button.set_text(text="Pause")
                    else:
                        mixer.music.play()
                elif event.ui_element == pause_button:
                    if is_pause:
                        pygame.mixer.music.unpause()
                        is_pause = False
                        pause_button.set_text(text="Pause")
                        play_button.set_text(text="Play")
                        stop_button.set_text(text="Stop")
                    else:
                        mixer.music.pause()
                        is_pause = True
                        pause_button.set_text(text="Paused")
                        play_button.set_text(text="Continue")
                elif event.ui_element == stop_button:
                    play_button.set_text(text="Play")
                    stop_button.set_text(text="Stopped")
                    pause_button.set_text(text="Pause")
                    mixer.music.stop()
                elif event.ui_element == browse_button:
                    select_file()
                elif event.ui_element == language_button:
                    handle_language_change()
                elif event.ui_element == about_button:
                    show_about()

    if language == "Romanian":
        # update display
        time_delta = clock.tick(60) / 900.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    pause_button.enable()
                    stop_button.enable()
                    play_button.set_text(text="CÂNTĂ")
                    pause_button.set_text(text="Pauză")
                    stop_button.set_text(text="Oprește")
                    if is_pause:
                        pygame.mixer.music.unpause()
                        is_pause = False
                        pause_button.set_text(text="Pauză")
                    else:
                        mixer.music.play()
                elif event.ui_element == pause_button:
                    if is_pause:
                        pygame.mixer.music.unpause()
                        is_pause = False
                        pause_button.set_text(text="Pauză")
                        play_button.set_text(text="Cântă")
                        stop_button.set_text(text="Oprește")
                    else:
                        mixer.music.pause()
                        is_pause = True
                        pause_button.set_text(text="Ai pus pauză")
                        play_button.set_text(text="Continuă")
                elif event.ui_element == stop_button:
                    play_button.set_text(text="Cântă")
                    stop_button.set_text(text="Oprit")
                    pause_button.set_text(text="Pauză")
                    mixer.music.stop()
                elif event.ui_element == browse_button:
                    select_file()
                elif event.ui_element == language_button:
                    handle_language_change()
                elif event.ui_element == about_button:
                    show_about()

    manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(gradient_surface, (0, 0))
    manager.draw_ui(window_surface)

    locale.setlocale(locale.LC_TIME, 'en-US')

    current_time = time.strftime("%H:%M:%S", time.localtime())
    current_date = datetime.date.today().strftime("%b %d %Y")
    font = pygame.font.SysFont(None, 40)
    date_text_surface = font.render(current_date, True, (55, 255, 255))
    time_text_surface = font.render(current_time, True, (55, 255, 255))
    date_x = width - date_text_surface.get_width() - 20
    time_x = width - time_text_surface.get_width() - 20

    window_surface.blit(image1, (image1_x, image1_y))
    window_surface.blit(image2, (image2_x, image2_y))
    window_surface.blit(image3, (image3_x, image3_y))
    window_surface.blit(date_text_surface, (date_x, 70))
    window_surface.blit(time_text_surface, (time_x, 110))
    pygame.display.update()

pygame.quit()
