from app.enum.default_args import DefaultArgs

class CurrentModel():
    def __init__(self, user, artist, song, song_url, album, album_cover):
        self.user = user
        self.artist = artist
        self.song = song
        self.song_url = song_url
        self.album = album
        self.album_cover = album_cover
        self.theme = DefaultArgs.THEME.value
        self.style = DefaultArgs.STYLE.value
        self.reload = DefaultArgs.RELOAD.value
    
    def json(self):
        return {
            "user": self.user,
            "artist": self.artist,
            "song": self.song,
            "song_url": self.song_url,
            "album": self.album,
            "album_cover": self.album_cover, 
            "theme": self.theme,
            "style": self.style,
            "reload": self.reload
        }

    def set_theme(self, theme):
        self.theme = theme
        
    def set_style(self, style):
        self.style = style
        
    def set_reload(self, time_refresh):
        self.reload = time_refresh
