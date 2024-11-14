def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []
    postfix = ""
    
    for char in expression:
        if char.isalnum():  # Operand
            postfix += char
        elif char == '(':  # Opening parenthesis
            stack.append(char)
        elif char == ')':  # Closing parenthesis
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Pop the opening parenthesis '('
        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.append(char)
    
    while stack:
        postfix += stack.pop()
    
    return postfix

s = input("Enter the Infix Expression \n")
result = infix_to_postfix(s)
print("The postfix expression is: ", result)
