import fresh_tomatoes
import media

# creating an instance of class movie

ice_age = media.Movie("Ice Age",
                      "To save themselves, Sid, Manny, Diego, and the rest of the herd must leave their home and embark on a quest full of comedy and adventure.",
                      "http://www.impawards.com/2016/posters/ice_age_five_ver2.jpg",
                      "https://www.youtube.com/watch?v=Ohq6NmKMja8",
                      "Mike Thurmeier",
                      "-",
                      "40.86 crores USD",
                      "10.5 crores USD")

lion_king = media.Movie("Lion King",
                        "Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble.",
                        "http://www.cartoonpics.net/data/media/103/the_lion_king_movie.jpg",
                        "https://www.youtube.com/watch?v=_ujGv5dhGfk",
                        "Rob Minkoff, Roger Allers",
                        "-",
                        "96.85 crores USD",
                        "4.5 crores USD")

despicable_me = media.Movie("Despicable Me",
                            "The mischievous Minions hope that Gru will return to a life of crime after the new boss of the Anti-Villain League fires him.",
                            "https://image.tmdb.org/t/p/w300_and_h450_bestv2/6t3YWl7hrr88lCEFlGVqW5yV99R.jpg",
                            "https://www.youtube.com/watch?v=6DBi41reeF0",
                            "Pierre Coffin, Kyle Balda",
                            "Despicable Me",
                            "103.5 crores USD",
                            "8 crores USD")

cars = media.Movie("Cars",
                   "Blindsided by a new generation of blazing-fast racers, the legendary Lightning McQueen is suddenly pushed out of the sport he loves.",
                   "https://images-na.ssl-images-amazon.com/images/I/51YP4C-LjhL.jpg",
                   "https://www.youtube.com/watch?v=2LeOH9AGJQM",
                   "John Lasseter",
                   "Cars",
                   "38.4 crores USD",
                   "17.5 crores USD")

boss_baby = media.Movie("Boss Baby",
                        "Seven-year-old Tim gets jealous when his parents give all their attention to his little brother.",
                        "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
                        "https://www.youtube.com/watch?v=O2Bsw3lrhvs",
                        "Tom McGrath",
                        "The Boss Baby Film Series",
                        "49.89 crores USD",
                        "12.5 crores USD")

angry_bird = media.Movie("Angry Bird",
                         "The movie takes us to an island populated entirely by happy, flightless birds or almost entirely.",
                         "https://media.services.cinergy.ch/media/box1600/1931a7536713d76de3f61757d9868bde5e1c41d9.jpg",
                         "https://www.youtube.com/watch?v=1U2DKKqxHgE",
                         "Clay Kaytis, Fergal Reilly",
                         "-",
                         "34.98 crores USD",
                         "7.3 crores USD")

# movie_list is an array of movie which contains all the movie information
movie_list = [ice_age, lion_king, despicable_me, cars, boss_baby, angry_bird]

# open_movies_page is a function which takes the list of movie as an argument and display all movie poster on the screen
fresh_tomatoes.open_movies_page(movie_list)
