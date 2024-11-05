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
    
    # add element after a given node
    def add_after(self, data, x):
        if self.head is None:
            print("Linked List is empty.")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("Node is not present in the Linked List.")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            if n.nref is not None: # if it is not last node
                n.nref.pref = new_node
            n.nref = new_node

    # add element before a given node
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty.")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("Node is not present in the Linked List.")
        else:
            new_node = Node(data)
            new_node.pref = n.pref
            new_node.nref = n
            if n.pref is not None: # if it is not first node
                n.pref.nref = new_node
            else:
                self.head = new_node
            n.pref = new_node

    # Deletion Operation
    # delete element at the beginning
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty cannot delete.")
        elif self.head.nref is None:
            self.head = None
            print("Linked List is empty now after element deletion.")
        else:
            self.head = self.head.nref
            self.head.pref = None

    # delete element at the end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty cannot delete.")
        elif self.head.nref is None:
            self.head = None
            print("Linked List is empty now after element deletion.")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    # delete element by value
    def delete_node(self, x):
        if self.head is None:
            print("Linked List is empty cannot delete.")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
                print("Linked List is empty now after element deletion.")
            else:
                print("Element is not present in the Linked List.")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n.nref is not None: # if it is not last node
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else: # if it is last node
            if n.data == x:
                n.pref.nref = None
            else:
                print("Element is not present in the Linked List.")

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
# add after a specific node
dl1.add_after(55, 50)
# add before a specific node
dl1.add_before(25, 20)
print("Linked List in Forward Direction: ")
dl1.print_LL_Forward()
print("\n")
print("Linked List in Backward Direction: ")
dl1.print_LL_Backward()
print()
# delete element at the beginning
dl1.delete_begin()
print()
print("Linked List after deleting element at the beginning: ")
dl1.print_LL_Forward()
print()
# delete element at the end
dl1.delete_end()
print()
print("Linked List after deleting element at the end: ")
dl1.print_LL_Forward()
print()
# delete a specific node by value
dl1.delete_node(55)
print()
print("Linked List after deleting element by value: ")
dl1.print_LL_Forward()
print()
