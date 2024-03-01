class LinkedStack:

    class Node:
        __slots__ = 'element', 'next_node'  # Slots for memory optimization

        def __init__(self, element, next_node):
            self.element = element  # Initialize element of the node
            self.next_node = next_node  # Initialize the reference to the next node

    def __init__(self):
        self.head = None  # Initialize head pointer to None
        self.size = 0  # Initialize stack size to 0

    def length(self):
        return self.size  # Return the size of the stack

    def isEmpty(self):
        return self.size == 0  # Check if the stack is empty

    def push(self, e):
        self.head = self.Node(e, self.head)  # Create a new node and make it the new head
        self.size += 1  # Increment the size of the stack

    def top(self):
        if self.isEmpty():
            raise RuntimeError("Stack is Empty")  # Raise error if stack is empty
        return self.head.element  # Return the element at the top of the stack

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Stack is Empty")  # Raise error if stack is empty
        node = self.head.element  # Get the element at the top of the stack
        self.head = self.head.next_node  # Move the head pointer to the next node
        self.size -= 1  # Decrement the size of the stack
        return node  # Return the element that was removed


# Test code
if __name__ == "__main__":
    stack = LinkedStack()  # Create a new LinkedStack object

    # Test push operation
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Test top operation
    print("Top element:", stack.top())  # Should print 3

    # Test pop operation
    print("Popped element:", stack.pop())  # Should print 3

    # Test length operation
    print("Stack length:", stack.length())  # Should print 2

    # Test if the stack is empty
    print("Is stack empty?", stack.isEmpty())  # Should print False

    # Test popping all elements
    while not stack.isEmpty():
        print("Popped element:", stack.pop())  # Should print 2 and 1

    # Test if the stack is empty after popping all elements
    print("Is stack empty?", stack.isEmpty())  # Should print True

    # Test popping from an empty stack (should raise an error)

    #stack.pop()
    
    # print("Popped element:", stack.pop())  # Uncomment to test
