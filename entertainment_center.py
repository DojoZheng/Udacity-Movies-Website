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

pianist = media.Movie("The Legend of 1900",
					"An epic story of a man who could do anything...except be ordinary.",
					"https://images-na.ssl-images-amazon.com/images/M/MV5BMTU5NjgyMjEyMV5BMl5BanBnXkFtZTcwNTA4NjIyMQ@@._V1_.jpg",
					"http://player.youku.com/embed/XMjcyOTMxMg==")

wolf = media.Movie("Wolf Warrors 2",
					"An man who tried to save all the people in Africa",
					"https://upload.wikimedia.org/wikipedia/en/b/b5/Wolf_Warriors_2_poster.jpeg",
					"http://player.youku.com/embed/XMjQ4Mzc4ODQwOA==")

spider = media.Movie("Spider Man",
					"The story of our hero - spider man.",
					"https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
					"http://player.youku.com/embed/XMzAxOTkwMTM4MA==")

kongfu = media.Movie("Attack & Defence",
					"Our Papa Ma Yun is playing Kongfu.",
					"https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign=b3f364854190f60310bd9415587bd87e/4d086e061d950a7b3b79a67001d162d9f2d3c932.jpg",
					"http://player.youku.com/embed/XMzE0ODE3NTgwOA==")


movies = [toy_story, avatar, pianist, wolf, spider, kongfu]
fresh_tomatoes.open_movies_page(movies)
# print (media.Movie.VALID_RATINGS)
# print (media.Movie.__doc__)
# print (media.Movie.__name__)
# print (media.Movie.__module__)