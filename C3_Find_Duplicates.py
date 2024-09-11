def Find_duplicates(arr):
    res=[]
    for i in range(len(arr)):
        index = abs(arr[i])-1
        if arr[index]<0:
            res.append(abs(arr[i]))
        else:
            arr[index]= - arr[index]
            
    return res

#test case 1
arr = [1, 3, 4, 2, 2]
print(Find_duplicates(arr))

#test case 2
arr =  [3, 1, 3, 4, 2]
print(Find_duplicates(arr))

#test case 3
arr =  [1, 1]
print(Find_duplicates(arr))
            
#test case 4
arr =  [1, 4, 4, 2, 3]
print(Find_duplicates(arr))
            