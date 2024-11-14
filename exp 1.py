stack = []
pointer = -1  

def push():
    global pointer
    a = int(input("Enter the number to be pushed \n"))
    if pointer + 1 < len(stack):
        stack[pointer + 1] = a
    else:
        stack.append(a)
    pointer += 1
    org()

def pop():
    global pointer
    if pointer >= 0:
        print("The value that was poped is",stack[pointer])
        pointer -= 1
    else:
        print("Stack is empty.")
    org()

def peek():
    if pointer >= 0:
        print("Top value: ", stack[pointer])
    else:
        print("Stack is empty.")
    org()

def display():
    print(stack[:pointer + 1])
    org()


def org():
    n = int(input("Enter 1 for push, 2 for pop, 3 for peek  and 4 for display \n"))
    if n == 1:
        push()
    elif n == 2:
        pop()
    elif n == 3:
        peek()
    elif n == 4:
        display()
    else:
        print("Exiting...")
        exit()

org()
