def LengthOfLongestSubstring(s):
    visited = {}
    i = 0
    result = 0
        
    for j in range(len(s)):
        if s[j] in visited:
            i = max(visited[s[j]], i)
                
        result = max(j-i+1, result)
        visited[s[j]] = j + 1
            
    return result

#Test Case 1
s = "abcabcbb"
print(LengthOfLongestSubstring(s))

#Test Case 1
s = "bbbbb"
print(LengthOfLongestSubstring(s))

#Test Case 1
s = "pwwkew"
print(LengthOfLongestSubstring(s))

#Test Case 1
s = "abcdefgh"
print(LengthOfLongestSubstring(s))

#Test Case 1
s = "a"
print(LengthOfLongestSubstring(s))
    