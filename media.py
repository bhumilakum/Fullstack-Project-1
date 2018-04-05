class Movie:
    """
    A class Movie acts as a template. This creates instances of this class.
    Such as:
    movie_name = Movie()

    The class Movie is defined in file media.py, and to create an instance of
    this class, a developer should import this file. After that, the instance
    will be created such as,
    movie_name = media.Movie()

    To create an object of this class, a user should write code as mentioned
    below by passing all required arguments.

    Syntax:
    movie_name = media.Movie(movie_title, movie_story, movie_poster_img, 
        movie_youtube_url, director, film_series, box_office, budget)

    Example: 
        ice_age = media.Movie("Ice Age",
                              "Example description",
                              "http://www.impawards.com/ice_age_five.jpg",
                              "https://www.youtube.com/watch?v=Ohq6NmKMja8",
                              "Mike Thurmeier",
                              "-",
                              "40.86 crores USD",
                              "10.5 crores USD")

    The __init__() function initialize or construct the object of a class
    Movie by assigning value.

    def __init__(self, movie_title, movie_story, movie_poster_img, 
        movie_youtube_url, movie_director, movie_film_series, 
        movie_box_office, movie_budget):
        self.title = movie_title
        self.story_line = movie_story
        self.poster_img = movie_poster_img
        ....
        ....
        ....

    The __init__() function does not return any value.

    """

    def __init__(self, movie_title, movie_story, movie_poster_img, 
        movie_youtube_url, movie_director, movie_film_series, 
        movie_box_office, movie_budget):
        self.title = movie_title
        self.story_line = movie_story
        self.poster_img = movie_poster_img
        self.youtube_trailer_url = movie_youtube_url
        self.director = movie_director
        self.film_series = movie_film_series
        self.box_office = movie_box_office
        self.budget = movie_budget
