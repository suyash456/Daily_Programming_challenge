def count_substrings_with_k_distinct(s, k):
    n = len(s)
    count = 0
    for i in range(n):
        distinct_char_set = set()
        for j in range(i, n):
            distinct_char_set.add(s[j])
            if len(distinct_char_set) == k:
                count += 1
            if len(distinct_char_set) > k:
                break
    return count

# Test case 1
s = "pqpqs"
k = 2
print(count_substrings_with_k_distinct(s, k))

# Test case 2
s = "aabacbebebe"
k = 3
print(count_substrings_with_k_distinct(s, k))

# Test case 3
s = "a"
k = 1
print(count_substrings_with_k_distinct(s, k))

# Test case 4
s = "abc"
k = 3
print(count_substrings_with_k_distinct(s, k))

# Test case 5
s = "abc"
k = 2
print(count_substrings_with_k_distinct(s, k))
