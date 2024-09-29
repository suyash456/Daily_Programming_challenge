def Reverse_stack(stack):
    if not stack:
        return
    
    top = stack.pop()
    Reverse_stack(stack)
    Insert_at_bottom(stack, top)

def Insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        Insert_at_bottom(stack, item)
        stack.append(top)

#Test case 1
stack =  [3, 2, 1]
Reverse_stack(stack)
print(stack)

#Test case 2
stack = [5]
Reverse_stack(stack)
print(stack)

#Test case 3
stack = [-5, -10, -15]
Reverse_stack(stack)
print(stack)

#Test case 4
stack = []
Reverse_stack(stack)
print(stack)

#Test case 5
stack = [3,3,3]
Reverse_stack(stack)
print(stack)
