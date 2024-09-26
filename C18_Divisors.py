def Divisor(n):
    divisor=0
    for i in range (1, n//2+1):
        if n%i==0:
            divisor+=1
    return divisor+1

#Test case 1
n=18
print(Divisor(n))

#Test case 2
n=29
print(Divisor(n))

#Test case 3
n=100
print(Divisor(n))

#Test case 4
n=1
print(Divisor(n))

#Test case 5
n=997
print(Divisor(n))

