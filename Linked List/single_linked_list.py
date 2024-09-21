# Single Linked List
'''
Perform operations like 
- Add element
- Remove element
- traversal
'''
# Add element
'''
We can add element at
- beginning
- end
- inbetween
'''
'''
if you want to add element at the beginning then follow these steps
- Create a new node.
- Add data to the new node.
- Make the next of the new node as the previous head.
- Make the new node as the head.

if you want to add element at the end then follow these steps
- Create a new node.
- Add data to the new node.
- Find the last node.
- Make the next of the last node point to the new node.

if you want to add element inbetween two node then follow these steps
- Create a new node.
- Add data to the new node.
- Find the previous node.
- Make the next of the new node as the next of the previous node.
- Make the next of the previous node point to the new node.
'''
'''
Removing an Element from the Beginning of a Linked List
- Check if the List is Empty: If the head is None, the list is empty, and there is nothing to remove.
- Update the Head: Set the head to be the next node in the list (i.e., head = head.next).

Removing an Element from the End of a Linked List
- Check if the List is Empty: If the head is None, the list is empty, and there is nothing to remove.
- Traverse to the Last Node: Traverse the list to find the second-to-last node.
- Update the Next of the Second-to-Last Node to None: Set the next of the second-to-last node to None.

Removing an Element from Between Two Nodes in a Linked List
- Check if the List is Empty: If the head is None, the list is empty, and there is nothing to remove.
- Find the Node to be Removed: Traverse the list to find the node before the one to be removed.
- Update the Next of the Previous Node: Set the next of the previous node to the next of the node to be removed.
'''
# program to create single linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # function to print the linked list
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = " ") # print data
                n = n.ref # go to next node

    # add element at the beginning
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # add element at the end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node 

    # add element inbetween two nodes
    def add_inbetween(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

LL1 = LinkedList() # create object
# add element at the beginning
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin("linkan")
# add element at the end
LL1.add_end(30)
LL1.add_end(40)
LL1.print_LL()
