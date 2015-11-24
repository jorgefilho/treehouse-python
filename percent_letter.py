user_string = input("What's your word? ")
user_number = input("What's your number? ")


try:
	our_num = int(user_number)
except:
	our_num = float(user_number)

if not '.' in user_number:
	print(user_string[our_num])
else:
	ratio = round(len(user_string)*our_num)
	print(user_string[ratio])