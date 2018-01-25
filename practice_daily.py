# # #for importing dictionary to string
# # #import json
# # import random
# #
# # # def even_odd(num):
# # #     return not num % 2
# # #
# # # start = 5
# # #
# # # while start > 0:
# # #     number = random.randint(1,99)
# # #     if even_odd(number):
# # #         print("{} is even".format(number))
# # #     else:
# # #         print("{} is odd".format(number))
# # #     start -= 1
# #
# #
# # #day 1 range
# # empty_list = []
# #
# # for i in range(2000 , 2050):
# #     if (i % 7 == 0) and (i % 5 !=0):
# #         empty_list.append(str(i))
# #
# # #print((','.join(empty_list)).replace(',',' '))
# #
# # #day 2 math fun
# #
# # def factorial(num):
# #     if num == 0:
# #         return 1
# #     return num * factorial(num-1)
# # #print(factorial(5))
# #
# # def sum(num):
# #     if num == 0:
# #         return 1
# #     return num + sum(num-1)
# #
# # #print(sum(5))
# #
# # #day 3 create a dictionary aka hashtables
# #
# # # print('Enter a number:')
# # # n = int(input())
# # # d = dict()
# # # for i in range(1, n+1):
# # #     d[i] = i*i
# # # print(d)
# # #
# # # for i in d:
# # #     print("{}:{}".format(i,d[i]))
# # ###########comment line or highlighted section with ctrl+/ ^_^!
# #
# # #day 4 tuples
# # #tuples absolutely can not be altered once set
# #
# # # values = input("Give numbers with only a comma between them:")
# # # list = values.split(',')
# # # tuple = tuple(list)
# # # print(list , tuple)
# #
# # # for i in range(0,101):
# # #     d = dict()
# # #     for i in range(i, i+1):
# # #         d[i] = i*i
# # #         input = json.dumps("{}".format(d))
# # #         my_dict = json.loads(input)
# # #         print(tuple(my_dict.split(',')))
# #
# # # my_list = "1,2,3,4,5"
# # # list = my_list.split(',')
# # # tupled = tuple(list)
# # # print(tupled)
# #
# # #treehouse challenge to get computer to guess user's number
# #
# # # class Collab(object):
# # #     def __init__(self):
# # #         self.s = ''
# # #     def getString(self):
# # #         self.s = input('Give me a string...')
# # #     def printString(self):
# # #         print(self.s.upper())
# # #     def createTupleString(self):
# # #         thisTup = self.s.split(',')
# # #         tupled = tuple(thisTup)
# # #         print(tupled)
# # #     def indiLetters(self):
# # #         for i in self.s:
# # #             print(i)
# # #     def sDict(self):
# # #         stringDictionary = dict()
# # #         for i in self.s:
# # #             stringDictionary[i] = self.s
# # #         print(stringDictionary)
# # #         for wordPair in stringDictionary:
# # #             print("{}:{}".format(wordPair, stringDictionary[wordPair]))
# # #
# # # x = Collab()
# # # print(x)
# # #
# # # x.getString()
# # # x.printString()
# # # x.createTupleString()
# # # x.indiLetters()
# # # x.sDict()
# #
# # # c = 50
# # # h = 30
# # # import math
# # # x = []
# # # y = [i for i in input('give me a number: ').split(',')]
# # # for d in y:
# # #     x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# # # print(','.join(x))
# #
# # # def palindrome(string):
# # #     back_word = string[::-1]
# # #     if string == back_word:
# # #         print("yes")
# # #     else:
# # #         print("no")
# # #
# # # palindrome("redivider")
# #
# # # def merge(a,b):
# # #     merged_dict = []
# # #     for item in a:
# # #         merged_dict.append(item)
# # #     for item in b:
# # #         merged_dict.append(item)
# # #     print(sorted(merged_dict, reverse=True))
# # #
# # # merge([],[])
# # # merge([1],[0])
# # # merge([7,5,1],[2])
# # # merge([7,8,9],[1,2,3])
# # # yay!
# #
# # # def last_word_length(text):
# # #     letters=[]
# # #     counter = 0
# # #     length = len(letters)
# # #     back_word = text[::-1]
# # #     for item in text:
# # #         letters.append(item)
# # #     if len(text) > 0:
# # #         if letters[length-1] == " ":
# # #             for letter in letters:
# # #                 if letter != " ":
# # #                     counter += 1
# # #                 else:
# # #                     break
# # #         elif letters[length-1] != " ":
# # #             for letter in back_word:
# # #                 if letter != " ":
# # #                     counter += 1
# # #                 else:
# # #                     break
# # #     print(counter)
# # #
# # # last_word_length("")
# # # last_word_length("hi ")
# # # last_word_length("last    ")
# # # last_word_length('string of words')
# #
# #
# # # def find_in_sorted(nums, target):
# # #     new_arr = sorted(nums)
# # #     #go with only nums if order matters
# # #     counter = []
# # #     for i,j in enumerate(new_arr):
# # #         if j == target:
# # #             counter.append(i)
# # #     if len(counter) == 1:
# # #         print(counter[0])
# # #     elif nums == [] or len(counter) == 0:
# # #         print(-1)
# # #     elif len(counter) > 1:
# # #         length = len(counter)-1
# # #         print("in range({},{})".format(counter[0],counter[length]+1))
# # #
# # # find_in_sorted([],0)
# # # find_in_sorted([1,2,3],0)
# # # find_in_sorted([1,2,3],2)
# # # find_in_sorted([1,2,2,2,2,2,3],2)
# # # find_in_sorted([1,2,3,4,6,7,8,12,13,16], 12)
# # # find_in_sorted([1,3,2,3,4,5,3,1],3)
# #
# #
# # # def simplify_path(path):
# # #     new_path = ''
# # #     name = ''
# # #     for i, j in enumerate(path):
# # #         if i == 0 and j == '/':
# # #             new_path += "/"
# # #         elif j != "/" and j != ".":
# # #             name += j
# # #         elif i != 0 and len(name) != 0 and j == "/":
# # #             for x, y, z in zip(path, path[1:],path[2:]):
# # #                 if x == "/" and y == "/" and z == "/":
# # #                     new_path += name
# # #                     new_path += "/"
# # #                     name = ''
# # #     for x, y, z in zip(path,path[1:],path[2:]):
# # #         if x == "." and y == "." and z == ".":
# # #             new_path += "..."
# # #
# # #     print(new_path)
# # #
# # # simplify_path('/')
# # # simplify_path('/../')
# # # simplify_path('/...')
# # # simplify_path('/foo/..')
# # # simplify_path('/foo///.//bar//')
# #
# # #need pull request for codekatas as max num
# #
# # # num = '912583'
# # #
# # # def create_max(num,k):
# # #     new_array = sorted(num, reverse=True)
# # #     new_string = ""
# # #     for i in range(0,k):
# # #         new_string += new_array[i]
# # #     if int(new_string)  < int(num):
# # #         print(new_string)
# # #     else:
# # #         print(num)
# # #
# # #
# # # create_max(num,1)
# # # create_max(num,2)
# # # create_max(num,3)
# # # create_max(num,4)
# # # create_max(num,5)
# # # create_max(num,6)
# #
# # #completed Yellow Belt!
# # #
# # # p = random_prime(2^512); q = random_prime(2^512)
# # # N = p * q
# # #
# # # a = p - ( p % 2 ^86)
# # #
# # # sage: hex(a) 'a9759e8c9fba8c0ec3e637d1e26e7b88befeb03ac199d1190' \
# # #              '76e3294d16ffcaef629e2937a03592895b29b0ac708e79830' \
# # #              '4330240bc000000000000000000000'
# # # RSA key recovery ... partial info
# # #
# # # X = 2^86
# # # M = matrix([[X^2, 2*X*a, a^2], [0, X, a], [0,0,N]])
# # # B = M.LLL()
# # #
# # # Q = B[0][0]*x^2/X^2+B[0][1]*x/X+B[0][2]
# # #
# # # sage: a + Q.roots(ring==ZZ)[0][0] == p
# # # True
# #
# # #LLL algorithm to find short vector
# #
# # # media.ccc.de/v/34c3-9075-latticehacks#t=951
# #
# # # lattice ftw
# #
# # #
# # # import numpy
# # # def primesfrom3to(n):
# # #     """ Returns a array of primes, 3 <= p < n """
# # #     sieve = numpy.ones(n/2, dtype=numpy.bool)
# # #     for i in xrange(3,int(n**0.5)+1,2):
# # #         if sieve[i/2]:
# # #             sieve[i*i/2::i] = False
# # #     return 2*numpy.nonzero(sieve)[0][1::]+1
# # #
# # # primesfrom3to(262144)
# #
# #
# # # a = [1,2,3,4]
# # # b = [5,6,7,8]
# # #
# # # a.append(9)
# # # a.extend(b)
# # # # print(a)
# # # del a[4]
# # # # print(a)
# # #
# # # a.insert(len(a),9)
# # # # print(a)
# #
# # favorite_things = ["a",'b','c','d','e']
# # slice1 = favorite_things[:]
# # # print(slice1)
# # length = len(favorite_things)-2
# # slice2 = favorite_things[length:]
# # # print(slice2)
# #
# # slice3 = favorite_things[::-1]
# # #
# # # def first_and_last_4(x):
# # #     y = x[:4]
# # #     z = x[-4:]
# # #     # w = y.extend(z)
# # #     # ^won't work
# # #     y.extend(z)
# # #     print(y)
# # #
# # # first_and_last_4(slice3)
# # #
# # # pleh = [1,2,3,4,5,6,7]
# # #
# # # def reverse_evens(p):
# # #     a = p[::-1]
# # #     b = []
# # #     if len(a) % 2 == 0:
# # #         b.extend(a[1::2])
# # #     elif len(a) % 2 != 0:
# # #         b.extend(a[0::2])
# # #     print(b)
# # #
# # #
# # #
# # # reverse_evens(pleh)
# # # pleh = [1,2,3,4,5]
# # # reverse_evens(pleh)
# #
# # # a_list = [1,2,3]
# # # b_list = a_list[:]
# # # print(b_list)
# #
# # # def sillycase(x):
# # #     length = len(x)
# # #     if length % 2 == 0:
# # #         d = int(length / 2)
# # #         print("{}{}".format(x[:d].lower(),x[d:].upper()))
# # #     elif length % 2 != 0:
# # #         d = int((length) / 2)
# # #         print("{}{}".format(x[:d].lower(), x[d:].upper()))
# # #
# # # m = "justin"
# # # i = "jessica"
# # # s = "brad"
# # #
# # #
# # # sillycase(m)
# # # sillycase(i)
# # # sillycase(s)
# #
# # # def divide(x,y):
# # #     return x/y
# # #
# # # x,y = 5,2
# # #
# # # try:
# # #     result = divide(x,y)
# # # except ValueError:
# # #     print('Invalid inputs')
# # # else:
# # #     print('Result is %.1f' % result)
# # #
# # # use % instead of format
# #
# # # def sort_priority(values, group):
# # #     found = False
# # #     def helper(x):
# # #         nonlocal found
# # #         if x in group:
# # #             found = True
# # #             return (0,x)
# # #         return (1,x)
# # #     values.sort(key=helper)
# # #     print(values,found)
# # #
# # numbers = [8,3,1,2,5,4,7,6]
# # group = {2,3,5,7}
# # # sort_priority(numbers, group)
# #
# # # priorities sort order
# # # *** use nonlocal to access variables outside of scope ***
# # # avoid using nonlocal for larger functions and in python 2...else:
# #
# # # class Sorter(object):
# # #     def __init__(self,group):
# # #         self.group = group
# # #         self.found = False
# # #
# # #     def __call__(self,x):
# # #         if x in self.group:
# # #             self.found = True
# # #             return (0,x)
# # #         return(1,x)
# # #
# # # sorter = Sorter(group)
# # # numbers.sort(key=sorter)
# # # assert sorter.found is True
# # # # assert sorter.found is False produces AssertionError
# # # print(numbers)
# #
# # #for python 2 instead of nonlocal use arrays:
# #
# # # def sort_priority(numbers,group):
# # #     found = [False]
# # #     def helper(x):
# # #         if x in group:
# # #             found[0] = True
# # #             return (0,x)
# # #         return (1,x)
# # #     numbers.sort(key=helper)
# # #     return found[0]
# # #
# # # print(sort_priority(numbers,group))
# #
# # #works with dicts, sets, and instance of class
# # #
# # # def index_words(text):
# # #     result = []
# # #     if text:
# # #         result.append(0)
# # #     for index, letter in enumerate(text):
# # #         if letter == ' ':
# # #             result.append(index+1)
# # #     return result
# # #
# # # address = 'Four score and seven years ago...'
# # # result = index_words(address)
# # # print(result[:3])
# # #
# # # #finds the index of the first letter in a word, curtailed to 3, better one below in a generator.
# # #
# # # def index_words_iter(text):
# # #     if text:
# # #         yield 0
# # #     for index, letter in enumerate(text):
# # #         if letter == ' ':
# # #             yield index + 1
# # #
# # # result = list(index_words_iter(address))
# # # print(result)
# #
# # # import math
# # #
# # # pi = math.pi
# # #
# # # def cesaro_method_pi():
# # #     times = 0
# # #     one_counter = 0
# # #     while times < 100:
# # #         a = random.randint(0, 1000)
# # #         b = random.randint(0, 1000)
# # #         if math.gcd(a,b) != 1:
# # #             times += 1
# # #         elif math.gcd(a,b) == 1:
# # #             times += 1
# # #             one_counter += 1
# # #     return(one_counter)
# # #
# # #
# # # def bring_it_together():
# # #     data_set = []
# # #     while len(data_set) < 100000:
# # #         data_set.append(cesaro_method_pi()/100)
# # #     for data in data_set:
# # #         if data == 6/(math.pi*math.pi):
# # #             print(data)
# # #
# # #
# # # bring_it_together()
# # # Prob(gcd(n1,n2)=1) = 6/(pi*pi) cesaro's method pi
# #
# #
# # def normalize(numbers):
# #     total = sum(numbers)
# #     result = []
# #     for value in numbers:
# #         percent = 100 * value / total
# #         result.append(percent)
# #     return result
# #
# # visits = [15,35,80]
# # percentages = normalize(visits)
# # print(percentages)
#
# #can only do once with one set, otherwise StopIteration is raised and a {} will be returned instead of data
# #
# #add a copy of list instead inside generator *see below
#
# # def normalize_copy(numbers):
# #     numbers = list(numbers)
# #     total = sum(numbers)
# #     result = []
# #     for value in numbers:
# #         percent = 100 * value/total
# #         result.append(percent)
# #     return result
# #
# # extra copy can eat up memory....
#
# # def normalize_func(get_iter):
# #     total = sum(get_iter())
# #     result = []
# #     for value in get_iter():
# #         percent = 100 * value / total
# #         result.append(percent)
# #     return result
# #
# # #to use normalize_fun, pass a lambda to call the generator and create a new iterator each time
# #
# # percentages = normalize_func(lambda: read_visits(path)))
# #
# #
# #this can be clumsy. ergo, use an iterator protocol
# # when python sees for x in foo it calls iter(foo), which is the built-in function __iter__
# #this calls the __next__ function and repeats until StopIteration is waived
# # to achieve this, put it in a class as a generator *see below
#
# # class ReadVisits(object):
# #     def __init__(self,data_path):
# #         self.data_path = data.path
# #
# #     def __iter__(self):
# #         with open(self.data_path) as f:
# #             for line in f:
# #                 yield int(line)
# #
# # visits = ReadVisits(path)
# # percentages = normalize(visits)
# # print(percentages)
#
# # def log(message, *values):
# #     if not values:
# #         print(message)
# #     else:
# #         values_str = ", ".join(str(x) for x in values)
# #         print('%s: %s' % (message, values_str))
# # log("My numbers are", 1,2)
# # log('Hi there') #do not have to put in values because of *
# #you can use * to iter as well. *see below
#
# # favorite_colors = ["purple","blue","green","silver"]
# # print('Favorite colors:',*favorite_colors)
# # print('My favorite colors are %s' % favorite_colors)
# # print('Favorite colors are {}'.format(*favorite_colors)) #does only one
# # print('Colors {}, {}, {}, and {}.'.format(*favorite_colors))
#
# # def my_generator():
# #     for i in range(10):
# #         yield i
# #
# # def my_func(*args):
# #     print(args)
# #
# # it = my_generator()
# # my_func(*it)
# #
# # def remainder(number,divisor):
# #     return number % divisor
# #
# # assert remainder(20,7) == 6
#
# # import time
# #
# # def log(message,when=None):
# #     when = time.time() if when is None else when
# #     print('%s: %s' % (when,message))
# #
# # log("Hi there!")
# # time.sleep(0.1)
# # log("Hiya!")
#
# #
# # def safe_division(number, divisor, **kwargs):
# #     ignore_overflow = kwargs.pop('ignore_overflow',False)
# #     ignore_zero_division = kwargs.pop('ignore_zero_division', False)
# #     try:
# #         return number/divisor
# #     except OverflowError:
# #         if ignore_overflow:
# #             return 0
# #         else:
# #             raise
# #     except ZeroDivisionError:
# #         if ignore_zero_division:
# #             return float('inf')
# #         else:
# #             raise
# #
# # #don't have to use key= logic with python3, however, do in lower versions, this works for all...
# # result = safe_division(1,10**500, ignore_overflow=True)
# # print(result)
# #
# # result = safe_division(1,0,ignore_zero_division=True)
# # print(result)
#
# # algebra = x = (x*x) - 2
# #  programming ...
#
# # def find_x(x):
# #     return (x*x)-2
# #
# # print("x is equal to %d" % find_x(6))
#
# # result = map(lambda x:x**2,[1,2,3,8])
# # print(list(result))
#
# # def F(n):
# #     if n==0: return 0
# #     elif n== 1: return 1
# #     else:
# #         return F(n-1)+F(n-2)
# #
# # def get_fib():
# #     counter = 30
# #     while counter > 0:
# #         number = F(counter)
# #         counter -= 1
# #         yield number
# #
# # def gen_fib():
# #     x = list(get_fib())
# #     print(x[::-1])
# #
# # gen_fib()
#
# # mx = lambda x, y: x if x > y else y
# # print(mx(10,8))
# #
# # n = [4,3,2,1]
# # print(list(map(lambda x:x**2,n)))
# # #can substitute lambda for math.sqrt
# #
# # print(list(filter(lambda x:x>2,n)))
# # #or
# # print([x for x in n if x>2])
#
# #generators
#
# # def square_numbers(nums):
# #     for i in nums:
# #         yield(i*i)
# #
# # my_nums = square_numbers([1,2,3,4,5])
# # print(my_nums)
# #will only return the first one so do...
# # for num in my_nums:
# #     print(num)
#
# #list comprehension
#
# # my_nums = [x*x for x in [1,2,3,4,5]]
# #switch first [] to () to get gen object
# #or print list(my_nums)
# #same results... gen better for performance
#
# # nums = [0,1,2,3,4,5,6,7,8,9]
# # #list comprehension
# # my_list = [n for n in nums]
# # my_list = [n*n for n in nums]
# # my_list = list(map(lambda n: n*n, nums))
# # my_list = [n for n in nums if n%2 == 0]
# # my_list = [n for n in nums if n>1]
# # my_list = list(filter(lambda n: n%2== 0, nums))
# # my_list = []
# # for letter in 'abcd':
# #     for num in range(4):
# #         my_list.append((letter,num)) #handy way to give append 'only one' value
#
# # my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# #
# # print(my_list)
# #
# # names = ["Bruce","Clark","Peter","Logan","Wade"]
# # heros = ["Batman","Superman","Spiderman","Wolverine","Deadpool"]
# # # print(list(zip(names,heros)))
# #
# # # my_dict = {}
# # # for name, hero in zip(names, heros):
# # #     my_dict[name]=hero
# # # print(my_dict)
# #
# # my_dict = {name:hero for name, hero in zip (names, heros) if name != "Peter"}
# # print(my_dict)
# # # list comprehension ftw!
#
# #set is like a list but with all unique values
#
# # nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9,1]
# # # my_set = set()
# # # for n in nums:
# # #     my_set.add(n)
# # # # #sweet!
# # #
# # my_set = set(n for n in nums)
# # # #or
# # # my_set = {n for n in nums}
# # #
# # # print(my_set)
# #
# # #Generator Expressions
# #
# # def gen_func(my_set):
# #     for n in my_set:
# #         yield n*n
# #
# # # my_gen = gen_func(my_set)
# # #or
# # my_gen = (n*n for n in my_set)
# #
# # # for i in my_gen:
# # #     print(i)
# # print(list(my_gen))
#
# # names = {"teachers":{1:{"first_name":"Joe","last_name":"Smith"},2:{"first_name":"Tom","last_name":"Brown"}},"mentors":{1:{"first_name":"Jim","last_name":"Chill"}}}
# # print(names["teachers"][1]['first_name'])
# #
# # def get_teachers_names():
# #     for i in names["teachers"]:
# #         yield names['teachers'][i]['first_name'], names['teachers'][i]['last_name']
# #
# # print(list(get_teachers_names()))
# # del names["teachers"]
# # print(names)
# # names["teachers"] = {1:{"first_name":"Joe","last_name":"Smith"}}
# # print(names)
# # names["teachers"].update({2:{"first_name":"Tom","last_name":"Brown"}})
# # print(names)
#
# # def packer(**kwargs):
# #     print(kwargs)
# #
# #
# # packing = packer(name="Jessica",num=42,pet="Brutus",brother="Justin")
# #
# # def unpacker(first_name=None,last_name=None):
# #     if first_name and last_name:
# #         print("Hi {} {}".format(first_name,last_name))
# #     else:
# #         print("Hi no name!")
# #
# # unpacker(**{"last_name":"Norm","first_name":"Sloopy"})
#
# # template = "Hi I'm {name} and I love to eat {food}!"
# #
# # # def string_factory(x):
# # #     new = []
# # #     for i in x:
# # #         new.append(template.format(name = i['name'],food = i['food']))
# # #     print(new)
# # <3 <3 <3 <3
# # def string_factory(x):
# #     new = [ template.format(**i) for i in x]
# #     print(new)
# #
# # values = [{"name":"Michelle","food":"sushi"},{"name":"Chase","food":"cake"}]
# #
# # string_factory(values)
#
# # try_again = {"up":1,"down":0,"left":-1,"right":2}
# # # for key in try_again.keys():
# # #     print(key)
# # # for value in try_again.values():
# # #     print(value)
# #
# # for items in try_again.items():
# #     print(items)
#
# # sen = "I do not like it Sam I Am"
# #
# # def word_count(x):
# #     a = x.lower().split()
# #     d = dict.fromkeys(a,0)
# #     for word in a: d[word]+=1
# #     print(d)
# #
# # word_count(sen)
# #
# # teachers = {'A B':['jQ',"Qj"],'C D':['U1','1U','11UU'],'E F':['Bl'],'G H':['CC','DI','JJ','OO','P0']}
#
# # def num_teachers(x):
# #     counter=0
# #     for key in x.keys():
# #         counter+=1
# #     print(counter)
# #
# # num_teachers(teachers)
# #
# # def num_courses(x):
# #     counter = 0
# #     for i in x:
# #         for a in x[i]:
# #             counter+=1
# #     print(counter)
# #
# # num_courses(teachers)
#
# # def courses(x):
# #     a = []
# #     for i in x:
# #         for j in x[i]:
# #             a.append(j)
# #     print(a)
# #
# # courses(teachers)
#
# # def most_courses(x):
# #     a = {}
# #     b = []
# #     for i in x:
# #         a.update({len(x[i]):i})
# #         b.append(len(x[i]))
# #     b.sort()
# #     print(a[b[-1]])
# #
# # most_courses(teachers)
#
# # def stats(x):
# #     a = []
# #     for i in x:
# #         b = [i,len(x[i])]
# #         a.append(b)
# #     print(a)
# #
# # stats(teachers)
#
# #tuples
# #
# # def add(*nums):
# #     total = 0
# #     for num in nums:
# #         total += num
# #     return total
# #
# # print(add(5,5,5))
# #
# # def add(base,*args):
# #     total = base
# #     for num in args:
# #         total+=num
# #     return total
# #
# # print(add(5,20))
# #
# #
# # def multiply(base,*args):
# #     total = base
# #     for arg in args:
# #         total *= arg
# #     return total
# #
# # print(multiply(5,5))
#
# # course_minutes = {"Python":60,"Django":100,"Flask":190,"Java":200}
# #
# # for course,minutes in course_minutes.items():
# #     print("{} is {} minutes long".format(course,minutes))
# #
# # ages = {"George":10,"James":15,"Michelle":2,"Tabby":1,"Gigi":100}
# #
# # for name,age in ages.items():
# #     print("{} is {} years old.".format(name,age))
#
# # print(list(enumerate("abc")))
# #
# # for index,letter in enumerate("abcdefghijklmnopqrstuvwxyz",start=1):
# #     print(index,letter)
#
# # name = "jessica cottner"
#
# # def stringcases(x):
# #     up = x.upper()
# #     down = x.lower()
# #     left = ""
# #     ind = 0
# #     for index,letter in enumerate(down):
# #         if ind != 0:
# #             letter = letter.upper()
# #             ind = 0
# #         if index==0:
# #             letter = letter.upper()
# #             left+=letter
# #         elif letter == " ":
# #             ind = index+1
# #             left+=letter
# #         else:
# #             left+=letter
# #     print(left)
#
# # def stringcases(x):
# #     up = x.upper()
# #     down = x.lower()
# #     left = x.title()
# #     # left = " ".join([word[0].upper() + word[1:] for word in x.split()])
# #     right = x[::-1]
# #     ans = (up,down,left,right)
# #     print(ans)
#
#
# # stringcases(name)
#
# # L1 = [1,2,3,4]
# # L2 = ("red","blue","yellow","green")
# #
# # def combo(x,y):
# #     ans = []
# #     for index, arg in enumerate(x):
# #         for i, j in enumerate(y):
# #             if index == i:
# #                 ans.append((arg,j))
# #     print(ans)
# #
# #
# # combo(L1,L2)
# #
# # def fib(num):
# #     a,b = 0,1
# #     for i in range(0,num):
# #         yield "{}:{}".format(i+1,a)
# #         a,b = b,a+b
# #
# # for item in fib(10):
# #     print(item)
#
#
# #sets
#
# # low_primes = {1,3,5,7,11,13}
# # low_primes.add(17)
# # low_primes.update({19,23},{2,29})
# # low_primes.add(15)
# # low_primes.remove(15)
# # print(low_primes)
# # song = set(["hi","low","no"])
# # print(song)
#
# # import time
# #
# # def untap(name):
# #     print("Untap.")
# #     time.sleep(1)
# #     print("Any lands you have that can be untapped, are untapped now {}.".format(name))
# #     time.sleep(1)
# #
# # def upkeep():
# #     print("Upkeep.")
# #     time.sleep(1)
# #     print("All upkeep triggers resolve now.")
# #     time.sleep(1)
# #
# # def draw():
# #     print("Draw permitted card amount.")
# #     time.sleep(1.5)
# #
# # def main_phase():
# #     lands = input("Play land?").lower()
# #     if lands == "yes":
# #         print("Played land.")
# #     ans = input("Tap land?").lower()
# #     if ans == "yes":
# #         move = input("Play card?").lower()
# #         if move =="yes":
# #             print("Played card.")
# #         elif move == "no":
# #             print("Bruh.")
# #             return
# #     elif ans == "no":
# #         return
# #
# # def combat(name):
# #     print("Begin combat.")
# #     ans = input("Response?").lower()
# #     if ans == "yes":
# #         print("Resolve response.")
# #     elif ans == "no":
# #         print("Declare attackers.")
# #     time.sleep(0.6)
# #     attack = int(input("Number of attackers?"))
# #     ans = input("Response?").lower()
# #     if ans == "yes":
# #         print("Resolve response.")
# #     elif ans == "no":
# #         print("Declare blockers.")
# #     block = int(input("Number of blockers?"))
# #     ans = input("Response?").lower()
# #     if ans == "yes":
# #         print("Resolve response.")
# #     dam = input("Was lethal damage taken?").lower()
# #     if dam == "yes":
# #         amount = int(input("How much?"))
# #         # player = input("Player A or B?")
# #         return amount
# #     elif dam == "no" and attack == block:
# #             return 0
# #     elif dam == "no" and attack != block:
# #         ans = input("Are you sure no lethal damage was taken directly, {}?".format(name)).lower()
# #         if ans == "yes":
# #             return 0
# #         elif ans == "no":
# #             amount = input(int("How much damage got through?"))
# #             return amount
# #
# # def main_phase_two():
# #     print("Main phase two.")
# #     ans = input("Spell to do direct damage?").lower()
# #     if ans == 'yes':
# #         amount = input(int("How much?"))
# #         return amount
# #     elif ans == "no":
# #         return 0
# #
# # def end_step(name):
# #     turn(name)
# #
# # def turn(name):
# #     lifetotal = 20
# #     untap(name)
# #     upkeep()
# #     draw()
# #     main_phase()
# #     ans = input("Move to combat {}?".format(name)).lower()
# #     if ans == "yes":
# #         a = combat(name)
# #         if a != 0:
# #             lifetotal -=a
# #     b = main_phase_two()
# #     if b != 0:
# #         lifetotal -=b
# #     eot = input("Ready to end turn {}?".format(name)).lower()
# #     if eot == "yes" and lifetotal !=0:
# #         end_step(name)
# #     elif lifetotal <= 0:
# #         print("You win {}! Game Over.".format(name))
# #         return
# #
# # def play():
# #     print("Greetings!")
# #     name = input("What is your name?")
# #     print("Right on {}! Let's play!".format(name))
# #     choice = input("Play or draw?").lower()
# #     turn(name)
# #
# #
# # play()
#
# # set1 = set(range(10))
# # set2 = {1,2,3,5,7,11,13,17,19,23}
# # print(set1.union(set2))
# # print(set1,set2)
# # print(set1.difference(set2))
# # print(set2.difference(set1))
# # print(set1-set2)
# # print(set2-set1)
# # print(set1 ^ set2)
# # print(set2.symmetric_difference(set1))
# # print(set1.intersection(set2))
# # print(set1 & set2)
# # print(set1 <= set2)
# # print(set1 != set2)
#
# # courses = {
# #     "Python Basics":{"Python","functions","variables"},
# #     "Java Basics":{"Java","strings",'input','loops'},
# #     "PHP Basics":{"PHP",'variables','floats','HTML'},
# #     "Ruby Basics":{"Ruby",'strings','conditions','functions'}
# # }
# #
# # # def covers(x):
# # #     for course in courses:
# # #         if len(courses[course] & x) == len(x):
# # #             return [course]
# # # def covers(x):
# # #     solution = []
# # #     for key,value in courses.items():
# # #         if value.issuperset(x):
# # #             solution.append(key)
# # #             break
# # #     return solution
# # #
# # def covers(a):
# #     for k,v in courses.items():
# #         c = v&a
# #         if c==a:
# #             return [k]
# # def covers(x):
# #     c_list = []
# #     for i in courses:
# #         if x.intersection(courses[i]):
# #             c_list.append(i)
# #     return c_list
#
# # def covers(x):
# #     y = []
# #     for course in courses:
# #         if courses[course] & x:
# #             y.append(course)
# #     return y
#
#
# # print(covers({"Python","functions"}))
# # print(covers({'strings','input'}))
#
# # print(random.sample(range(10000000), 60))
# #
# #
# # def move(player,direction):
# #     x,y,hp = player
# #     a,b = direction
# #     x += a
# #     y += b
# #     if x < 0:
# #         x = 0
# #         hp-=5
# #     if x > 9:
# #         x = 9
# #         hp-=5
# #     if y < 0:
# #         y = 0
# #         hp-=5
# #     if y > 9:
# #         y = 9
# #         hp -= 5
# #     return x,y,hp
# #
# # # print(move((1,1,10),(-1,0)))
# # # print(move((0,1,10),(-1,0)))
# # print(move((0,9,5),(0,1)))
#
#
# # tiles = ('-',' ','-',' ','-','||',
# #          '_',"|","_","|",'_',"|",'||',
# #          '&',' ','_',' ','||',
# #          ' ', ' ', ' ', '^', ' ','||')
# #
# #
# # for tile in tiles:
# #     if tile != "||":
# #         print(tile,end="")
# #     else:
# #         print()
#
# # class Student:
# #     def __init__(self, name, **kwargs):
# #         self.name = name
# #         for key, value in kwargs.items():
# #             setattr(self, key, value)
# #
# # jessica = Student("Jessica", has_pet=True, has_mate=False)
# #
# # print(jessica.has_pet)
#
# # class RaceCar:
# #     def __init__(self, color, fuel_remaining, **kwargs):
# #         self.color =  color
# #         self.fuel_remaining = fuel_remaining
# #         self.laps = 0
# #         for key, value in kwargs.items():
# #             setattr(self, key, value)
# #     def run_lap(self, length):
# #         self.fuel_remaining -= length * 0.125
# #         self.laps += 1
# #         print(self.laps)
# #
# #
# # beatbox = RaceCar("red", 100)
# #
# # class Fruit:
# #     def __init__(self, has_pulp=False, has_rind=False, juicy=True, **kwargs):
# #         self.has_pulp = has_pulp
# #         self.has_rind = has_rind
# #         self.juicy = juicy
# #         for key, value in kwargs.items():
# #             setattr(self, key, value)
# #
# # class Orange(Fruit):
# #
# #     def __init__(self, has_pulp=True, has_rind=True):
# #         super().__init__(has_pulp, has_rind)
# #         self.has_pulp = has_pulp
# #         self.has_rind = has_rind
# #
# #     def describe(self):
# #         print("Fruit has pulp {}, has rind {}, and is juicy {}.".format(self.has_pulp, self.has_rind, self.juicy))
# #
# # tangerine = Orange()
# # tangerine.describe()
#
# # def combiner(x):
# #     s = ""
# #     n = 0
# #     for i in x:
# #         if isinstance(i, (int, float)):
# #             n += i
# #         elif isinstance(i, str):
# #             s += i
# #     s += str(n)
# #     print(s)
# #
# # combiner(["apple", 5.2, "dog", 8])
# #
# #
# # def morse(x):
# #     string = []
# #     for h, i in enumerate(x):
# #         if i == '.':
# #             string.append("dot")
# #         elif i == "_":
# #             string.append("dash")
# #     print("-".join(string))
# #
# #
# # morse("...")
#
# # class Book:
# #     def __init__(self, title, author):
# #         self.title = title
# #         self. author = author
# #     def __str__(self):
# #         return '{} by {}'.format(self.title, self.author)
# #
# # class Bookcase:
# #     def __init__(self, books=None):
# #         self.books = books
# #
# #     @classmethod
# #     def create_bookcase(cls, book_list):
# #         books = []
# #         for title, author in book_list:
# #             books.append(Book(title, author))
# #         return cls(books)
# #
# # bc = Bookcase.create_bookcase([("The Giver", "Lois Lowry"),("Live", "United")])
# # print(str(bc.books[0]))
#
# # def from_string(str):
# #     new_str = str.split('-')
# #     output = []
# #     for sym in new_str:
# #         if sym == "Hugs":
# #             output.append('_')
# #         elif sym == "Smile":
# #             output.append('.')
# #     print(output)
# #
# # from_string("Hugs-Smile")
#
# # class Circle:
# #     def __init__(self, diameter):
# #         self.diameter = diameter
# #
# #     @property
# #     def radius(self):
# #         return self.diameter / 2
# #
# #     @radius.setter
# #     def radius(self, radius):
# #         self.diameter = radius * 2
# #
# # small = Circle(10)
# # print(str(small.diameter))
# # print(str(small.radius))
# # small.radius = 10
# # print(str(small.diameter))
#
# # class Item:
# #     def __init__(self, name, description):
# #         self.name = name
# #         self.description = description
# #
# # class Weapon:
# #     def __init__(self, name, description, damage):
# #         self.damage = damage
# #         self.name = name
# #         self.description = description
# #
# # class Inventory:
# #     def __init__(self):
# #         self.slots = []
# #
# #     def add(self, item):
# #         self.slots.append(item)
# #
# #     def __len__(self):
# #         return len(self.slots)
# #
# #     def __contains__(self, item):
# #         return item in self.slots
# #
# #     def __iter__(self):
# #         for i in self.slots:
# #             yield i
# #     # or yield from self.slots
# #
# # coin = Item('coin', 'a gold coin')
# # inventory = Inventory()
# # inventory.add(coin)
# # print(len(inventory))
# # sword = Weapon('sword', 'sharp', 40)
# # inventory.add(sword)
# # print(sword in inventory)
# # for item in inventory:
# #     print(item.description)
#
# # class ReversedStr(str):
# #     def __new__(*args, **kwargs):
# #         self = str.__new__(*args, **kwargs)
# #         self = self[::-1]
# #         return self
# #
# # rs = ReversedStr("Brutus")
# # print(rs)
#
# # import copy
# #
# # class FilledList(list):
# #     def __init__(self, count, value, *args, **kwargs):
# #         super().__init__()
# #         for _ in range(count):
# #             self.append(copy.copy(value))
# #             #makes sure that reference is not repeated as it is a copy of original
# #
# # fl = FilledList(9, 4)
# # print(len(fl))
# # print(fl)
# # fl2 = FilledList(2, [1,2,3])
# # print(fl2)
# # fl2[0][1] = 5
# # print(fl2)
#
# # class JavascriptObject(dict):
# #     def __getattribute__(self, item):
# #         try:
# #             return self[item]
# #         except KeyError:
# #             return super().__getattribute__(item)
# #
# # jso = JavascriptObject({'name': 'Jessica'})
# # jso.language = 'Python'
# # print(jso.name)
# # print(jso.language)
# # print(jso.fake)
# #
# import random
#
#
# class Die:
#     def __init__(self, sides=2, value=0):
#         if not sides >= 2:
#             raise ValueError("Must have at least 2 sides")
#         if not isinstance(sides, int):
#             raise ValueError("Sides must be a whole number")
#         self.value = value or random.randint(1, sides)
#
#     def __int__(self):
#         return self.value
#
#     def __eq__(self, other):
#         return int(self) == other
#
#     def __ne__(self, other):
#         return int(self) != other
#
#     def __gt__(self, other):
#         return int(self) > other
#
#     def __lt__(self, other):
#         return int(self) < other
#
#     def __ge__(self, other):
#         return int(self) > other or int(self) == other
#
#     def __le__(self, other):
#         return int(self) < other or int(self) == other
#
#     def __add__(self, other):
#         return int(self) + other
#
#     def __radd__(self, other):
#         return int(self) + other
#
#     def __repr__(self):
#         return str(self.value)
#
# class D6(Die):
#     def __int__(self, value=0):
#         super().__init__(sides=6, value=value)
#
#
# d = Die(6)
# print(d)
# d1 = D6()
# print(d1)
#
#
# class Hand(list):
#     def __init__(self, size=0, die_class=None, *args, **kwargs):
#         if not die_class:
#             raise ValueError("You must provide a die class")
#         super().__init__()
#
#         for _ in range(size):
#             self.append(die_class())
#
#     def _by_value(self, value):
#         dice = []
#         for die in self:
#             if die == value:
#                 dice.append(die)
#         return dice
#
# class YatzyHand(Hand):
#     def __init__(self, *args, **kwargs):
#         super().__init__(size=5, die_class=D6, *args, **kwargs)
#
#     @property
#     def ones(self):
#         return self._by_value(1)
#
#     @property
#     def twos(self):
#         return self._by_value(2)
#
#     @property
#     def threes(self):
#         return self._by_value(3)
#
#     @property
#     def fours(self):
#         return self._by_value(4)
#
#     @property
#     def fives(self):
#         return self._by_value(5)
#
#     @property
#     def sixes(self):
#         return self._by_value(6)
#
#     @property
#     def _sets(self):
#         return {
#             1: len(self.ones),
#             2: len(self.twos),
#             3: len(self.threes),
#             4: len(self.fours),
#             5: len(self.fives),
#             6: len(self.sixes)
#         }
#
# hand = Hand(size=5, die_class=D6)
#
# yh = YatzyHand()
# print(yh)
#
# class YatzyScoresheet:
#     def scores_ones(self, hand):
#         return sum(hand.ones)
#
#     def _score_set(self, hand, set_size):
#         scores = [0]
#         for worth, count in hand._sets.item():
#             if count == set_size:
#                 scores.append(worth*set_size)
#         return max(scores)
#
#     def score_one_pair(self, hand):
#         return self._score_set(hand, 2)
#
# three = D6(value=3)
# four = D6(value=4)
# one = D6(value=1)
# # hand[:] = [one, three, three, four, four]
# YatzyScoresheet().score_one_pair(yh)
#
# # class Board:
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height
# #         self.cells = []
# #         for y in range(self.height):
# #             for x in range(self.width):
# #                 self.cells.append((x, y))
# #
# #     def __iter__(self):
# #         for cell in self.cells:
# #             yield cell
# #
# # class TicTacToe(Board):
# #     def __init__(self):
# #         super().__init__(width=3, height=3)
# #
# # b = Board(3, 3)
# # print(list(b))
# # a = TicTacToe()
# #
# # class Die:
# #     def __init__(self, sides=2):
# #         if sides < 2:
# #             raise ValueError("Can't have fewer than two sides")
# #         self.sides = sides
# #         self.value = random.randint(1, sides)
# #
# #     def __int__(self):
# #         return self.value
# #
# #     def __add__(self, other):
# #         return int(self) + other
# #
# #     def __radd__(self, other):
# #         return int(self) + other
# #
# #
# # class D20(Die):
# #     def __init__(self):
# #         super().__init__(sides=20)
# #
# # class Hand(list):
# #     def __init__(self, rolls=0, die_class=D20):
# #         super().__init__()
# #         for _ in range(rolls):
# #             self.append(die_class())
# #
# #     @classmethod
# #     def roll(cls, rolls):
# #         return cls(rolls=rolls)
# #
# #     @property
# #     def total(self):
# #         return sum(self)
# #
# # h = Hand()
# # b = D20()
# # c = Hand.roll(2)
# # print(c.total)
# # print(int(b))

import math, random

class Mana:
    def __init__(self, land_type=1, num_lands=17, evo=0):
        if land_type < 1:
            raise ValueError("Only super secret decks can run with no mana.")
        self.land_type = land_type
        self.num_lands = num_lands
        self.evo = evo
        self.mana = []
        self.totals = math.floor(num_lands / land_type)
        m_types = [2, 3, 4, 5, 6]
        for z in range(evo):
            self.mana.append(10)
        for y in range(self.land_type):
            for x in range(self.totals-1):
                self.mana.append(m_types[y])
        while len(self.mana) != num_lands:
            rando = random.randint(0, self.land_type-1)
            self.mana.append(m_types[rando])

    def __iter__(self):
        for lands in self.mana:
            yield lands


class Spells:
    def __init__(self, removal=4, life_gain=1, tutor=2, draw_cards=1, combat_tricks=4):
        self.total_spells = {33: removal, 9: life_gain, 66: tutor, 42: draw_cards, 7: combat_tricks}
        if removal < 0 or life_gain < 0 or tutor < 0 or draw_cards < 0:
            raise ValueError("You're going to need a positive number of spells.")
        self.removal = removal
        self.life_gain = life_gain
        self.tutor = tutor
        self.draw_cards = draw_cards
        self.combat_tricks = combat_tricks
        self.spells = []
        for value in self.total_spells:
            for _ in range(self.total_spells[value]):
                self.spells.append(value)

    def __iter__(self):
        for spells in self.spells:
            yield spells


class Creatures:
    def __init__(self, lil=9, bombs=2):
        if lil < 5 or bombs < 1:
            raise ValueError("You're going to need some creatures")
        self.lil = lil
        self.bombs = bombs
        self.total_creatures = {8: lil, 88: bombs}
        self.creatures = []
        for value in self.total_creatures:
            for _ in range(self.total_creatures[value]):
                self.creatures.append(value)

    def __iter__(self):
        for creatures in self.creatures:
            yield creatures


class Deck:
    def __init__(self, total_cards=40, mana=Mana(), spells=Spells(), creatures=Creatures()):
        if total_cards < 40:
            raise ValueError("40 is the lowest card amount in all formats.")
        self.total_cards = total_cards
        self.mana = mana
        self.spells = spells
        self.creatures = creatures
        self.cards = []
        self.cards.extend(mana)
        self.cards.extend(spells)
        self.cards.extend(creatures)

        if len(self.cards) < self.total_cards:
            raise ValueError("Check total card count.")

    @property
    def total(self):
        random.shuffle(self.cards)
        return self.cards


# evo = Deck(mana=Mana(land_type=2, evo=3))
# print(evo.total)
# deck1 = Deck()
# print(deck1.total)
# non_evo = Deck(mana=Mana(evo=2))
# print(non_evo.total)
# pyodbc
# pdb bugger
# deck2 = Deck(60, mana=Mana(land_type=2, num_lands=26), spells=Spells(removal=6, life_gain=0, draw_cards=4, combat_tricks=6), creatures=Creatures(lil=13, bombs=4))
# print(deck2.total)

# import random
#
# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides
#         self.roll = random.randint(1, self.sides)
#
#     def __iter__(self):
#         yield self.roll
#
# a = Die()
# print(a.roll)
#
# class C:
#     def __init__(self, size=2):
#         self.size = size
#         self.rolls = []
#         for _ in range(size):
#             a = Die()
#             self.rolls.append(int(a.roll))
#
#     def __iter__(self):
#         yield self.rolls
#
# c = C()
# print(c.rolls)































