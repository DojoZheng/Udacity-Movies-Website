import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"http://player.youku.com/embed/XMTE2MDEyNDU2")
# print(toy_story.storyline)
# toy_story.show_trailer()

avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					"http://player.youku.com/embed/XMTk4ODUyNDQ4")

# print(avatar.storyline)
# avatar.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)