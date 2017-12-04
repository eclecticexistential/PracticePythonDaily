#for importing dictionary to string
#import json
import random

#day 1 range
empty_list = []

for i in range(2000 , 2050):
    if (i % 7 == 0) and (i % 5 !=0):
        empty_list.append(str(i))

#print((','.join(empty_list)).replace(',',' '))

#day 2 math fun

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)
#print(factorial(5))

def sum(num):
    if num == 0:
        return 1
    return num + sum(num-1)

#print(sum(5))

#day 3 create a dictionary aka hashtables

# print('Enter a number:')
# n = int(input())
# d = dict()
# for i in range(1, n+1):
#     d[i] = i*i
# print(d)
#
# for i in d:
#     print("{}:{}".format(i,d[i]))
###########comment line or highlighted section with ctrl+/ ^_^!

#day 4 tuples
#tuples absolutely can not be altered once set

# values = input("Give numbers with only a comma between them:")
# list = values.split(',')
# tuple = tuple(list)
# print(list , tuple)

# for i in range(0,101):
#     d = dict()
#     for i in range(i, i+1):
#         d[i] = i*i
#         input = json.dumps("{}".format(d))
#         my_dict = json.loads(input)
#         print(tuple(my_dict.split(',')))

# my_list = "1,2,3,4,5"
# list = my_list.split(',')
# tupled = tuple(list)
# print(tupled)

#treehouse challenge to get computer to guess user's number
