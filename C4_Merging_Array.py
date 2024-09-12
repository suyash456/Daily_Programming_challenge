# Insertion sort function (from DAY 1 code)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to merge arrays A and B in order
def inorder_merge(A, B):
    m = len(A)
    n = len(B)

    for i in range(m):
        if A[i] > B[0]:
            # Swap A[i] with B[0]
            A[i], B[0] = B[0], A[i]

            # Sort B after the swap to maintain its sorted order
            insertion_sort(B)

    # Print array A
    print("Array A =", A)

    # Print array B
    print("Array B =", B)

#test case 1
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
inorder_merge(arr1, arr2)

#test case 2
arr1 = [10,12,14]
arr2 =[1,3,5]
inorder_merge(arr1, arr2)

#test case 3
arr1 = [2,3,8]
arr2 = [4, 6, 10]
inorder_merge(arr1, arr2)

#test case 4
arr1 = [1]
arr2 = [2]
inorder_merge(arr1, arr2)
