#!/usr/bin/env python2.7

import media
import fresh_tomatoes

# movies data to input to site (Title, Storyline, Photo URL, Trailer URL)
muppet_treasure_island = media.Movie("Muppet Treasure Island", "A story about pirate Muppets" , "https://upload.wikimedia.org/wikipedia/en/a/a3/Muppettreasure.png", "https://www.youtube.com/watch?v=KLUdKoCganU")
american_beauty = media.Movie("American Beauty", "A movie about a typical American family" , "https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg", "https://www.youtube.com/watch?v=hIq9Zjw0mm8")
dumb_and_dumber = media.Movie("Dumb & Dumber", "A movie about two best friends" , "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg", "https://www.youtube.com/watch?v=MSu25pQ4iFw")

# list of movies to be displyed
movies = [muppet_treasure_island, american_beauty, dumb_and_dumber]


# builds html web page with movies
fresh_tomatoes.open_movies_page(movies)
