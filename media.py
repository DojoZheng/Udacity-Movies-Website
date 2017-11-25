import webbrowser

class Movie():
	""" This class provides a way to store movie related information """
	VALID_RATINGS = ["G", "PG","PG-13","R"]

	def __init__(self, movie_title, poster_image, trailer_youku):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_url = trailer_youku

	def show_trailer(self):
		webbrowser.open(self.trailer_url)