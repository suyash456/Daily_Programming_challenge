def Find_leader(arr):
    res=[]
    n= len(arr)
    Max = arr[n-1]
    res.append(Max)
    for i in range(n-2 ,-1,-1):
        if arr[i]>Max:
            res.append(arr[i])
            Max = arr[i]
    return res[::-1]
    
#test case1 
arr =[16, 17, 4, 3, 5, 2]
print("Leaders:",Find_leader(arr))

#test case2 
arr =[1, 2, 3, 4, 0]
print("Leaders:",Find_leader(arr))

#test case3
arr = [7, 10, 4, 10, 6, 5, 2]
print("Leaders:",Find_leader(arr))

#test case4
arr =[100, 50, 20, 10]
print("Leaders:",Find_leader(arr))

#test case5
arr =[5]
print("Leaders:",Find_leader(arr))