import media
import fresh_tomatoes

# initialize the movies data
movies_data = [
	# toy_story
	["Toy Story",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"http://player.youku.com/embed/XMTE2MDEyNDU2",
	media.Movie.VALID_RATINGS[0]],

	# avatar
	["Avatar",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"http://player.youku.com/embed/XMTk4ODUyNDQ4",
	media.Movie.VALID_RATINGS[1]],

	# pianist
	["The Legend of 1900",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMTU5NjgyMjEyMV5BMl5BanBnXkFtZTcwNTA4NjIyMQ@@._V1_.jpg",
	"http://player.youku.com/embed/XMjcyOTMxMg==",
	media.Movie.VALID_RATINGS[2]],

	# wolf
	["Wolf Warrors 2",
	"https://upload.wikimedia.org/wikipedia/en/b/b5/Wolf_Warriors_2_poster.jpeg",
	"http://player.youku.com/embed/XMjQ4Mzc4ODQwOA==",
	media.Movie.VALID_RATINGS[3]],

	# spiderman
	["Spider Man",
	"https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
	"http://player.youku.com/embed/XMzAxOTkwMTM4MA==",
	media.Movie.VALID_RATINGS[3]],

	# kongfu
	["Attack & Defence",
	"https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign=b3f364854190f60310bd9415587bd87e/4d086e061d950a7b3b79a67001d162d9f2d3c932.jpg",
	"http://player.youku.com/embed/XMzE0ODE3NTgwOA==",
	media.Movie.VALID_RATINGS[4]]
]

# initialize the movies array
movies_arr = []
for movie in movies_data:
	movie_name = movie[0]
	movie_imageUrl = movie[1]
	movie_url = movie[2]
	movie_rating = movie[3]
	print(movie_name + ":" + movie_rating)
	movies_arr.append(media.Movie(movie_name, movie_imageUrl, movie_url, movie_rating))

# 

# open movies page in browser
fresh_tomatoes.open_movies_page(movies_arr)
