print('-'*20, " Methods ", '-'*20)
l = [1,2,3,4,5]
l.append(6)
print(l)
l.insert(0,0)
print(l)

print('-'*20, " Functions ", '-'*20)

# Functions that add two number the prints it
def my_Addition(arg1,arg2):
    print(arg1 + arg2)

my_Addition(10, 5)

# Functions that have a return value
def my_Multiplication(param1, param2):
    return param1 * param2

x = my_Multiplication(2, 10)
print(x)

print('-'*20)

print(2%2==0)

def my_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print('The number is not prime!')
            break
    else:
        print('The number is prime!')

my_prime(1)

print('-'*20, " Lambda Expression ", '-'*20)

reverse = lambda str: str[::-1]

print(reverse('idol'))