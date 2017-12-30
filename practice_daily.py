#for importing dictionary to string
#import json
import random

# def even_odd(num):
#     return not num % 2
#
# start = 5
#
# while start > 0:
#     number = random.randint(1,99)
#     if even_odd(number):
#         print("{} is even".format(number))
#     else:
#         print("{} is odd".format(number))
#     start -= 1


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

# class Collab(object):
#     def __init__(self):
#         self.s = ''
#     def getString(self):
#         self.s = input('Give me a string...')
#     def printString(self):
#         print(self.s.upper())
#     def createTupleString(self):
#         thisTup = self.s.split(',')
#         tupled = tuple(thisTup)
#         print(tupled)
#     def indiLetters(self):
#         for i in self.s:
#             print(i)
#     def sDict(self):
#         stringDictionary = dict()
#         for i in self.s:
#             stringDictionary[i] = self.s
#         print(stringDictionary)
#         for wordPair in stringDictionary:
#             print("{}:{}".format(wordPair, stringDictionary[wordPair]))
#
# x = Collab()
# print(x)
#
# x.getString()
# x.printString()
# x.createTupleString()
# x.indiLetters()
# x.sDict()

# c = 50
# h = 30
# import math
# x = []
# y = [i for i in input('give me a number: ').split(',')]
# for d in y:
#     x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(x))

# def palindrome(string):
#     back_word = string[::-1]
#     if string == back_word:
#         print("yes")
#     else:
#         print("no")
#
# palindrome("redivider")

# def merge(a,b):
#     merged_dict = []
#     for item in a:
#         merged_dict.append(item)
#     for item in b:
#         merged_dict.append(item)
#     print(sorted(merged_dict, reverse=True))
#
# merge([],[])
# merge([1],[0])
# merge([7,5,1],[2])
# merge([7,8,9],[1,2,3])
# yay!

# def last_word_length(text):
#     letters=[]
#     counter = 0
#     length = len(letters)
#     back_word = text[::-1]
#     for item in text:
#         letters.append(item)
#     if len(text) > 0:
#         if letters[length-1] == " ":
#             for letter in letters:
#                 if letter != " ":
#                     counter += 1
#                 else:
#                     break
#         elif letters[length-1] != " ":
#             for letter in back_word:
#                 if letter != " ":
#                     counter += 1
#                 else:
#                     break
#     print(counter)
#
# last_word_length("")
# last_word_length("hi ")
# last_word_length("last    ")
# last_word_length('string of words')


# def find_in_sorted(nums, target):
#     new_arr = sorted(nums)
#     #go with only nums if order matters
#     counter = []
#     for i,j in enumerate(new_arr):
#         if j == target:
#             counter.append(i)
#     if len(counter) == 1:
#         print(counter[0])
#     elif nums == [] or len(counter) == 0:
#         print(-1)
#     elif len(counter) > 1:
#         length = len(counter)-1
#         print("in range({},{})".format(counter[0],counter[length]+1))
#
# find_in_sorted([],0)
# find_in_sorted([1,2,3],0)
# find_in_sorted([1,2,3],2)
# find_in_sorted([1,2,2,2,2,2,3],2)
# find_in_sorted([1,2,3,4,6,7,8,12,13,16], 12)
# find_in_sorted([1,3,2,3,4,5,3,1],3)


# def simplify_path(path):
#     new_path = ''
#     name = ''
#     for i, j in enumerate(path):
#         if i == 0 and j == '/':
#             new_path += "/"
#         elif j != "/" and j != ".":
#             name += j
#         elif i != 0 and len(name) != 0 and j == "/":
#             for x, y, z in zip(path, path[1:],path[2:]):
#                 if x == "/" and y == "/" and z == "/":
#                     new_path += name
#                     new_path += "/"
#                     name = ''
#     for x, y, z in zip(path,path[1:],path[2:]):
#         if x == "." and y == "." and z == ".":
#             new_path += "..."
#
#     print(new_path)
#
# simplify_path('/')
# simplify_path('/../')
# simplify_path('/...')
# simplify_path('/foo/..')
# simplify_path('/foo///.//bar//')

#need pull request for codekatas as max num

# num = '912583'
#
# def create_max(num,k):
#     new_array = sorted(num, reverse=True)
#     new_string = ""
#     for i in range(0,k):
#         new_string += new_array[i]
#     if int(new_string)  < int(num):
#         print(new_string)
#     else:
#         print(num)
#
#
# create_max(num,1)
# create_max(num,2)
# create_max(num,3)
# create_max(num,4)
# create_max(num,5)
# create_max(num,6)

#completed Yellow Belt!






















