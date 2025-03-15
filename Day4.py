x = {1, 2, 3, 4, 5}
lam_fun = lambda x: x ** x  # Giving some output
map_op = map(lam_fun, x)
# print(list(map_op))

# x = None
# print(x)
y = [1, 2, 3, 4, 5]
lam_fun = lambda x: x % 2 == 0  # Giving some boolean
filt_op = filter(lam_fun, y)
# print(list(filt_op))


z = [0, 1, 2, 3]
lam_fun = lambda x: True if x % 2 == 0 else False
filt_op = filter(lam_fun, z)
# print(list(filt_op))

list2 = [-1, -2, -3, 1, 2, 3, 4, 0, None, True, False, [], {}, range(0), 0.0, 0j, [1, 2, 3]]
filt_op = filter(None, list2)
# print(list(filt_op))

from itertools import *
import itertools

# from  day3 import *

f = list(filterfalse(None, list2))
# print("filter false output",f)


from functools import reduce

z = [0, 1, 2, 3]
lam_fun = lambda x: x * x
list2 = [-1, -2, -3, 1, 2, 3, 4, 0, None, True,  False, [], {}, range(0), 0.0, 0j]
x = list(map(lam_fun, list(filter(None, list2))))
# print(x)


integers  = 99999999999999999999999999999999999999999999999999999999999999999999999999999999
integers1  = -99999999999999999999999999999999999999999999999999999999999999999999999999999999
# print(type(integers1))
x = 3
y = 4

print(type(None))

# print(x+y)
# print(x-y)
# print(x*y)
# print(100/3)
# print(x//y)
# print(x%y)

# s  = float(3)
# print(s)
# print(type(s))
# a = 3 + 4j

#print(round(100/3, 3.44, 3.55))

# def round_args(*args):
#     for i in args:
#         print(round(i))
#
# round_args(2.3,4.5577, 5.688)

def round_args(*args):
    for i in args:
        print(round(i))

round_args(2.4, 3.14159, 5.6)

x = -6
print("abs function output",abs(x))








