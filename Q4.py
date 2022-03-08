#4. Write a Python Program to Check Armstrong Number
n = int(input("Enter any number: "))
sumn = 0
t = n
while t>0:
    di = t%10
    sumn = sumn + (di**3)
    t = t//10
if sumn == n:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")
