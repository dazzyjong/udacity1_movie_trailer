import webbrowser

class Movie():
    """
    Attributes:
        title: The movie title
        storyline: Summarized story of the movie
        poster_image_url: The URL of Movie's poster
        trailer_youtube_url: The URL of Movie's youtube trailer
    """
    def __init__(self, title, storyline, poster_image_url, youtube_trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = youtube_trailer_url

    def show_trailer(self):
        """Open a default web browser with youtube trailer URL"""
        webbrowser.open(self.youtube_trailer_url)
