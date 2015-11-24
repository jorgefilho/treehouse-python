import random

rand_num = random.randint(1, 10)
guessed_nums = []
allowed_guesses = 5

while len(guessed_nums) < allowed_guesses:
	guess = input("Guess a number between 1 and 10: ")

	try:
		player_number = int(guess)
	except:
		print("That's not a whole number !")
		break

	if not player_number > 0 or not player_number < 11:
		print("That number ins't between 1 and 10!")
		break

	guessed_nums.append(player_number)

	if player_number == rand_num:
		print("You win! My number was {}.".format(rand_num))
		print("It took you {} tries.".format(guessed_nums))
		break
	else:
		if rand_num > player_number:
			print("Nope! My number is higher than {}. Guess #{}".format(player_number, len(guessed_nums)))
		else:
			print("Nope! My number is lower than {}. Guess #{}".format(player_number, len(guessed_nums)))	
		continue

if not rand_num in guessed_nums:
	print("Sorry! My number was {}.".format(rand_num))