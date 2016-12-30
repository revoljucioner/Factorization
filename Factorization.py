import math
n = int(input("Введите число:"))
i=0
while i<=math.sqrt(n):
    i=i+1
    if (n%i==0):
        print(i)
        print(n/i)
