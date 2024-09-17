def longestCommonPrefix(strs):
        if not strs:
            return ""
        
        # Loop through the characters of the first string
        for i in range(len(strs[0])):
            ch = strs[0][i]
            
            # Compare the current character with the same index in other strings
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != ch:
                    return strs[0][:i]
        
        return strs[0]


# Test Case 1
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

# Test Case 2
strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs))

# Test Case 3
strs = ["apple", "ape", "april"]
print(longestCommonPrefix(strs))

# Test Case 4
strs = [""]
print(longestCommonPrefix(strs))

# Test Case 5
strs = ["alone"]
print(longestCommonPrefix(strs))