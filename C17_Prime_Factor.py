def Prime_Factor(n):
    i = 2
    Factors=[]
    
    while n>1:
        if n %i==0:
          Factors.append(i)
          n = n//i
          
        else:
            i+=1
    return Factors

#Test case 1
n=30
print(Prime_Factor(n)) 

#Test case 2
n=49
print(Prime_Factor(n)) 

#Test case 3
n=19
print(Prime_Factor(n)) 

#Test case 4
n=64
print(Prime_Factor(n)) 

#Test case 5
n=123456
print(Prime_Factor(n))      