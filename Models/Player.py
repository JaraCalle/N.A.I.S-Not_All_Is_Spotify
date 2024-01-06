from Models.SongState import SongState
import pygame
import os
import time
import threading
import random

class Player:
    def  __init__(self, music_dir: str) -> None:
        self.music_dir = music_dir
        self.songs = [song if song.endswith(".mp3") else "" for song in os.listdir(self.music_dir)]
        try:
            self.songs.remove("")
        except ValueError:
            pass
        self.state = SongState()

        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        pygame.init()
        
        self.event_thread = threading.Thread(target=self._pygame_event_handler)
        self.event_thread.daemon = True
        self.event_thread.start()

    def _pygame_event_handler(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    self.play_next()
            time.sleep(0.1)

    def load_first_song(self) -> None:
        pygame.mixer.init()
        self.state.set_song(self.songs[0], 0)
        pygame.mixer.music.load(f"{self.music_dir}/{self.songs[self.state.song_index]}")
        self.play()

    def load_random_song(self) -> None:
        pygame.mixer.init()
        song_index = random.randint(0, len(self.songs) - 1)
        self.state.set_song(self.songs[song_index], song_index)
        pygame.mixer.music.load(f"{self.music_dir}/{self.songs[self.state.song_index]}")
        self.play()

    def load_song(self, song: str) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(song)
    
    def play(self) -> None:
        pygame.mixer.music.play()
        self.state.set_playing(True)
    
    def pause(self, e=None) -> None:
        pygame.mixer.music.pause()
        self.state.set_playing(False)

    def unpause(self, e=None) -> None:
        pygame.mixer.music.unpause()
        self.state.set_playing(True)
    
    def play_next(self, e=None) -> None:
        self.pause()
        try:
            self.state.set_song(self.songs[self.state.song_index + 1], self.state.song_index + 1)
        except IndexError:
            self.state.set_song(self.songs[0], 0)

        self.load_song(f"{self.music_dir}/{self.songs[self.state.song_index]}")
        self.play()

    def play_random_next(self, e=None) -> None:
        self.pause()
        song_index = random.randint(0, len(self.songs) - 1)
        while song_index == self.state.song_index:
            song_index = random.randint(0, len(self.songs) - 1)
        self.state.set_song(self.songs[song_index], song_index)
        self.load_song(f"{self.music_dir}/{self.songs[self.state.song_index]}")
        self.play()