# -*- coding: utf-8 -*-
"""
@author: Andreas Spielhofer
"""
import movie_1 as media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life", 
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", 
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")


the_hunt = media.Movie("The Hunt",
                       "A teacher that becomes target of social outcast", 
                       "https://upload.wikimedia.org/wikipedia/en/4/44/The_Hunt_%282012_film%29.jpg", 
                       "https://www.youtube.com/watch?v=vK9cO7QN8Ak")                   

midnight_in_paris = media.Movie("Midnight in Paris", 
                                "A writer that misteriously goes back to the 1920's",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

memento = media.Movie("Memento",
                      "The inability to form new memories and suffers short-term memory loss approximately every five minutes",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")


#toy_story.storyline()
#avatar.show_trailer()
#the_hunt.title()

movies = [toy_story, avatar, the_hunt, midnight_in_paris, memento]
fresh_tomatoes.open_movies_page(movies)

