# #for importing dictionary to string
# #import json
# import random
#
# # def even_odd(num):
# #     return not num % 2
# #
# # start = 5
# #
# # while start > 0:
# #     number = random.randint(1,99)
# #     if even_odd(number):
# #         print("{} is even".format(number))
# #     else:
# #         print("{} is odd".format(number))
# #     start -= 1
#
#
# #day 1 range
# empty_list = []
#
# for i in range(2000 , 2050):
#     if (i % 7 == 0) and (i % 5 !=0):
#         empty_list.append(str(i))
#
# #print((','.join(empty_list)).replace(',',' '))
#
# #day 2 math fun
#
# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num-1)
# #print(factorial(5))
#
# def sum(num):
#     if num == 0:
#         return 1
#     return num + sum(num-1)
#
# #print(sum(5))
#
# #day 3 create a dictionary aka hashtables
#
# # print('Enter a number:')
# # n = int(input())
# # d = dict()
# # for i in range(1, n+1):
# #     d[i] = i*i
# # print(d)
# #
# # for i in d:
# #     print("{}:{}".format(i,d[i]))
# ###########comment line or highlighted section with ctrl+/ ^_^!
#
# #day 4 tuples
# #tuples absolutely can not be altered once set
#
# # values = input("Give numbers with only a comma between them:")
# # list = values.split(',')
# # tuple = tuple(list)
# # print(list , tuple)
#
# # for i in range(0,101):
# #     d = dict()
# #     for i in range(i, i+1):
# #         d[i] = i*i
# #         input = json.dumps("{}".format(d))
# #         my_dict = json.loads(input)
# #         print(tuple(my_dict.split(',')))
#
# # my_list = "1,2,3,4,5"
# # list = my_list.split(',')
# # tupled = tuple(list)
# # print(tupled)
#
# #treehouse challenge to get computer to guess user's number
#
# # class Collab(object):
# #     def __init__(self):
# #         self.s = ''
# #     def getString(self):
# #         self.s = input('Give me a string...')
# #     def printString(self):
# #         print(self.s.upper())
# #     def createTupleString(self):
# #         thisTup = self.s.split(',')
# #         tupled = tuple(thisTup)
# #         print(tupled)
# #     def indiLetters(self):
# #         for i in self.s:
# #             print(i)
# #     def sDict(self):
# #         stringDictionary = dict()
# #         for i in self.s:
# #             stringDictionary[i] = self.s
# #         print(stringDictionary)
# #         for wordPair in stringDictionary:
# #             print("{}:{}".format(wordPair, stringDictionary[wordPair]))
# #
# # x = Collab()
# # print(x)
# #
# # x.getString()
# # x.printString()
# # x.createTupleString()
# # x.indiLetters()
# # x.sDict()
#
# # c = 50
# # h = 30
# # import math
# # x = []
# # y = [i for i in input('give me a number: ').split(',')]
# # for d in y:
# #     x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# # print(','.join(x))
#
# # def palindrome(string):
# #     back_word = string[::-1]
# #     if string == back_word:
# #         print("yes")
# #     else:
# #         print("no")
# #
# # palindrome("redivider")
#
# # def merge(a,b):
# #     merged_dict = []
# #     for item in a:
# #         merged_dict.append(item)
# #     for item in b:
# #         merged_dict.append(item)
# #     print(sorted(merged_dict, reverse=True))
# #
# # merge([],[])
# # merge([1],[0])
# # merge([7,5,1],[2])
# # merge([7,8,9],[1,2,3])
# # yay!
#
# # def last_word_length(text):
# #     letters=[]
# #     counter = 0
# #     length = len(letters)
# #     back_word = text[::-1]
# #     for item in text:
# #         letters.append(item)
# #     if len(text) > 0:
# #         if letters[length-1] == " ":
# #             for letter in letters:
# #                 if letter != " ":
# #                     counter += 1
# #                 else:
# #                     break
# #         elif letters[length-1] != " ":
# #             for letter in back_word:
# #                 if letter != " ":
# #                     counter += 1
# #                 else:
# #                     break
# #     print(counter)
# #
# # last_word_length("")
# # last_word_length("hi ")
# # last_word_length("last    ")
# # last_word_length('string of words')
#
#
# # def find_in_sorted(nums, target):
# #     new_arr = sorted(nums)
# #     #go with only nums if order matters
# #     counter = []
# #     for i,j in enumerate(new_arr):
# #         if j == target:
# #             counter.append(i)
# #     if len(counter) == 1:
# #         print(counter[0])
# #     elif nums == [] or len(counter) == 0:
# #         print(-1)
# #     elif len(counter) > 1:
# #         length = len(counter)-1
# #         print("in range({},{})".format(counter[0],counter[length]+1))
# #
# # find_in_sorted([],0)
# # find_in_sorted([1,2,3],0)
# # find_in_sorted([1,2,3],2)
# # find_in_sorted([1,2,2,2,2,2,3],2)
# # find_in_sorted([1,2,3,4,6,7,8,12,13,16], 12)
# # find_in_sorted([1,3,2,3,4,5,3,1],3)
#
#
# # def simplify_path(path):
# #     new_path = ''
# #     name = ''
# #     for i, j in enumerate(path):
# #         if i == 0 and j == '/':
# #             new_path += "/"
# #         elif j != "/" and j != ".":
# #             name += j
# #         elif i != 0 and len(name) != 0 and j == "/":
# #             for x, y, z in zip(path, path[1:],path[2:]):
# #                 if x == "/" and y == "/" and z == "/":
# #                     new_path += name
# #                     new_path += "/"
# #                     name = ''
# #     for x, y, z in zip(path,path[1:],path[2:]):
# #         if x == "." and y == "." and z == ".":
# #             new_path += "..."
# #
# #     print(new_path)
# #
# # simplify_path('/')
# # simplify_path('/../')
# # simplify_path('/...')
# # simplify_path('/foo/..')
# # simplify_path('/foo///.//bar//')
#
# #need pull request for codekatas as max num
#
# # num = '912583'
# #
# # def create_max(num,k):
# #     new_array = sorted(num, reverse=True)
# #     new_string = ""
# #     for i in range(0,k):
# #         new_string += new_array[i]
# #     if int(new_string)  < int(num):
# #         print(new_string)
# #     else:
# #         print(num)
# #
# #
# # create_max(num,1)
# # create_max(num,2)
# # create_max(num,3)
# # create_max(num,4)
# # create_max(num,5)
# # create_max(num,6)
#
# #completed Yellow Belt!
# #
# # p = random_prime(2^512); q = random_prime(2^512)
# # N = p * q
# #
# # a = p - ( p % 2 ^86)
# #
# # sage: hex(a) 'a9759e8c9fba8c0ec3e637d1e26e7b88befeb03ac199d1190' \
# #              '76e3294d16ffcaef629e2937a03592895b29b0ac708e79830' \
# #              '4330240bc000000000000000000000'
# # RSA key recovery ... partial info
# #
# # X = 2^86
# # M = matrix([[X^2, 2*X*a, a^2], [0, X, a], [0,0,N]])
# # B = M.LLL()
# #
# # Q = B[0][0]*x^2/X^2+B[0][1]*x/X+B[0][2]
# #
# # sage: a + Q.roots(ring==ZZ)[0][0] == p
# # True
#
# #LLL algorithm to find short vector
#
# # media.ccc.de/v/34c3-9075-latticehacks#t=951
#
# # lattice ftw
#
# #
# # import numpy
# # def primesfrom3to(n):
# #     """ Returns a array of primes, 3 <= p < n """
# #     sieve = numpy.ones(n/2, dtype=numpy.bool)
# #     for i in xrange(3,int(n**0.5)+1,2):
# #         if sieve[i/2]:
# #             sieve[i*i/2::i] = False
# #     return 2*numpy.nonzero(sieve)[0][1::]+1
# #
# # primesfrom3to(262144)
#
#
# # a = [1,2,3,4]
# # b = [5,6,7,8]
# #
# # a.append(9)
# # a.extend(b)
# # # print(a)
# # del a[4]
# # # print(a)
# #
# # a.insert(len(a),9)
# # # print(a)
#
# favorite_things = ["a",'b','c','d','e']
# slice1 = favorite_things[:]
# # print(slice1)
# length = len(favorite_things)-2
# slice2 = favorite_things[length:]
# # print(slice2)
#
# slice3 = favorite_things[::-1]
# #
# # def first_and_last_4(x):
# #     y = x[:4]
# #     z = x[-4:]
# #     # w = y.extend(z)
# #     # ^won't work
# #     y.extend(z)
# #     print(y)
# #
# # first_and_last_4(slice3)
# #
# # pleh = [1,2,3,4,5,6,7]
# #
# # def reverse_evens(p):
# #     a = p[::-1]
# #     b = []
# #     if len(a) % 2 == 0:
# #         b.extend(a[1::2])
# #     elif len(a) % 2 != 0:
# #         b.extend(a[0::2])
# #     print(b)
# #
# #
# #
# # reverse_evens(pleh)
# # pleh = [1,2,3,4,5]
# # reverse_evens(pleh)
#
# # a_list = [1,2,3]
# # b_list = a_list[:]
# # print(b_list)
#
# # def sillycase(x):
# #     length = len(x)
# #     if length % 2 == 0:
# #         d = int(length / 2)
# #         print("{}{}".format(x[:d].lower(),x[d:].upper()))
# #     elif length % 2 != 0:
# #         d = int((length) / 2)
# #         print("{}{}".format(x[:d].lower(), x[d:].upper()))
# #
# # m = "justin"
# # i = "jessica"
# # s = "brad"
# #
# #
# # sillycase(m)
# # sillycase(i)
# # sillycase(s)
#
# # def divide(x,y):
# #     return x/y
# #
# # x,y = 5,2
# #
# # try:
# #     result = divide(x,y)
# # except ValueError:
# #     print('Invalid inputs')
# # else:
# #     print('Result is %.1f' % result)
# #
# # use % instead of format
#
# # def sort_priority(values, group):
# #     found = False
# #     def helper(x):
# #         nonlocal found
# #         if x in group:
# #             found = True
# #             return (0,x)
# #         return (1,x)
# #     values.sort(key=helper)
# #     print(values,found)
# #
# numbers = [8,3,1,2,5,4,7,6]
# group = {2,3,5,7}
# # sort_priority(numbers, group)
#
# # priorities sort order
# # *** use nonlocal to access variables outside of scope ***
# # avoid using nonlocal for larger functions and in python 2...else:
#
# # class Sorter(object):
# #     def __init__(self,group):
# #         self.group = group
# #         self.found = False
# #
# #     def __call__(self,x):
# #         if x in self.group:
# #             self.found = True
# #             return (0,x)
# #         return(1,x)
# #
# # sorter = Sorter(group)
# # numbers.sort(key=sorter)
# # assert sorter.found is True
# # # assert sorter.found is False produces AssertionError
# # print(numbers)
#
# #for python 2 instead of nonlocal use arrays:
#
# # def sort_priority(numbers,group):
# #     found = [False]
# #     def helper(x):
# #         if x in group:
# #             found[0] = True
# #             return (0,x)
# #         return (1,x)
# #     numbers.sort(key=helper)
# #     return found[0]
# #
# # print(sort_priority(numbers,group))
#
# #works with dicts, sets, and instance of class
# #
# # def index_words(text):
# #     result = []
# #     if text:
# #         result.append(0)
# #     for index, letter in enumerate(text):
# #         if letter == ' ':
# #             result.append(index+1)
# #     return result
# #
# # address = 'Four score and seven years ago...'
# # result = index_words(address)
# # print(result[:3])
# #
# # #finds the index of the first letter in a word, curtailed to 3, better one below in a generator.
# #
# # def index_words_iter(text):
# #     if text:
# #         yield 0
# #     for index, letter in enumerate(text):
# #         if letter == ' ':
# #             yield index + 1
# #
# # result = list(index_words_iter(address))
# # print(result)
#
# # import math
# #
# # pi = math.pi
# #
# # def cesaro_method_pi():
# #     times = 0
# #     one_counter = 0
# #     while times < 100:
# #         a = random.randint(0, 1000)
# #         b = random.randint(0, 1000)
# #         if math.gcd(a,b) != 1:
# #             times += 1
# #         elif math.gcd(a,b) == 1:
# #             times += 1
# #             one_counter += 1
# #     return(one_counter)
# #
# #
# # def bring_it_together():
# #     data_set = []
# #     while len(data_set) < 100000:
# #         data_set.append(cesaro_method_pi()/100)
# #     for data in data_set:
# #         if data == 6/(math.pi*math.pi):
# #             print(data)
# #
# #
# # bring_it_together()
# # Prob(gcd(n1,n2)=1) = 6/(pi*pi) cesaro's method pi
#
#
# def normalize(numbers):
#     total = sum(numbers)
#     result = []
#     for value in numbers:
#         percent = 100 * value / total
#         result.append(percent)
#     return result
#
# visits = [15,35,80]
# percentages = normalize(visits)
# print(percentages)

#can only do once with one set, otherwise StopIteration is raised and a {} will be returned instead of data
#
#add a copy of list instead inside generator *see below

# def normalize_copy(numbers):
#     numbers = list(numbers)
#     total = sum(numbers)
#     result = []
#     for value in numbers:
#         percent = 100 * value/total
#         result.append(percent)
#     return result
#
# extra copy can eat up memory....

# def normalize_func(get_iter):
#     total = sum(get_iter())
#     result = []
#     for value in get_iter():
#         percent = 100 * value / total
#         result.append(percent)
#     return result
#
# #to use normalize_fun, pass a lambda to call the generator and create a new iterator each time
#
# percentages = normalize_func(lambda: read_visits(path)))
#
#
#this can be clumsy. ergo, use an iterator protocol
# when python sees for x in foo it calls iter(foo), which is the built-in function __iter__
#this calls the __next__ function and repeats until StopIteration is waived
# to achieve this, put it in a class as a generator *see below

# class ReadVisits(object):
#     def __init__(self,data_path):
#         self.data_path = data.path
#
#     def __iter__(self):
#         with open(self.data_path) as f:
#             for line in f:
#                 yield int(line)
#
# visits = ReadVisits(path)
# percentages = normalize(visits)
# print(percentages)

# def log(message, *values):
#     if not values:
#         print(message)
#     else:
#         values_str = ", ".join(str(x) for x in values)
#         print('%s: %s' % (message, values_str))
# log("My numbers are", 1,2)
# log('Hi there') #do not have to put in values because of *
#you can use * to iter as well. *see below

# favorite_colors = ["purple","blue","green","silver"]
# print('Favorite colors:',*favorite_colors)
# print('My favorite colors are %s' % favorite_colors)
# print('Favorite colors are {}'.format(*favorite_colors)) #does only one
# print('Colors {}, {}, {}, and {}.'.format(*favorite_colors))

# def my_generator():
#     for i in range(10):
#         yield i
#
# def my_func(*args):
#     print(args)
#
# it = my_generator()
# my_func(*it)
#
# def remainder(number,divisor):
#     return number % divisor
#
# assert remainder(20,7) == 6

# import time
#
# def log(message,when=None):
#     when = time.time() if when is None else when
#     print('%s: %s' % (when,message))
#
# log("Hi there!")
# time.sleep(0.1)
# log("Hiya!")

#
# def safe_division(number, divisor, **kwargs):
#     ignore_overflow = kwargs.pop('ignore_overflow',False)
#     ignore_zero_division = kwargs.pop('ignore_zero_division', False)
#     try:
#         return number/divisor
#     except OverflowError:
#         if ignore_overflow:
#             return 0
#         else:
#             raise
#     except ZeroDivisionError:
#         if ignore_zero_division:
#             return float('inf')
#         else:
#             raise
#
# #don't have to use key= logic with python3, however, do in lower versions, this works for all...
# result = safe_division(1,10**500, ignore_overflow=True)
# print(result)
#
# result = safe_division(1,0,ignore_zero_division=True)
# print(result)

# algebra = x = (x*x) - 2
#  programming ...

# def find_x(x):
#     return (x*x)-2
#
# print("x is equal to %d" % find_x(6))

# result = map(lambda x:x**2,[1,2,3,8])
# print(list(result))

# def F(n):
#     if n==0: return 0
#     elif n== 1: return 1
#     else:
#         return F(n-1)+F(n-2)
#
# def get_fib():
#     counter = 30
#     while counter > 0:
#         number = F(counter)
#         counter -= 1
#         yield number
#
# def gen_fib():
#     x = list(get_fib())
#     print(x[::-1])
#
# gen_fib()

# mx = lambda x, y: x if x > y else y
# print(mx(10,8))
#
# n = [4,3,2,1]
# print(list(map(lambda x:x**2,n)))
# #can substitute lambda for math.sqrt
#
# print(list(filter(lambda x:x>2,n)))
# #or
# print([x for x in n if x>2])

#generators

# def square_numbers(nums):
#     for i in nums:
#         yield(i*i)
#
# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums)
#will only return the first one so do...
# for num in my_nums:
#     print(num)

#list comprehension

# my_nums = [x*x for x in [1,2,3,4,5]]
#switch first [] to () to get gen object
#or print list(my_nums)
#same results... gen better for performance

# nums = [0,1,2,3,4,5,6,7,8,9]
# #list comprehension
# my_list = [n for n in nums]
# my_list = [n*n for n in nums]
# my_list = list(map(lambda n: n*n, nums))
# my_list = [n for n in nums if n%2 == 0]
# my_list = [n for n in nums if n>1]
# my_list = list(filter(lambda n: n%2== 0, nums))
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num)) #handy way to give append 'only one' value

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
#
# print(my_list)
#
# names = ["Bruce","Clark","Peter","Logan","Wade"]
# heros = ["Batman","Superman","Spiderman","Wolverine","Deadpool"]
# # print(list(zip(names,heros)))
#
# # my_dict = {}
# # for name, hero in zip(names, heros):
# #     my_dict[name]=hero
# # print(my_dict)
#
# my_dict = {name:hero for name, hero in zip (names, heros) if name != "Peter"}
# print(my_dict)
# # list comprehension ftw!

#set is like a list but with all unique values

# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9,1]
# # my_set = set()
# # for n in nums:
# #     my_set.add(n)
# # # #sweet!
# #
# my_set = set(n for n in nums)
# # #or
# # my_set = {n for n in nums}
# #
# # print(my_set)
#
# #Generator Expressions
#
# def gen_func(my_set):
#     for n in my_set:
#         yield n*n
#
# # my_gen = gen_func(my_set)
# #or
# my_gen = (n*n for n in my_set)
#
# # for i in my_gen:
# #     print(i)
# print(list(my_gen))






