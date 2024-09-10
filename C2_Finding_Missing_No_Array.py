def Find_missing_values(arr):
    n= len(arr)+1
    expected_sum = n *(n+1)//2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    
    return missing_number

#test case 1
arr= [1, 2, 4, 5]
print("Missing Value = ",Find_missing_values(arr))

#test case 2
arr= [2, 3, 4, 5]
print("Missing Value = ",Find_missing_values(arr))

#test case 3
arr= [1, 2, 3, 4]
print("Missing Value = ",Find_missing_values(arr))

#test case 4
arr= [1]
print("Missing Value = ",Find_missing_values(arr))


