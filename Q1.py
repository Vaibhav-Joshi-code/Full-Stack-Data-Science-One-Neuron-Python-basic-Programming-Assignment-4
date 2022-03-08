#1. Write a Python Program to Find the Factorial of a Number
x = int(input("Enter any number: "))
if x>0:
    prod = 1
    for i in range(x,0,-1):
        prod *= i
    print(f"Factorial of {x} is {prod}")
elif x==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial does not exist")
