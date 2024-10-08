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

    # add after a specific node
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the Linked List.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    # add before a specific node
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty.")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in the Linked List.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    # adding element when linked list is empty
    def add_when_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty.")
    
    # delete element at the beginning
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            self.head = self.head.ref
    
    # delete element at the end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty.")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    # delete a specific node by value
    def delete_node(self, x):
        if self.head is None:
            print("Cannot delete. Linked List is empty.")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in the Linked List.")
        else:
            n.ref = n.ref.ref

    # delete entire linked list
    def delete_linked_list(self):
        self.head = None

LL1 = LinkedList() # create object
# add element when linked list is empty
LL1.add_when_empty(100)
# add element at the beginning
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
# add element at the end
LL1.add_end(60)
LL1.add_end(70)
# add after a specific node
LL1.add_after(50, 20)
# add before a specific node
LL1.add_before(80, 60)

LL1.print_LL() # to check what are the elements in the linked list
print("\n")
# delete element at the beginning
LL1.delete_begin()
# delete element at the end
LL1.delete_end()
# delete a specific node by value
LL1.delete_node(60)

LL1.print_LL()
