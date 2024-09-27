def Evaluate_expression(Expression):
    arr = Expression.split()
    stack=[]
    operator=["+","-","*","/","%","^"]

    for item in arr:
        if item not in operator:
            stack.append((item))
        else:
            first=int(stack.pop())
            sec=int(stack.pop())

            if(item=="+"):
                stack.append(sec + first)

            if (item == "-"):
                stack.append(sec - first)

            if (item == "*"):
                stack.append(sec * first)

            if (item == "/"):
                stack.append(sec / first)

            if (item == "%"):
                stack.append(sec % first)
            if (item == "^"):
                stack.append(sec ** first)

    return stack[-1]

#Test case 1
Expression =  "5 6 +"
print(Evaluate_expression(Expression))

#Test case 2
Expression =  "3 4 2 * 1 5 - 2 3 ^ ^ / +"
print(Evaluate_expression(Expression))

#Test case 3
Expression =  "-5 6 -"
print(Evaluate_expression(Expression))

#Test case 4
Expression =  "15 7 1 1 + - / 3 * 2 1 1 + + -"
print(Evaluate_expression(Expression))

#Test case 5
Expression =  '5'
print(Evaluate_expression(Expression))

