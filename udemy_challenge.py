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
	
	def __repr__(self):  
		return f'Deck of {len(self.cards)} cards'

	def count(self):
		return len(self.cards)

	def _deal(self, amount):
		if len(self.cards) == 0:
			raise ValueError('All cards have been dealt')
		elif amount < len(self.cards):
			cards = self.cards[:amount]
			self.cards = self.cards[amount:]
			return cards
		else:
			cards = self.cards[:len(self.cards)]
			self.cards = self.cards[len(self.cards):]
			return cards

	def shuffle(self):
		if len(self.cards) != 52:
			raise ValueError ('Only full decks can be shuffled')
		else:
			random.shuffle(self.cards)

	def deal_card(self):
		return self._deal(1)

	def deal_hand(self, amount):
		return self._deal(amount)



	






	


