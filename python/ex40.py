class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["happy_bday to you",
	               "I don't want to get sued",
	               "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	                    "With pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

newsong = ["happy_dwbday to you",
	        "I dondw't want to get sued",
	        "So Idw'll stop right there"]

new_song = Song(newsong)

new_song.sing_me_a_song()
