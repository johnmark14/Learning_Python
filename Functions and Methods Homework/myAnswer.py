# Functions and Methods Homework

# 1. Write a function that computes the volume of a sphere given its radius
print('-'*20, " Answer to Problem 1 ", '-'*20)

def vol(rad):
    #formula:

    #(4/3)*3.14159265358979*r^3
    rad = (4/3)*3.14159265358979*rad**3
    return print("%10.6f" % rad)

vol(5)

# 2. Write a function that checks whether a number is in a
#    given range (Inclusive of high and low)
print('-'*20, " Answer to Problem 2 ", '-'*20)
'''
def ran_bool(num,low,high):
    for n in range(low,high):
        if n==num:
            return True
    else:
        return False
'''

def ran_bool(num,low,high):
    return num in range(low,high)

print(ran_bool(11,1,10))

# 3. Write a Python function that accepts a string and calculate
#    the number of upper case letters and lower case letters.
print('-'*20, " Answer to Problem 3 ", '-'*20)


def up_low(s):
    d={"up":0, "low":0}
    for n in s:
        if n.islower():
            d["low"] += 1
        elif n.isupper():
            d["up"] += 1
    print("String is :",s,"\nNo. of Upper case characters : ", d["up"],  "\nNo. of Lower case characters : ", d["low"])

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")


# 4. Write a Python function that takes a list and returns a new list with
#    unique elements of the first list.
print('-'*20, " Answer to Problem 4 ", '-'*20)

sList = [1,1,1,1,2,2,3,3,3,3,4,5]

def get_distinct(original_list):
    distinct_list = []
    for each in original_list:
        if each not in distinct_list:
            distinct_list.append(each)
    return distinct_list

print(get_distinct(sList))

# Write a Python function to multiply all the numbers in a list.
print('-'*20, " Answer to Problem 5 ", '-'*20)

def multiply(numbers):
    p = numbers[0]
    for n in numbers[1:]:
        p*=n
    print(p)

list = [1,2,3,-4]

multiply(list)

# Write a Python function to check whether a string is palindrome or not
print('-'*20, " Answer to Problem 6 ", '-'*20)

def palindrome(s):
    if s == s[::-1]:
        print("palindrome (%s)" %s)
    else:
        print("not palindrome (%s)" %s)

palindrome("madam")

# HARD!!
# Write a Python function to check whether a string is pangram or not
#       Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
#       For example : "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module

print('-'*20, " Answer to Problem 7 ", '-'*20)

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    strM = set(str1.replace(" ", ""))

    if len(alphaset) <= len(strM):
        print(True)
    else:
        print(False)


ispangram("The quick brown fox jumps over a lazy dog")