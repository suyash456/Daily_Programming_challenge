def Reverse_words(s):

    words = s.split()
    reversed_words = words[::-1]
    result = " ".join(reversed_words)
    
    return result

#test case 1
s="the sky is blue"
print(Reverse_words(s))

#test case 2
s="  hello world  "
print(Reverse_words(s))

#test case 3
s="a good   example"
print(Reverse_words(s))

#test case 4
s= "    "
print(Reverse_words(s))

#test case 5
s="word"
print(Reverse_words(s))
