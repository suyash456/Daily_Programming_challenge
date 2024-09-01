def findkth_number(arr):
    if len(arr)<2:
        return None
    Kth = 0
    L = 0
    
    for num in arr:
        if num > L:
            Kth = L
            L = num
            
        elif num > Kth and num != L:
            Kth = num 
            
    print("Kth Number in Array :",Kth)    
    

arr = [3, 2, 1, 5, 6, 4]
kth_num = findkth_number(arr)
        
            
        
        