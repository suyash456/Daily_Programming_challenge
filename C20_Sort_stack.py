def Sort_stack(stack):
    if not stack:
        return
    top = stack.pop()
    Sort_stack(stack)
    Insert_sorted(stack, top)

def Insert_sorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return
    top = stack.pop()
    Insert_sorted(stack, element)
    stack.append(top)

# Test case 1
stack = [7, 1, 5]
Sort_stack(stack)
print(stack)

# Test case 2
stack = [5]
Sort_stack(stack)
print(stack)

# Test case 3
stack = [-3, 14, 8, 2]
Sort_stack(stack)
print(stack)

# Test case 4
stack = []
Sort_stack(stack)
print(stack)

# Test case 5
stack = [3,3,3]
Sort_stack(stack)
print(stack)
