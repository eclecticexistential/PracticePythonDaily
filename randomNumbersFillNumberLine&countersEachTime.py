import random

def get_random_number(x):
	numbers = [0,0,0,0,0,0,0,0,0,0]
	counter = 0
	while True:
		num = random.random()
		if num >= 0 and num < 0.5:
			if num < 0.1:
				numbers[0] = 1
			elif num >= 0.1 and num < 0.2:
				numbers[1] = 2
			elif num >= 0.2 and num < 0.3:
				numbers[2] = 3
			elif num >= 0.3 and num < 0.4:
				numbers[3] = 4
			elif num >= 0.4 and num < 0.5:
				numbers[4] = 5
		elif num >= 0.5:
			if num < 0.6:
				numbers[5] = 6
			elif num >= 0.6 and num < 0.7:
				numbers[6] = 7
			elif num >= 0.7 and num < 0.8:
				numbers[7] = 8
			elif num >= 0.8 and num < 0.9:
				numbers[8] = 9
			elif num >= 0.9 and num < 1:
				numbers[9] = 10
		counter += 1
		if counter > x:
			return numbers
			break


def find_the_perfect_amount(y,z):
	total_tries = 0
	life = [0]
	for i in range(z,y):
		check_zeros = get_random_number(i)
		for nums in check_zeros:
			if nums == 0:
				# print("New starting point {}".format(i))
				life[0] = 1
				life.append(i)
				find_the_perfect_amount(y,i+1)
				break
			elif nums != 0:
				total_tries += 1
		if total_tries ==10:
			next_num = int(str(y)+"0")
			if(next_num < 10000000000000000000000000000000000000000000):
				find_the_perfect_amount(next_num,i)
				break
			else:
				# print("Good job. {} is the required number of tries.".format(i))
				break
	return life


def get_odds(x):
	counter = 0
	while True:
		new_num = find_the_perfect_amount(10000,x)
		if new_num[0] == 0:
			continue
		elif new_num[0] == 1:
			counter += 1
			print(new_num[1])
		elif counter > 10:
			print(counter)
		else:
			print("Hi")




get_odds(80)
