def sort_array(arr):
    L=0
    M=0
    H= len(arr)-1
    
    while M <= H:
        if arr[M] == 0:
            arr[L], arr[M] = arr[M], arr[L]
            L += 1
            M += 1
        elif arr[M] == 1:
            M += 1
        else:
            arr[M], arr[H] = arr[H], arr[M]
            H -= 1

arr = [0, 1, 2, 1, 0, 2, 1, 0]
sort_array(arr)
print(arr)
