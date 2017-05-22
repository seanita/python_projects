import mystuff2

thing = mystuff2.MyStuff()

print(thing.apple())
print(thing.tangerine)


class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

lyrics1  = ["Happy birthday to you",
					"I don't wan to get sued",
					"So I'll stop right here"]

happy_bday = Song(lyrics1)

lyrics2 = ["They rally around the family", 
						"With pockets full of shells"]

bulls_on_parade = Song(lyrics2)


happy_bday.sing_me_a_song() 
print('\n')
bulls_on_parade.sing_me_a_song()
--
snippets = PHRASES.keys()

for snippet in snippets:
	print(snippet)
	print(snippet.count("self"))