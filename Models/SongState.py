class SongState:
    def __init__(self) -> None:
        self.is_playing = False
        self.song_index = 0
        self.songs_name = ""
    
    def set_song(self, song: str, index: int) -> None:
        self.songs_name = song
        self.song_index = index

    def set_playing(self, is_playing: bool) -> None:
        self.is_playing = is_playing