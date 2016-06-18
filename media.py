import webbrowser

class Movie():
    valid_rating = ["G", "PG", "PG-13", "R"]

    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        # This will open a browser and play trailer





# note to self: __init__ means it initalizes or creates space in meory, to remember details like title, story ....
# it takes few pieces of information or arguments.


