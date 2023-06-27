import pygame
import os

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def list_music_files(directory):
    music_files = []
    for file in os.listdir(directory):
        if file.endswith('.mp3') or file.endswith('.wav'):
            music_files.append(file)
    return music_files

pygame.init()
pygame.mixer.init()

music_directory = r"C:\Users\AYUSH\OneDrive\Desktop\new_songs"

files = list_music_files(music_directory)

print("Available Music Files:")
for i, file in enumerate(files):
    print(f'{i+1}. {file}')

selection = int(input('Select a file to play (enter the corresponding number): '))

if 1 <= selection <= len(files):
    selected_file = files[selection - 1]
    file_path = os.path.join(music_directory, selected_file)

    play_music(file_path)

    input("Press Enter to stop the music...")
    stop_music()
else:
    print("Invalid selection!")
