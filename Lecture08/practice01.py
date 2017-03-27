#imports IntSet class from 'intset.py', and the inserts replaces the e
from intset import IntSet

a = IntSet()

a.insert(3)
a.insert(9)
a.insert(4)
a.insert(7)

a.remove(10)

print(a.member(10))
print(a.member(9))

print(a)

b = IntSet()

b.insert(4)
b.insert(7)

print(b)