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
#
# p = random_prime(2^512); q = random_prime(2^512)
# N = p * q
#
# a = p - ( p % 2 ^86)
#
# sage: hex(a) 'a9759e8c9fba8c0ec3e637d1e26e7b88befeb03ac199d1190' \
#              '76e3294d16ffcaef629e2937a03592895b29b0ac708e79830' \
#              '4330240bc000000000000000000000'
# RSA key recovery ... partial info
#
# X = 2^86
# M = matrix([[X^2, 2*X*a, a^2], [0, X, a], [0,0,N]])
# B = M.LLL()
#
# Q = B[0][0]*x^2/X^2+B[0][1]*x/X+B[0][2]
#
# sage: a + Q.roots(ring==ZZ)[0][0] == p
# True

#LLL algorithm to find short vector

# media.ccc.de/v/34c3-9075-latticehacks#t=951

# lattice ftw

#
# import numpy
# def primesfrom3to(n):
#     """ Returns a array of primes, 3 <= p < n """
#     sieve = numpy.ones(n/2, dtype=numpy.bool)
#     for i in xrange(3,int(n**0.5)+1,2):
#         if sieve[i/2]:
#             sieve[i*i/2::i] = False
#     return 2*numpy.nonzero(sieve)[0][1::]+1
#
# primesfrom3to(262144)


# a = [1,2,3,4]
# b = [5,6,7,8]
#
# a.append(9)
# a.extend(b)
# # print(a)
# del a[4]
# # print(a)
#
# a.insert(len(a),9)
# # print(a)

favorite_things = ["a",'b','c','d','e']
slice1 = favorite_things[:]
# print(slice1)
length = len(favorite_things)-2
slice2 = favorite_things[length:]
# print(slice2)

slice3 = favorite_things[::-1]
#
# def first_and_last_4(x):
#     y = x[:4]
#     z = x[-4:]
#     # w = y.extend(z)
#     # ^won't work
#     y.extend(z)
#     print(y)
#
# first_and_last_4(slice3)
#
# pleh = [1,2,3,4,5,6,7]
#
# def reverse_evens(p):
#     a = p[::-1]
#     b = []
#     if len(a) % 2 == 0:
#         b.extend(a[1::2])
#     elif len(a) % 2 != 0:
#         b.extend(a[0::2])
#     print(b)
#
#
#
# reverse_evens(pleh)
# pleh = [1,2,3,4,5]
# reverse_evens(pleh)

# a_list = [1,2,3]
# b_list = a_list[:]
# print(b_list)

def sillycase(x):
    length = len(x)
    if length % 2 == 0:
        d = int(length / 2)
        print("{}{}".format(x[:d].lower(),x[d:].upper()))
    elif length % 2 != 0:
        d = int((length) / 2)
        print("{}{}".format(x[:d].lower(), x[d:].upper()))

m = "justin"
i = "jessica"
s = "brad"


sillycase(m)
sillycase(i)
sillycase(s)














