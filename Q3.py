#3. Write a Python Program to Print the Fibonacci sequence
x = int(input("Enter number of terms you want to get in a Fibonacci sequence: "))
n1=0
n2=1
k = [n1,n2]
for i in range(1,x+1):
    n = n1+n2
    n1=n2
    n2=n
    k.append(n)
    if len(k) == x:
        print(f"The first {x} terms of a Fibonacci sequence are {k}")
