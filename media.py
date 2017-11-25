import webbrowser

class Movie():
	""" This class provides a way to store movie related information """


	# Class Variable: These are the Movies Ratings 
	# G: General Audiences. All ages admitted.
	# PG: Parental Guidance Suggested. Some material may not be suitable for children.
	# PG-13: Parents Strongly Cautioned. Some material may be inappropriate for children under 13.
	# R: Restricted. Under 17 requires accompanying parent or adult guardian.
	# NC-17: No Children. No one 17 and under admitted.
	VALID_RATINGS = ["G", "PG","PG-13","R","NC-17"]

	def __init__(self, movie_title, poster_image, trailer_youku, rating):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_url = trailer_youku
		self.valid_rating = rating

	def show_trailer(self):
		webbrowser.open(self.trailer_url)