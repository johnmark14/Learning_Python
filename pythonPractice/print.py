s = "Hello world"
print ('This is my string: %s' %s)

"""
Printing of Floating point numbers
"""

f = 10.5

print ('\nFloating point numbers: %1.2f' %f)

"""
If Else in Python!
"""
print("-"*20)
a = 10>10;

if a:
    print(a)
else:
    print("That's not true!")

print('-'*20)
list_ofMe = [1, 2, 3, 4, 5]
sumOfList = 0

for myList in list_ofMe:
    sumOfList += myList
    print(sumOfList)

# note that indention is a sign that statement is inside of the loop!

print(sumOfList)

# And it also work on string! nice!

thisString = "Hello this is a string!"
print("-"*20)
for myString in thisString:
    print(myString)



# Dictionary in a for loops
print('-'*10,' Dictionary in a for loops ', '-'*10)

myDictionary = {"k1":2, "k2":4, "k3":8}

print(myDictionary)
i=0
for v,k in myDictionary.items():
    print(v)
    print(k)
    i += 1
    print (i)

# Doing while Loop
print('-'*10,' Doing while Loop ', '-'*10)

print('-'*20)

i = 0

while i <=10:
    print(i)
    i+=1
else:
    print("Done i is now ", i)

print('-'*20)

x = 0
while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x+=1

# Using range
print('-'*10,' Using range ', '-'*10)
x = range(11)
print(type(x))
for r in range(5,11):
    print(r)


# List comprehension
print('-'*10,' List Comprehension ', '-'*10)
l =[]

for letter in 'word':
    l.append(letter)
    print(l)

# Comprehension is like this
print('-'*20)
lst = [lttr for lttr in 'word']

print(lst)

print('-'*20)
# square root this 8^2 for x in range(0, 10)
lst1 = [x**2 for x in range(0,10)]
print(lst1)




