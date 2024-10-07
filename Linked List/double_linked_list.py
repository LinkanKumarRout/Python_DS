'''
Double Linked List:

- It is a type of Linked List
- It is similar to the single linked list
- It has two pointers
- Head and Tail
- Head points to the previous node
- Tail points to the next node

Advantages of Double Linked List
- Dynamic Size
- Efficient Insertions/Deletions
- Memory Utilization
- Sequential Access
- Complexity

Disadvantages of Double Linked List
- Memory Overhead
- Random Access

Types of Double Linked List
- Circular
- Circular with Loop
- Circular with Loop and Head and Tail
'''

# program to create double linked list
class Node:
    def __init__(self, data)
        self.data = data
        self.pref = None
        self.nref = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # print linked list in forward direction
    def print_LL_Forward(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.nref

    # print linked list in backward direction
    def print_LL_Backward(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "<--", end = " ")
                n = n.pref
