# # #Stack using Linked List

# # class Node:
# #     def __init__(self, value = None):
# #         self.value = value
# #         self.next = None

# # class LinkedList:
# #     def __init__(self):
# #         self.head = None
    
# #     def __iter__(self):
# #         curNode = self.head
# #         while curNode:
# #             yield curNode  #yield is used to return value
# #             curNode = curNode.next

# # class Stack:
# #     def __init__(self):
# #         self.LinkedList = LinkedList()

# #     def __str__(self):
# #         values = [str(x.value) for x in self.LinkedList]
# #         return '\n'.join(values)

# #     def isEmpty(self):
# #         if self.LinkedList.head ==None:
# #             return True
# #         else:
# #             return False

# #     def push(self,value):
# #         node = Node(value)
# #         node.next =self.LinkedList.head
# #         self.LinkedList.head = node

# #     def pop(self):
# #         if self.isEmpty():
# #             return "There is no element in the stack"
# #         else:
# #             nodeValue = self.LinkedList.head.value
# #             self.LinkedList.head = self.LinkedList.head.next
# #             return nodeValue
        
# #     def peek(self):
# #         if self.isEmpty():
# #             return "There is not any element in the stack"
# #         else:
# #             return self.LinkedList.head.value
        
# #     def delete(self):
# #         self.LinkedList.head = None

# # customStack = Stack()

# # print(customStack.isEmpty())

# # customStack.push(1)
# # customStack.push(2)
# # customStack.push(3)

# # print("Top element is:", customStack.peek())
# # print("Popped element:", customStack.pop())
# # print("Popped element:", customStack.pop())
# # print("Top element is:", customStack.peek())

# # customStack.delete()
# # print(customStack)
# # print(customStack.isEmpty())
# # print(customStack.pop())

# #=========================================================================================================================
# #Queue Linked List
# class Node:

#     def __init__(self, value=None):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return str(self.value)


# class LinkedList:

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode   #We use yield to return value sequentially
#             curNode = curNode.next

# class Queue:

#     def __init__(self):
#         self.LinkedList = LinkedList()

#     def __str__(self):
#         values = [str(x.value) for x in self.LinkedList]
#         return '\n'.join(values)

#     def enqueue(self, value):
#         newNode = Node(value)
#         if self.LinkedList.head is None:
#             self.LinkedList.head = newNode
#             self.LinkedList.tail = newNode
#         else:
#             self.LinkedList.tail.next = newNode
#             self.LinkedList.tail = newNode

#     def isEmpty(self):
#         if self.LinkedList.head is None:
#             return True
#         else:
#             return False

#     def dequeue(self):
#         if self.isEmpty():
#             return "There is no node in the queue"
#         else:
#             tempNode = self.LinkedList.head
#             # If only one node exists
#             if self.LinkedList.head == self.LinkedList.tail:
#                 self.LinkedList.head = None
#                 self.LinkedList.tail = None

#             else:
#                 self.LinkedList.head = self.LinkedList.head.next
#             return tempNode.value

#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element in the queue"
#         else:
#             return self.LinkedList.head.value

# # Create Queue
# customQueue = Queue()

# # Insert elements
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)

# # Display Queue
# print("Queue Elements:")
# print(customQueue)

# # Peek front value
# print("Front Value:")
# print(customQueue.peek())

# # Remove element
# print("Dequeued Element:")
# print(customQueue.dequeue())

# # Display queue again
# print("Queue After Dequeue:")
# print(customQueue)