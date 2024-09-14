def find_subarrays_with_zero_sum(arr):
    prefix_sum_map = {}
    
    prefix_sum = 0
    subarrays = []
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum == 0:
            subarrays.append((0, i))
        
        if prefix_sum in prefix_sum_map:
            for start_index in prefix_sum_map[prefix_sum]:
                subarrays.append((start_index + 1, i))
        
        if prefix_sum in prefix_sum_map:
            prefix_sum_map[prefix_sum].append(i)
        else:
            prefix_sum_map[prefix_sum] = [i]
    
    return subarrays

#Test Case1
arr = [1, 2, -3, 3, -1, 2]
print(find_subarrays_with_zero_sum(arr))
