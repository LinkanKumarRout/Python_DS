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
