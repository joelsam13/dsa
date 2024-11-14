def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit(): 
            stack.append(int(char))
        else:  
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
            elif char == '^':
                stack.append(a ** b)

    return stack.pop()

postfix_expr = input("Enter a postfix expression: ")
result = evaluate_postfix(postfix_expr)
print("Postfix Expression: ", postfix_expr)
print("Evaluation Result: ",result)