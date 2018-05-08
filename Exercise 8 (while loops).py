while 1:
	p1play = str(input("P1: Rock, Paper, or Scissors?: "))
	p2play = str(input("P2: Rock, Paper, or Scissors?: "))
	
	if p1play == "quit":
		break
	if p1play == p2play:
		print("It's a draw!")
	elif p1play == "rock" & p2play == "scissors":
		print("Player 1 Wins!")
	elif p1play == "scissors" & p2play == "rock":
		print("Player 2 Wins!")
	elif p1play == "scissors" & p2play == "paper":
		print("Player 1 Wins!")
	elif p1play == "paper" & p2play == "scissors":
		print("Player 2 Wins!")
	elif p1play == "paper" & p2play == "rock":
		print("Player 1 Wins!")
	elif p1play == "rock" & p2play == "paper":
		print("Player 1 Wins!")
	else:
		print("Invalid play!")