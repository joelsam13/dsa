queue = []
front = -1
rear = -1
size = 0

def create_queue(s):
    global queue, front, rear, size
    queue = [None] * s
    front = -1
    rear = -1
    size = s
    org()

def insert():
    global front, rear
    if is_full():
        print("Queue is full! Cannot insert.")
    else:
        value = int(input("Enter the value to insert: "))
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = value
        print("Inserted " , value , " into queue.")
    org()

def delete():
    global front, rear
    if is_empty():
        print("Queue is empty! Cannot delete.")
    else:
        print("Deleted" , queue[front], " from queue.")
        queue[front] = None
        front += 1
        if front > rear:
            front = rear = -1
    org()

def display():
    if is_empty():
        print("Queue is empty!")
    else:
        print("Queue elements are:", end=" ")
        for i in range(front, rear + 1):
            if queue[i] is not None:
                print(queue[i], end=" ")
        print()
    org()

def is_empty():
    return front == -1

def is_full():
    return rear == size - 1

def org():
    print("\nQueue Operations:")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        display()
    else:
        print("Exiting...")
        exit()

if __name__ == "__main__":
    size = int(input("Enter the size of the queue: "))
    create_queue(size)
