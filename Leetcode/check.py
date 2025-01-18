class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after_value(self, prev_value, new_value):
        """
        Inserts a new node with the given new_value after the node with the given prev_value.

        Args:
            prev_value (any): The value of the node after which to insert the new node.
            new_value (any): The value to be inserted in the new node.
        """

        # Create a new node
        new_node = Node(new_value)

        # If the linked list is empty
        if self.head is None:
            self.head = new_node
            return

        # Find the previous node
        prev_node = self.head
        while prev_node and prev_node.data != prev_value:
            prev_node = prev_node.next

        # If the previous node is not found
        if prev_node is None:
            print("The given previous value not found")
            return

        # Insert the new node after the previous node
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        """Prints the linked list."""
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

print("Original Linked List:")
llist.print_list()

llist.insert_after_value(2, 4)

print("Linked List after insertion:")
llist.print_list()