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
    def __init__(self, data):
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
    
    # Insertion Operation
    # insert when the linked list is empty
    def add_when_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty.")

    # add element at the beginning
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # add element at the end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

dl1 = DoubleLinkedList()
# add element when linked list is empty
dl1.add_when_empty(100)
# add element at the beginning
dl1.add_begin(40)
dl1.add_begin(30)
dl1.add_begin(20)
dl1.add_begin(10)
# add element at the end
dl1.add_end(50)
dl1.add_end(60)
dl1.add_end(70)
dl1.add_end(80)
print("Linked List in Forward Direction: ")
dl1.print_LL_Forward()
print("\n")
print("Linked List in Backward Direction: ")
dl1.print_LL_Backward()
