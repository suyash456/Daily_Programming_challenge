def First_element_to_repeat_k_times(arr, k):
    count_dict = {}
    
    # Count occurrences of each element
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the first element that appears exactly k times
    for num in arr:
        if count_dict[num] == k:
            return num
    
    return -1

# Test case
arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
print(First_element_to_repeat_k_times(arr, k))

# Test case
arr = [2, 3, 4, 2, 2, 5, 5]
k = 2
print(First_element_to_repeat_k_times(arr, k))

# Test case
arr = [1, 1, 1, 1]
k = 1
print(First_element_to_repeat_k_times(arr, k))

# Test case
arr = [10]
k = 1
print(First_element_to_repeat_k_times(arr, k))

# Test case
arr = [6, 6, 6, 6, 7, 7, 8, 8, 8]
k = 3
print(First_element_to_repeat_k_times(arr, k))