import media
import fresh_tomatoes

toy_story = media.Movie("Roaring Currents", "Based on the true story of the greatest naval battle in history",
                  "https://upload.wikimedia.org/wikipedia/en/3/3a/Battle_of_Myeongryang_poster.jpg",
                  "https://www.youtube.com/watch?v=VfYO-t5e40s")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School Of Rock", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight In Paris", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
