from sys import exit
from random import randint

# Creates an Engine class that has functions that control how scenes work and contains functions from the Map class that calls scenes


class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		current_scene.enter()


class Bar(object):
	def enter(self):
		print('''
			The year is 2517. You are one of 10 crew members on spaceship Firefly.
			Firefly landed on planet Liro hours ago, and now you and several crew members	
			relax with drinks at a local bar. Scanning the room, you see that the	
			Liroans inhabitants appear to be monsters of every shape and size, but twice as large	
			as you and the crew. The evening goes on without incident until a ")	
			few Liroans get drunk and start to singing the Unification Day anthem--a song your	
			captain, a former Browncoast, hates. Before you can stop him, Captain Mal throws a punch	
			at one of the singing Liroans. Zoe joins in. Suddenly, you and your crew are surrounded	
			by a group of big, angry Liroans. What do you do?	
			
				1.	fight back
				2.	radio for help
				3.	tell a Liroan joke 
		''')
		action = input("> ")

		if action == '1' or action == 'fight!':
			print('''
				Ruh-roh! The Liroans clearly outnumber your crew and are a much, much bigger.")
				The get up and surround your crew and then...
			''')
			return'death'

		elif action == '2' or action == 'radio for help':
			print('''
				Good choice! Luckily, the ship quickly picks up your distress signal.
				locks onto your vitals and beams you out of the bar just as the Liroans close in
			''')	 
			return 'ship'

		elif action == '3' or action == 'tell a joke':
			print('''
				Good move! You learned a bit Liroans while on the way to the planet. You tell
				the only Liroan joke you know. They think you are hilarious and invite you
				to play a game of cards
			''')
			return 'cardgame'


class CardGame(object):
	def enter(self):
		print('''
			After the bar incident, you and your crew were invited to play a card game, Galaxy Quest. You are 
			in a small room, with 2 doors. One door you entered and another you figured is an exist to outside.
			On one side of the card table sit three Liroans and on the other side, the side closet to door #2, 
			sit 3 of your crew members. The Liroans are infamous cheaters and who hate to lose. Today is no 
			exception. You glance under the table and see the Liroans passing cards to each other. What do you do?
			1.	yell 'cheaters!'
			2. 	grab money and run
			3. 	draw your gun
		''')

		action = input("> ")

		if action == '1' or action =='yell, cheaters!':
			print('''
				The Liroans become very angry. Although the know they are in fact cheaters
				no has the right to call them on it. Especially not the ones losing because of it.
				The Liroans stand up and then they...
			''')
			return('death')

		elif action == '2' or action =='grab money and run':
			print('''
				You yell 'run' to the crew and reach out the grab the loot on the table.
				A Liroan grabs you by the arm and then they..
				''')
			return('death')

		elif action == '3' or action =='escape back door':
			print('''
				You shoot that Liroans will the entire crew, including you, escape out the back door.
				Your ship, which received your distress signal earlier, is waiting for you. 
			''')
			return('ship')

# This class contains functions/methods for the Ship scene
class Ship(object):
	def enter(self):
		print('''
			You back on the ship, but the Liroans are on your tail. You must escape them, what you do you?
			1.	Open fire
			2. 	Warp drive
			3. 	Cloak		
		''')
		action = input("> ")

		if action == '1' or action == 'open fire':
			print('''
				The Liroan ship backs off, but only for a moment. They return with 2 
				other ships and beginning to fire with everything they have. They...
				''')
			return('death')

		if action == '2' or action == 'warp drive':
			print('''
				You need to enter 2 codes to push the ship into warp drive. The only problem is
				in the thick of the attack, you have forgotten them. You have 5 tries before
				the ship becomes disabled. The only person who can override it is Captain Mal,
				and he has just taken a hit to gut, unable to move. Think hard. What is the warp code?
				''')
			code = "%d%d" % (randint(1,2), randint(1,2))
			guess = input("[keypad]> ")
			guesses = 1

			while guess != code and guesses < 5:
				print("That's not correct. Try again")
				guess = input("[keypad]> ")
				guesses += 1

			if guess == code: 
				print('''
					Excellent! You unlock warp drive and the ship is propelled in a distance
					galaxy many light years away from where you were. The Liroans can never find
					you now. Your crew is once again safe.
					''')
				return('finished')

			else:
				print('''
					Sorry! You're out of tries. You look to your right and see the captain slip
					into a coma. All the while, the Liroans are closing it. Oh, no. The crew and ship is doomed. 
					The Liroans''')
				return 'death'

		if action == '3' or action == 'cloak':
			print('''
				The ship immediately becomes invisible. Everyone is safe. Your captain issues a command
				to go into warp drive, which means the ship has to temporarily decloak. Unfortunately, the
				Liroans lock on before you can go into warp drive, and fire at the ship. The Liroans...
				''')

			return('death')
 

class Death(object):		
		quips = [
			"fire their weapons, killing all of you, except for Zoe of course",
			"surround and crush you all to death, save Zoe, who becomes their queen",
			"send out a mighty blast and you all die, except for Zoe, who becomes their queen"
		]

		def enter(self):
			print(Death.quips[randint(0, len(self.quips) - 1)])	
			exit(1)


class Finished(object):
	def enter(self):
		print("You live to see another galactic day. Yay!!!")
		return('finished')


class Map(object):
	def __init__(self, start_scene):
		self.start_scene = start_scene

	scenes = {
		'bar': Bar(),
		'ship': Ship(),
		'cardgame': CardGame(),
		'death': Death(),
		'finished': Finished()
	}

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

#set a_map to Map class that calls 'bar' as first scene
a_map = Map('bar')
a_game = Engine(a_map)
a_game.play()
