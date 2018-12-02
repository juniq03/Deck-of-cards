import random

class Card:
	suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	
	def __init__(self, suit, value):
		if suit not in Card.suits:
			raise ValueError('Select "Hearts", "Diamonds", "Clubs" or "Spades"')
		if value not in Card.values:
			raise ValueError('Select "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q" or "K"') 
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	def __init__(self):
		self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
		# self._deal = 
	
	def __repr__(self):
		return f'Deck of {self.cards.count()}'

	def count(self):
		return len(self.cards)

	def _deal(self, amount):
		if self.cards.count() != 0	
			for x in range(amount):
				self.cards.pop(0)
		raise ValueError ('All cards have been dealt.')

	def shuffle(self):
		if len(self.cards) == 52: 
			return random.shuffle(self.cards)
		raise ValueError ('Only full decks can be shuffled')

first_deck = Deck()
print(first_deck.cards)
first_deck._deal(10)
print(first_deck.count())

