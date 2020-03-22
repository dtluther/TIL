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