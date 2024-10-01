from collections import deque

def Max_Sliding_Window(arr, k):
    dq = deque()
    result = []
    
    for i in range(len(arr)):

        if dq and dq[0] == i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result

#Test case
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Max_Sliding_Window(arr, k))

#Test case
arr = [1,5,3,2,4,6]
k = 3
print(Max_Sliding_Window(arr, k))

#Test case
arr = [1,2,3,4]
k = 2
print(Max_Sliding_Window(arr, k))

#Test case
arr = [7,7,7,7]
k = 1
print(Max_Sliding_Window(arr, k))
