**Q .** You are given an unsorted array of integers and a positive integer K. Your task is to find the Kth largest element in the array. The Kth largest element is the element that would appear in the Kth position if the array were sorted in descending order.

You need to implement a function that returns this Kth largest element without explicitly sorting the entire array.

Example
arr = [3, 2, 1, 5, 6, 4]
k = 2
Output: 5



**Solution :** 
                  The Value of The K is 2 that's why We have to find the secode largest number in an array . To Find the second largest number in an array we have to go through an array with the help of **for** loop .
                  Here is Logic For Solving This Problem
                  Initialize largest = 0, second_largest = -inf.
                  **Compare with 3: Update largest = 3, second_largest = 0.
                  Compare with 2: Update second_largest = 2.
                  Compare with 1: No change.
                  Compare with 5: Update second_largest = 3, largest = 5.
                  Compare with 6: Update second_largest = 5, largest = 6.
                  Compare with 4: No change**
