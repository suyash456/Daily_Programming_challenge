def LCM(N,M):
    max_num = max(N,M)
    
    while(True):
        if (max_num%N==0 and max_num%M==0):
            break
        max_num +=1 
    return max_num

#Test case 1
N=4
M=6
print(f"The LCM is {LCM(N,M)}")

#Test case 2
N=5
M=10
print(f"The LCM is {LCM(N,M)}")

#Test case 3
N=7
M=3
print(f"The LCM is {LCM(N,M)}")

#Test case 4
N=1
M=987654321
print(f"The LCM is {LCM(N,M)}")

#Test case 5
N=123456
M=789012
print(f"The LCM is {LCM(N,M)}")