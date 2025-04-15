class Stack:
    def _init_(self):
        self.stack = []

    # Push an item onto the stack
    def push(self, item):
        self.stack.append(item)

    # Pop an item from the stack
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "Stack is empty"

    # Peek the top item of the stack
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return "Stack is empty"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

# Example usage:

my_stack = Stack()

# Push items
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Peek the top item
print("Top item:", my_stack.peek())

# Pop an item
print("Popped item:", my_stack.pop())

# Check if the stack is empty
print("Is the stack empty?", my_stack.is_empty())

# Pop remaining items
print("Popped item:", my_stack.pop())
print("Popped item:", my_stack.pop())

# Try to pop from an empty stack
print("Popped item:", my_stack.pop())
