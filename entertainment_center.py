import media
import fresh_tomatoes

"""Create 6 movie instances and called fresh_tomatoes.open_movies_page(movies)"""

roaring_currents = media.Movie("Roaring Currents", "Based on the true story of the greatest naval battle in history",
                  "https://upload.wikimedia.org/wikipedia/en/3/3a/Battle_of_Myeongryang_poster.jpg",
                  "https://www.youtube.com/watch?v=VfYO-t5e40s")

captain_america_cw = media.Movie("Captain America", "Marvel Comics crossover storyline",
                "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                "https://www.youtube.com/watch?v=dKrVegVI0Us")

masquerade = media.Movie("Masquerade", "The Man Who Became King",
                "https://upload.wikimedia.org/wikipedia/en/8/85/Gwanghae.jpg",
                "https://www.youtube.com/watch?v=1TnfM5XWOtI")

starwars = media.Movie("Star Wars", "Star Wars begins again",
                "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                "https://www.youtube.com/watch?v=sGbxmsDFVnE")

midnight_in_paris = media.Movie("Midnight In Paris", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [roaring_currents, captain_america_cw, masquerade, starwars, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
