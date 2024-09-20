def Balanced_Parantesis(s):
    stack = []
    if len(s)==0:
        return True
    for char in s:
      
        if char in '({[':
            stack.append(char)
               
        elif char in ')}]':
          
            if not stack:
                return False
                
            top = stack.pop()
            if (top == '(' and char != ')') or \
               (top == '{' and char != '}') or \
               (top == '[' and char != ']'):
                return False
            
            else:
                return True
            

#Test Case 1
s =  "()"
print(Balanced_Parantesis(s))

#Test Case 2
s =  "([)]"
print(Balanced_Parantesis(s))

#Test Case 3
s = "[{()}]"
print(Balanced_Parantesis(s))

#Test Case 4
s =""
print(Balanced_Parantesis(s))

#Test Case 5
s = "{[}"
print(Balanced_Parantesis(s))

