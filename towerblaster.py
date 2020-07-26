import random

def intro():
	print("Welcome to Tower Blaster! Play Tower Blaster and fight the Vikings! ")
	print("Please read the following: ")
	print("1. You will be given a randomizes list of 10 ranging from 1 to 50.")
	print("2. The goal is to arrange the list from the left as the lowest and the right as the highest.")
	print("3. You will be given a top block in which you can switch one of your block with.")
	print("If you decide to not use the top block, you will be given a choice to use the random block.")
	print("However you can't see the block unless you say yes and if you say yes, you have to use it.")
	print("Good luck and beat the Vikings!!!!")

def split(complist):
	return complist[0:10], complist[10:20], complist[20:51]

def top_block1(random_block_list):
	top_block1 = random.choice(random_block_list)
	return top_block1

def ask_user1(user_blocks, random_block_list):
	first = top_block1(random_block_list)
	print("top block: ", first)
	yesorno =input("Use the top block?: ")
	block_list = []
	if yesorno.strip().lower() == "yes":
		number = input("What number to swap?: ")
		position = user_blocks.index(int(number))
		del user_blocks[position]
		user_blocks.insert(position, int(first))
		block_list.append(user_blocks)
		block_list.append(number)
		return block_list
	else: 
		nooryes =input("Use a random block?: ")
		if nooryes.strip().lower() == "yes":
			random_block = random.choice(random_block_list)
			print("random block:", random_block)
			random_block_list.append(first)
			number = input("What number to swap?: ")
			position = user_blocks.index(int(number))
			del user_blocks[position]
			user_blocks.insert(position, int(random_block))
			#return user_blocks
			block_list.append(user_blocks)
			block_list.append(number)
			return block_list
		else: 
			if nooryes.strip().lower() == "no":
				block_list.append(user_blocks)
				block_list.append(first)
				return block_list
			else:
				print("You must either use a random block or the top block") 
				exit()

def new_top_block(number):
	return number

def rep_ask_user(new_user_block, random_block_list, number):
	yesorno =input("Use the top block?: ")
	block_list = []
	if yesorno.strip().lower() == "yes":
		number2 = input("What number to swap?: ")
		position = new_user_block.index(int(number2))
		del new_user_block[position]
		new_user_block.insert(position, int(number))
		block_list.append(new_user_block)
		block_list.append(number2)
		return block_list
	else: 
		nooryes =input("Use a random block?: ")
		if nooryes.strip().lower() == "yes":
			random_block = random.choice(random_block_list)
			print("random block:", random_block)
			random_block_list.append(number)
			number = input("What number to swap?: ")
			position = new_user_block.index(int(number))
			del new_user_block[position]
			new_user_block.insert(position, int(random_block))
			#return user_blocks
			block_list.append(new_user_block)
			block_list.append(number)
			return block_list
		else: 
			if nooryes.strip().lower() == "no":
				block_list.append(new_user_block)
				block_list.append(number)
				return block_list
			else: 
				exit()


def computer(computer_blocks, number):
	if int(number) < 5: 
		position = 0
	elif int(number) >= 5 and int(number) < 10:
		position = 1
	elif int(number) >= 10 and int(number) < 15: 
		position = 2
	elif int(number) >= 15 and int(number) < 20: 
		position = 3
	elif int(number) >= 20 and int(number) < 25: 
		position = 4
	elif int(number) >= 25 and int(number) < 30: 
		position = 5
	elif int(number) >=30 and int(number) < 35: 
		position = 6
	elif int(number) >= 35 and int(number) < 40: 
		position = 7
	elif int(number) >= 40 and int(number) < 45: 
		position = 8
	elif int(number) >= 45 and int(number) <= 50: 
		position = 9
	figure = computer_blocks[position]
	del computer_blocks[position]
	computer_blocks.insert(position, int(number))
	cblocklist = []
	cblocklist.append(computer_blocks)
	cblocklist.append(figure)
	return cblocklist

def main(): 
	intro()
	complist = random.sample(range(1, 51), 50)
	user_blocks = split(complist)[0]
	computer_blocks = split(complist)[1]
	print("User's Blocks:", user_blocks)
	random_block_list = split(complist)[2]
	
	block_list = ask_user1(user_blocks, random_block_list)
	new_user_block = block_list[0]
	number = block_list[1]
	print("User's Blocks:", new_user_block)

	while (new_user_block != sorted(new_user_block)) or (computer_blocks != sorted(computer_blocks)): 
		cblocklist = computer(computer_blocks, number)
		computer_blocks = cblocklist[0]
		if computer_blocks == sorted(computer_blocks):
			print("The vikings won. You lost. :(")
			exit()
		number = cblocklist[1]
		number = new_top_block(number)
		print("top block: ", number)

		block_list = rep_ask_user(new_user_block, random_block_list, number)
		new_user_block = block_list[0]
		if new_user_block == sorted(new_user_block):
			print("YOU WIN!! :)")
			exit()
		number = block_list[1]
		print("User's Blocks:", new_user_block)
		number = (new_top_block(number))

main()

