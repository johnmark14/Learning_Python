
# Statement Assessment Test
# Lets test your knowledge

# 1. Use for, split(), and if to create a Statement that will print
#    out words that start with 's':

print('-'*10,'Answer to question number 1','-'*10)

st = 'Print only the words that start with s in this sentence'

for str in st.split():
    if str[0] == "s":
        print(str)


# 2. Use range() to print all the even numbers from 0 to 10
print('-' * 10, 'Answer to question number 2', '-' * 10)

'''
for num in range(0, 11):
    if num % 2 == 0:
        print(num)
'''

for num in range(0, 11, 2):
    print(num)

# 3. Use List comprehension to create a list of all numbers between 1 and 50
#   that are divisible by 3
print('-' * 10, 'Answer to question number 3', '-' * 10)

lst = [n for n in range(50) if n % 3 == 0]
print(lst)

# 4. Go through the string and if the length of a word is even print "even"!
print('-' * 10, 'Answer to question number 4', '-' * 10)

st = 'Print every word in this sentence that has an even number of letters'
'''
lst = [even for even in st.split() if len(even) % 2 == 0]
for lnth in lst:
    print(lnth + " ::: The length of this word is even!")
    print('-'*45)
'''

for word in st.split():
    if len(word)%2 == 0:
        print(word + " <-- has an even length!")



# 5. Write a program that prints the integers from 1 to 100. But for multiples
#    of three print "Fizz" instead of the number, and for the multiples of five
#    print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
print('-' * 10, 'Answer to question number 5', '-' * 10)
'''
Fizz = 1
Buzz = 1
for i in range(1,101):
    if i/3 == Fizz and i/5 == Buzz:
        print("FizzBuzz")
        Fizz += 1
        Buzz += 1
    elif i/3 == Fizz:
        print("Fizz")
        Fizz+=1
    elif i/5 == Buzz:
        print("Buzz")
        Buzz+=1
    else:
        print(i)
'''

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 6. Use List Comprehension to create a list of the first letters of every
#    word in the string below:
print('-' * 10, 'Answer to question number 6', '-' * 10)
st = "Create a list of the first letters of every word in this string"
'''
lst = [last[0] for last in [last for last in st.split()]]
'''

lst = [last[0] for last in st.split()]
print(lst)










