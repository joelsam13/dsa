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
        rear = (rear + 1) % size  # Wrap rear around
        queue[rear] = value
        print("Inserted", value, "into queue.")
    org()

def delete():
    global front, rear
    if is_empty():
        print("Queue is empty! Cannot delete.")
    else:
        print("Deleted", queue[front], "from queue.")
        queue[front] = None
        if front == rear:
            # Queue becomes empty after this deletion
            front = rear = -1
        else:
            front = (front + 1) % size  # Wrap front around
    org()

def display():
    if is_empty():
        print("Queue is empty!")
    else:
        print("Queue elements are:", end=" ")
        i = front
        while True:
            if queue[i] is not None:
                print(queue[i], end=" ")
            if i == rear:
                break
            i = (i + 1) % size  # Wrap around to next element
        print()
    org()

def is_empty():
    return front == -1

def is_full():
    return (rear + 1) % size == front

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
