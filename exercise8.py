import sys

play = input("Wanna play? (yes/no)")

def game (play):
		while (play != 'no'):
			player1 = str(input("Give me either Rock, Paper, Scissors to check if you can beat Player 2: "))
			player2 = str(input("Give me either Rock, Paper, Scissors to check if you can beat Player 1: "))
			if ( player1 == player2):
				print("It's a tie")
			elif ( player1 == 'Rock'):
				if ( player2 == 'Paper'):
					print ("Player 2 wins with a Paper pick")
				else:
					print ("Player 1 wins with a Rock pick")
			elif (player1 == 'Paper'):
				if ( player2 == 'Scissors'):
					print ("Player 2 wins with a Scissors pick")
				else:
					print ("Players 1 wins with a Paper pick")
			elif (player1 == 'Scissors'):
				if (player2 == 'Rock'):
					print ("Player 2 wins with a Rock pick")
				else:
					print ("Player 1 wins with a Scissors pick")
			else:
				print ("Not  a Rock, Paper or Scissors pick, sorry")

			play = input("Wanna keep playing?")
			if ( play == 'no'):return ("Bye bye!")

print(game(play))
