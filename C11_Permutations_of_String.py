def Permutations (s):      
    if len(s) == 1:
        return [s]
    perms = Permutations (s[1:])
    char = s[0]
    result = []
    
    for perm in perms:
        for i in range(len(perm)+1): 
            result.append(perm[:i]+ char + perm[i:])
            
    return result

#Test Case1
s="abc"
print(Permutations(s))
