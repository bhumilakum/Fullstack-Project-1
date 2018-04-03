class Movie:
    """
    This is the class Movie, that contains the information about movie like title, storyline, director etc.
    """

    # this __init__ function initialize or construct the object of class movie by assigning value
    
    def __init__(self, movie_title, movie_story, movie_poster_img, movie_youtube_url, movie_director, movie_film_series, movie_box_office, movie_budget):
        self.title = movie_title
        self.story_line = movie_story
        self.poster_img = movie_poster_img
        self.youtube_trailer_url = movie_youtube_url
        self.director = movie_director
        self.film_series = movie_film_series
        self.box_office = movie_box_office
        self.budget = movie_budget
