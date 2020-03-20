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