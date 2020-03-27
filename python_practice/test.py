# print('hello_world')

# a, b = 0, 1
# while a < 1000:
#     print(a)
#     a, b = b, a+b

# ### if statements
# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero:', x)
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# ### for statements
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# ### to iterate over the indices of a sequence WITHOUT `enumerate`
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# ### break and continue statements, and else clausesd on loops
# ## break breaks out of the innermost enclosing for or while loop
# ## an else clause run when no break occurs (feels more similar to an else clause in a try statement)
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break # exits the for loop with the else
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# ## the continue statement continues with the next iteration of the for/while loop
# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found a number", num)

# ### Defining functions
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end = ' ')
#         a, b = b, a+b
#     print()
# fib(2000)

# f = fib
# fib(10)

# print(fib)
# print(fib(100))

# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result

# f100 = fib2(100)
# print(f100)


# ### Default Argument Values
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         elif ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# # ask_ok('Do you really want to quit? ')
# # ask_ok('OK to overwrite the file? ', 2)
# ask_ok('OK to overwrite the file? ', 2, 'Come on, only yes or no!')

# i = 5
# def f(arg=i):
#     print(arg)

# i = 6
# f() # default values are evaluated at the point of function definition in the defining scope

# ## The default value is evaluated only once, so the following
# ## function accumulates the arguments passed to it on subsequent calls:
# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# ## If we don't want the default shared between subsequent calls,
# ## write it with the default value none and assign the list (array) in the function
# def f2(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f2(1))
# print(f2(2))
# print(f2(3))

# ### 4.7.2 Keyword arguments
# ## Keyword args must follow positional args)
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     # This has 1 required argument and 3 optional args
#     print("-- This parrot wouldn't", action, end=' ') # space instead of newline (\n)
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# # These below all work
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# # The following are all invalid
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

# ### *name and **names paramaters
# ## **name receives a dictionary
# ## *name receives a tuple
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")
# # Output:
# # -- Do you have any Limburger ?
# # -- I'm sorry, we're all out of Limburger
# # It's very runny, sir.
# # It's really very, VERY runny, sir.
# # ----------------------------------------
# # shopkeeper : Michael Palin
# # client : John Cleese
# # sketch : Cheese Shop Sketch

# ######## Python 3.8+ #########
# ## Special parameters
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only

# # / and * are optional, and they indicate the kinds of parameters
# # if no / or *, args may be passed by position or by keyword
# # Positional-only are placed before / (if no /, no positional-only params)
# # params after / may be positional-or-keyword or keyword-only
# # Keyword-only are placed after the *

# def standard_arg(arg):
#     print(arg)

# standard_arg(2)                         # positional param OR
# standard_arg(arg=2)                     # keyword arg

# def pos_only_arg(arg, /):
#     print(arg)

# pos_only_arg(1)                         # positional-only
# # pos_only_arg(arg=1) # this breaks

# def kwd_only_arg(*, arg):
#     print(arg)

# # kwd_only_arg(3) # this breaks
# kwd_only_arg(arg=3)                         # keyword-only

# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)

# >>> combined_example(1, 2, 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: combined_example() takes 2 positional arguments but 3 were given

# >>> combined_example(1, 2, kwd_only=3)
# 1 2 3

# >>> combined_example(1, standard=2, kwd_only=3)
# 1 2 3

# >>> combined_example(pos_only=1, standard=2, kwd_only=3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: combined_example() got an unexpected keyword argument 'pos_only'

# ######## Python 3.8+ closed #########

# ### 4.7.3 Arbitrary Argument Lists
# ## these arguments will be wrapped in a tuple after the normal arguments

# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))
# # >>> def concat(*args, sep="/"):
# # ...     return sep.join(args)
# # ...
# # >>> concat("earth", "mars", "venus")
# # 'earth/mars/venus'
# # >>> concat("earth", "mars", "venus", sep=".")
# # 'earth.mars.venus'

# ### 4.7.4 Unpacking Argument Lists
# ## * will unpack arguments our of a list or tuple
# # print(list(range(3, 6)))            # normal call with separate arguments
# # args = [3, 6]
# # print(list(range(*args)))           # call with arguments unpacked from a list

# ## ** will unpack arguments out of a dictionary
# # def parrot(voltage, state='a stiff', action='voom'):
# #     print("-- This parrot wouldn't", action, end=' ')
# #     print("if you put", voltage, "volts through it.", end=' ')
# #     print("E's", state, "!")

# # d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# # parrot(**d)

# ### 4.7.5 Lambda Expressions
# def make_incrementor(n):
#     return lambda x: x + n

# ## Uses a lambda expression to return a function
# f = make_incrementor(42)
# print(f(0))
# print(f(1))

# ## Another use is to pass a small function as an argument
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# ### 4.7.6 Documentation Strings
# def my_function():
#     """Do nothing, but document it.

#     No, really, it doesn't do anything.
#     """
#     pass

# print(my_function.__doc__)

# #### 5 Data Structures ####
# ### 5.1.3 List comprehensions
# ## consists of brackets containing an expression followed by a
# ## for clause, then zero or more for or if clauses, and outputs a new list
# squares = [x**2 for x in range(10)]
# print(squares)

# print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# vec = [-4, -2, 0, 2, 4]
# print([x*2 for x in vec])
# ## filtering
# print([x for x in vec if x >= 0])
# ## apply function to all elements
# print([abs(x) for x in vec])

# ## call a method on each element
# freshfruit = ['banana', '  cherry', 'orange']
# print([fruit.strip() for fruit in freshfruit])

# ## create a list of 2-tuples like (number, square)
# print([(x, x**2) for x in range(6)])

# ## flatten a list usinga listcomp with two 'for's
# vec2 = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec2 for num in elem])

# ## can also contain complex expressions and nested functions
# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])

# ### 5.1.4 Nested List Comprehensions
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# ## transpose
# print([[row[i] for row in matrix] for i in range(4)])
# ## The nested listcomp is evaluated in the context of the following for, so
# ## this is equivalent to:
# ## >>> transposed = []
# ## >>> for i in range(4):
# ## ...     transposed.append([row[i] for row in matrix])

# print(list(zip(*matrix)))

# ### 5.3 Tuples and Sequences
# ## tuples are immutable and consist of a number of values separated by commas
# ## HOWEVER, it's possible to have tuples that contain mutable objects, like lists
# t = 1235, 54321, 'hello'
# print(type(t))
# print(t[0])

# ## immutable
# t[0] = 88888
# # >>> Traceback (most recent call last):
# # ...   File "test.py", line 334, in <module>
# # ...     t[0] = 88888
# # ... TypeError: 'tuple' object does not support item assignment

# ## empty tuple
# empty = ()
# print(len(empty))
# ## singleton
# singleton = 'hello',    # <-- note trailing comma
# print(len(singleton))
# print(singleton)

# t2 = 1, 2, 'test', 'tuple'      # <-- tuple packing
# a, b, c, d = t2                 # <-- unpacking the tuple (or any sequence)
# print(a, b, c, d)

# ### 5.4 Sets
# ## to create an empty set, must use set(), not {} (that's an empty dictionary)
# basket = {'apple', 'orange', 'apple', 'orange', 'pear', 'banana'}

# print(basket)                   # automatically removed duplicates
# print('orange' in basket)       # fast membership testing
# print('crabgrass' in basket)

# a = set('abracadabra')
# b = set('alacazam')

# print(a)                        # unique letters in a
# print(a - b)                    # letters in a but not in b
# print(a | b)                    # union (letters in a or b or both)
# print(a & b)                    # intersection (letters in both a and b)
# print(a ^ b)                    # letters in a or b but NOT both

# ## set comprehensions are also supported
# print({x for x in 'abracadabra' if x not in 'abc'})


# ### 5.5 Dictionaries
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print(tel)
# print(tel['jack'])

# del tel['sape']
# tel['irv'] = 4127
# print(tel)

# print(list(tel))

# print(sorted(tel))

# print('guido' in tel)
# print('jack' not in tel)

# d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(d)

# ## also dict comprehensions can be created
# d2 = {x: x**2 for x in (2, 4, 6)}
# print(d2)

# ## when the keys are simplestrings, can specify pairs using keyword arguments
# d3 = dict(sape=4139, guido=4127, jack=4098)
# print(d3)

# ### 5.6 Looping Techniques
# ## when looping through dicts, items() method retrives the key and corredpsonding value
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# ## when looping through a sequence, enumerate() gives position index and value
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# ## to loop over 2+ sequences simultaneously, entries can be paired with zip()
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}? it is {1}.'.format(q,a))

#### 7 Input and Output ####
### Fancier Output Formatting
## formatted string literal
# year = 2016
# event = 'Referendum'
# print(f'Results of the {year} {event}')

# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)
# print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

# s = 'Hello, world.'
# print(str(s))
# print(repr(s))

# print(str(1/7))

# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' +  repr(y) + '...'
# print(s)

# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)

# # The argument to repr() may be any Python object:
# print(repr((x, y, ('spam', 'eggs'))))

# ### 7.1.1 Formatted String Literals
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# ## passing an integer after the ':' makes the field that minimum number of characters wide:
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')
# # >>> Sjoerd     ==>       4127
# # >>> Jack       ==>       4098
# # >>> Dcab       ==>       7678

# ## '!a' applies asciii(), '!s' applies str(), and '!r' applies repr()
# animals = 'eels'
# print(f'My hovercraft is full of {animals}.')
# print(f'My hovercraft is full of {animals!r}.')

# ### 7.1.2 The String format() Method
# print('We are the {} who say "{}"!'.format('knights', 'Ni'))

# ## a number in the brackets refers to position of the objects passed in
# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))

# ## can also use keyword arguments
# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# ## can arbitrarily combine the two
# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='George'))

# ## can pass in a dict and use square brackets to access the keys
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
#       'Dcab: {0[Dcab]:d}'.format(table))
# ## can also use the ** notation
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# ### 7.1.3 Manual String Formatting
# ## same table as above with squares and cubes, but formatted manually:
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end = ' ')
#     # note use of 'end' on previous line
#     print(repr(x*x*x).rjust(4))

# for x in range(1, 11):
#     print(repr(x).center(2), repr(x*x).center(3), end = ' ')
#     # note use of 'end' on previous line
#     print(repr(x*x*x).center(4))

# ## zfill pads 0s on the left, and understand + and - signs
# '-3.14'.zfill(7)
# for x in range(1, 11):
#     print(repr(x).zfill(2), repr(x*x).zfill(3), end = ' ')
#     # note use of 'end' on previous line
#     print(repr(x*x*x).zfill(4))

### 7.2 Reading and Writing Files (also JSON stuff)

#### 8. Errors and Exceptiond
## Syntax errors are also known as parsing errors, and happen before execution

### 8.2 Exceptions
## Errors detected during execution are exceptions

### 8.3 Handling Exceptions
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")

# class B(Exception):
#     pass

# class C(B):             # subclass of B
#     pass

# class D(C):             # subclass of C
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# ## a class in an except clause is compatible if it's the same or it's a base class thereof
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except B:           # each derived class will trigger this, so it will never hit the derived classes
#         print("B")
#     except D:
#         print("D")
#     except C:
#         print("C")

# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:         # CAREFUL, this last open except serves as a wildcard, which can mask a real programming error
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

## There is an optional else clause, which must come last.
## It is useful for code that must be executed if no exception is raised in the try clause
## The else cause is better than adding to to the try clause because it avoids
## accidentally catching an exception that wasn't raised by the code being protected
## by the try... except statement.
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()