#__________Stack implementation using Linked List___________#
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    # Print Stack
    def __str__(self):
        values = []
        current = self.LinkedList.head

        while current:
            values.append(str(current.value))
            current = current.next

        return '\n'.join(values)

    # Check if stack is empty
    def isEmpty(self):
        return self.LinkedList.head is None

    # Push element
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    # Pop element
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"

        nodeValue = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return nodeValue

    # Peek top element
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"

        return self.LinkedList.head.value

    # Delete stack
    def delete(self):
        self.LinkedList.head = None


# Create Stack
customStack = Stack()

print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)

print("Top element is:", customStack.peek())

print("Popped element:", customStack.pop())
print("Popped element:", customStack.pop())

print("Top element is:", customStack.peek())

customStack.delete()

print(customStack)
print(customStack.isEmpty())

print(customStack.pop())