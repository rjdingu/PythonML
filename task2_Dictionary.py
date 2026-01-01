# Square a dict 

def squareDict():
    d = {}
    ran = int(input("Enter a Number : "))
    for i in range(1,ran):
        d[i] = i*i

    print(d)

squareDict()


# Reverse the given DICTIONARY

def reverseDict(d):
    d2 = {}
    keys = []
    values = []
    for key,value in d.items():
        keys.append(key)
        values.append(value)

    for i in range(len(keys)):
        d2[values[i]] = keys[i]

    print(d2)

d ={1: 1, 2: 4, 3: 9, 4: 16}
reverseDict(d)

# Use reduce fuunction

from functools import reduce

def use_reduce(l):
    total = reduce(lambda x,y:x*y,l)
    print(total)

l = [1,2,3,4,5]
use_reduce(l)



# use map to do sort
def cel_to_fra(temp):
    return (temp * 1.8) + 32 
C = [94,32,12,43]
total = list(map(cel_to_fra,C))
print(total)

# use filter 

def senior_citizen(age):
    return age>=60

ages = [43,54,67,56,68,87,89,76,78,54]

senoir = list(filter(senior_citizen,ages))
print(senoir)




