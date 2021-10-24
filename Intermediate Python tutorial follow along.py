import sys
import collections
import OOP_FCC_follow_along
import itertools
# from OOP_FCC_follow_along import item1
# from OOP_FCC_follow_along import Item

# functions with *arg return type tuple the other variable argument param with **arg returns a dictionary type

# print(sys.getsizeof(goes here)) this will return the size of a given objects by bytes. Lists are more memory intensive
# data structures than tuples. Tuples are almost twice as small as lists.

listy = ["abc", 32, False]
tupley = tuple(listy.copy())  # this is not the same object this works to create a new facsimile of listy you could
# also use tupley = listy[:]
tupley_2 = listy       # this points to the same object
alist = [4, 5, 6]
btuplist = tuple(alist)

if tupley is listy:
    print("yessir")
elif tupley_2 is listy:
    print("this is the same object")
if tupley is not listy:
    print("no")

if btuplist is tuple():
    print("it is")
else:
    print("no It's not")

print(sys.getsizeof(tupley), "bytes")
print(sys.getsizeof(listy), "bytes")  # tuples are more efficient to iterate over
print(btuplist)
print(alist)

# on dictionaries use pop(key name) pop item will delete the last item
# You can use a tuple as a key in a dictionary but not a list


# Sets mutable non ordered information that do not allow duplicate elements
setty = {1, 2, 2, 4}  # will not recognize duplicates
asy = set("Stringgy")  # can use set to make a string or elements an unordered set of data. When you print a set the
# order will be random and different almost every time.

asy.discard(2)  # use discard instead of remove to get rid of things from a set because it will not raise an error.
print(setty)  # this sets type will show as dictionary to make an actual set data type you must use set() function
print(asy)

if 1 in setty:
    print("Yes.")

# all the prime numbers are odd numbers but all the odd numbers are not prime numbers
# a prime number is a number which can be divisible only by itself and the number 1
# some numbers like 9 cannot be divided by 2 but can be divided by numbers other than 1 and itself
# an odd number is a number which cannot be divided by the number 2
odds = {1, 3, 5, 7}
even = {2, 4, 6, 8, 10}
primes = {1, 2, 3, 7}

u = odds.union(even)  # union combines data from 2 sets without duplication
print(u)

i = odds.intersection(even)
gi = odds.intersection(primes)
print(i)  # returns empty set because they don't have the same elements
print(gi)  # returns whatever elements intersect in a data structure
# difference function returns the difference of two sets of data; there is also symmetric_difference() which will take
# return the difference of two data sets excluding the one that intersect.
# update(); symmetric_update(); and difference(); symmetric_difference_update()
# issuperset() and issubset()
# isdisjoint(): Return True if the set has no elements in common with other. Sets are disjoint if and only if their
# intersection is the empty set.
# frozenset() is an immutable version of a set is all
sh = frozenset([1, 2, 3, 4])  # syntax of frozen set is ([])

# strings split() function's default delimitter is a ' ' whitespace in the parentheses you can change that to split on
# anything you choose
gr = "hello,ght,lol,ght"
print(gr.split("h"))
var = 65
a = "hello {age}".format(age=var)  # .format() needs a key value pair to enter
print(a)

# Collections: This is a module to use. counter, namedtuple, OrderedDict, defaultdict, deque. Special container types.
# .counter store elements as dictionary keys
a = "aaaabbaccc"
my_counter = collections.Counter(a)  # returns the items as the keys and there amount as the value
print(my_counter)
print(my_counter.most_common(2))  # returns most common elements if you put 2 it will return a list with the two most
print(list(my_counter.elements()))  # common values. .elements() prints all elements

# namedtuple from collections: literally allows to make a named tuple container
Point = collections.namedtuple("Pointer", "x, y")
pt = Point(1, -4)
print(pt.x, pt.y)

# OrderedDict and defaultdict
ordered_dict = collections.OrderedDict()
ordered_dict['a'] = 1
ordered_dict['g'] = 7
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict.values())
print(ordered_dict.keys())

d = collections.defaultdict(float)  # default t=dict returns a default type as defined in it's creation this can be int,
# float, str as well but then the values must be of that type. Could also be list type this will default to returning
# an empty list. With a normal dictionary it would raise a key error.
d['a'] = 7
d['b'] = 0.0
print(d['a'])

# deque double ended queue
p = collections.deque()
p.append(1)
p.append(2)
p.append(3)
p.appendleft(4)
p.popleft()  # regular pop cuts off the right so there is only the pop left and no pop right
print(p)

p.extend([1, 4, 5])  # this extend method needs brackets
p.extend([9, 11])
print(p)
p.rotate(8)  # rotate moves every element over by the specified spaces
print(p)
print(type(OOP_FCC_follow_along.Item))  # when imported the class returns <class 'type'>
print(type(OOP_FCC_follow_along.item1))  # this returns <class 'OOP_FCC_follow_along.Item'>
print(type(OOP_FCC_follow_along.item3))  # this returns <class 'int'>

# Itertools: products, permutations, combinations, accumulate, groupby, and some infinite iterators.
itprod = [1, 3]  # it stands for itertools -> itertools product
itprod2 = [3]
prod = itertools.product(itprod, itprod2)  # cartesian product, makes coordinates with the first list to the second.
print(list(prod))  # this returns something like this: [(1, 3), (1, 4), (2, 3), (2, 4)] you can add  : repeat=2'

# permutations:


# Lambda/Anonymous Functions


# Exceptions and Errors:


# Logging:


# JSON


# Random Numbers:


# Decorators:


# Generators: Hey Future Daniel You must do all parts listed here tomorrow.

