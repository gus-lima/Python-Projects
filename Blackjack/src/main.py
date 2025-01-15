#
import random
import os
import re

from colorama import Fore, Style, Back, just_fix_windows_console, init
just_fix_windows_console()

CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['Spade', 'Heart', 'Diamonds', 'Club']

DECK = []

PLAYER_CARDS = []
CPU_CARDS = []

#TODO: Allow player to bet
PLAYER_CHIPS = 0
CPU_CHIPS = 0

def shuffle_cards():

	for suit in SUITS:
		for card in CARDS:
			DECK.append(f'{card} - {suit}')


	random.shuffle(DECK)

	# First stage (2 cards)
	for i in range(2):
		PLAYER_CARDS.append(DECK[i])
		DECK.pop(i)
		#CPU_CARDS.append(DECK[i])
		#DECK.pop(i)

	#print(f'Player: {PLAYER_CARDS}\nCPU: {CPU_CARDS}')

def hit_action():

	if len(DECK) > 0:
		PLAYER_CARDS.append(DECK[0])
		DECK.pop(0)

#TODO: count card value
def count_card_values():
	
	#list(filter(re.compile('A').match, PLAYER_CARDS))
	pass

def main():

	init()
	os.system('cls' if os.name == 'nt' else 'clear')

	shuffle_cards()

	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		#print(f'CPU Cards: [{CPU_CARDS[0]}] | [?]')
		print('Your Cards: ', end='')
		for card in PLAYER_CARDS: 
			print(f'[{card}]', end=' ')

		print("Cards value: ", sep='')
		count_card_values()

		user_choice = input("\n\nWhat is your action?\n[1] Hit\n[2] Fold\n[3] Double - Not Implemented\n> ")

		# Hit
		if user_choice == '1':
			hit_action()

		# Fold
		elif user_choice == '2':
			pass

		# Double Down
		elif user_choice == '3':
			pass

if __name__ == "__main__":
	main()