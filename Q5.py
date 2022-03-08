#5. Write a Python Program to Find Armstrong Number in an Interval
a = int(input("Enter lower limit of the interval: "))
b = int(input("Enter upper limit of the interval: "))
k = []
result = True
def isArmstrong(n):
    sumn = 0
    t = n
    while t>0:
        di = t%10
        sumn = sumn + di**3
        t = t//10
    if sumn == n:
        result = True
        return result
    else:
        result = False
        return result
for i in range(a,b+1):
    if isArmstrong(i) == True:
        k.append(i)
print(f"Armstrong numbers between {a} and {b} are {k}")
