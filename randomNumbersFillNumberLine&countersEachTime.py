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


def find_the_perfect_amount(y):
	life = [0]
	ran = range(y,121)
	for i in ran:
		check_zeros = get_random_number(i)
		for nums in check_zeros:
			if nums == 0:
				life[0] = 1
				if len(life) <2:
					life.append(i)
				elif len(life) >1:
					life[1] = i
				return life
	return life

def get_odds(x):
	num_zeros = 0
	counter = []
	while len(counter) < 11:
		new_num = find_the_perfect_amount(x)
		if new_num[0] == 0:
			num_zeros += 1
		elif new_num[0] == 1:
			counter.append(new_num[1])
	print(num_zeros,counter)





get_odds(80)
