# Fetch IMDB Ratings
# pip install PyMovieDb
from PyMovieDb import IMDB
movies = IMDB()
# Searching Movie
search_data = movies.search("Spiderman 2", year = 2004)
print(search_data)
# Fetch Movie by name
movie_data = movies.get_by_name("The Dark Knight")
# Fetch Movie by ID
data = movies.get_by_id("tt0468569")
# Fetch Movie by URL name
movie_url_data = movies.get("https://www.imdb.com/title/tt0468569/")
# Fetching Tv Shows
tv_shows = movies.get_by_name("breaking bad")
# Fetch Person Info
person = movies.person_by_name("Christian Bale")
# Fetch Top popular Movies
movie_top = movies.popular_movies(genre="action")
# Fetch Top popular Tv Shows
tv_top = movies.popular_tv(genre="thriller")
# Fetch Upcoming Movies
upcoming = movies.upcoming(region="us")