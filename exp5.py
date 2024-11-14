class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for i in range(2, position):
            if current_node is None:
                print(f"Position {position} is out of bounds.")
                return
            current_node = current_node.next
        if current_node is None:
            print(f"Position {position} is out of bounds.")
            return
        new_node.next = current_node.next
        current_node.next = new_node
 
    def delete_element(self, data):
        current_node = self.head
        if current_node is not None:
            if current_node.data == data:
                self.head = current_node.next
                current_node = None
                return
        while current_node is not None:
            if current_node.data == data:
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"Element {data} not found.")
            return
        prev_node.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Create a new linked list
linked_list = LinkedList()

# Insert elements at the front
linked_list.insert_at_front(3)
linked_list.insert_at_front(2)
linked_list.insert_at_front(1)

# Insert elements at the back
linked_list.insert_at_back(4)
linked_list.insert_at_back(5)

# Insert element at a specific position
linked_list.insert_at_position(2.5, 3)

# Delete an element
linked_list.delete_element(3)

# Display all elements
linked_list.display()
