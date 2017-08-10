import webbrowser


class Movie ():
      """
      To create an instance of this class you have to pass the folowin data in this order
          movie_title: The name of the movie.
          movie_storyline: A brief description about what the movie is about. 
          poster_image: An URL with the JPG file of the movie poster
          trailer_youtube: An URL pointing to the movie trailer in the youtube webpage.
      """
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ show_trailer function open a browser and load the URL passed by trailer_youtube parameter"""
        webbrowser.open(self.trailer_youtube_url)
