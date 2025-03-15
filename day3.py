#
#
# list = [1,2,3,4]
# print(list)
# print(id(list))
# list.append(8)
# print(list)
# print(id(list))
# list.extend([8,3,4])
# print(list)
# print(id(list))
#
#
# x = 'python'
# print(id(x))
# # x[0]='h'
# x = 'scala'
# print(id(x))

# y = {1,2,3,4,5}
# print(type(y))
# print(y)
# print(id(y))
# y.add(6)
# print(y)
# print(id(y))
#
# def add_two_num(x,y):
#     return x+y
#
def squaring(x):
    return x * x
#
# print(2+3)
#
# add_two_num(2,3)
#
# x= (lambda x,y : x+y)
#
# print("lambda func",x(2,3))
# a = 5
#
y = (lambda a : "even number" if  a%2 == 0 else "odd number" )
# print(y(5))

list1 = [1,2,3,4, 0]
list2 = list([5,6,7,8])

x = list(map(y,list1 ))
print(x)
y = (lambda a : a%2 == 0)



filt = filter(None ,list1 )
print("filter function result", list(filt))

from  functools import reduce
# list1 = [1,2,3,4,False, -1, [], "", range(0), 0.0, 0j, None, {}, (), set()]
# list2 = [1,2,3,4]
# lam = (lambda x : x*x)
# map_ex = list(map(lam, list2))
# print("map output",map_ex)
# red = reduce(lam, list2, 2)
# print(red)

list1 = [1, 2, 34, 5]
lam = (lambda x, y: x * y)
red = reduce(lam, list1, 2)
print(red)



# print(float("InFiNiTy"))
# print(float("infinity"))
# print(float("inFINity"))
# print(float("nan"))
# print(float("python"))
#
# x  = -9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# print(abs(x))
# y = (-3.456, 3.8976, 2.89377)
# print(abs(y))
# list1 = [1,2,34,45]
def print_absolute_values(*kwargs):
    for num in kwargs:
        print(abs(num))

print_absolute_values(a=4, b = -4.56)


























