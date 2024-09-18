from collections import defaultdict

def GroupAnagrams(strs):
        
    d = defaultdict(list)
        
    for s in strs:
        count = [0] * 26
            
        for letter in s:
                count[ord(letter) - ord('a')] += 1
                
        d[tuple(count)].append(s)
            
    return d.values()

#test case 1
strs= ["eat", "tea", "tan", "ate", "nat", "bat"]
print(GroupAnagrams(strs))

#test case 2
strs= [""]
print(GroupAnagrams(strs))

#test case 3
strs= ["a"]
print(GroupAnagrams(strs))

#test case 4
strs= ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
print(GroupAnagrams(strs))

#test case 5
strs=  ["abc", "def", "ghi"]
print(GroupAnagrams(strs))
     