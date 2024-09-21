# Stack Data Structure
'''
Stack is a data structure where addition and deletion of data takes place at the same end (top)
and the opposite end is called base.

it follows LIFO or FILO
'''
# Basic operation performed on a stack
'''
1. push - add element
2. pop - remove element
3. peek or top - give top element
4. isEmpty - tell stack is empty or not
'''
# application
'''
- reverse a string
- expression evaluation like prefix to postfix
- forward and backward feature in a browser
'''


# Queue Data Structure
'''
It is a linear data structure where element is added at one end(back/tail) and is removed at the other end(head/front)

it follows FIFO or LILO
'''
'''
the process of adding elements to the queue is called enqueue
and the process of removing element is called dequeue
'''
# operation
'''
- enqueue
- dequeue
- isFull()
- isEmpty()
'''
# application
'''
- fifo scenario
like uploading post, photo, comments
- call center
'''
# Priority Queue
'''
Are a modified version of queue where each element is associated with priority and they are served based on their priority.
if two element has same priority then element will be served as it's order
'''
'''
- priority may be the value itself
  - lowest the element highest the priority
  - highest the element highest the priority
- a tuple that hold value as well as priority
'''
# implimenting priority queue
'''
- list
- PriorityQueue from queue module
'''

# Linked List
'''
A linked list is a fundamental data structure in computer science used to store a collection of elements, called nodes. Each node contains two components: data and a reference (or link) to the next node in the sequence. Linked lists provide several advantages over other data structures, such as arrays, due to their dynamic nature and efficient insertion and deletion operations.
'''
'''
Node: element in a linked list
Head: first node in a linked list
Tail: Last node in a linked list - it points to None
'''
'''
Advantages of Linked Lists
- Dynamic Size: Linked lists can grow and shrink in size by allocating and deallocating memory as needed.
- Efficient Insertions/Deletions: Insertions and deletions of nodes are efficient, especially when adding or removing from the beginning or middle of the list.
- Memory Utilization: Linked lists do not require contiguous memory allocation, unlike arrays.

Disadvantages of Linked Lists
- Memory Overhead: Each node requires extra memory for storing the reference to the next (and possibly previous) node.
- Sequential Access: Linked lists do not support direct access to elements via indexing, requiring traversal from the head for any access.
- Complexity: Linked lists involve more complex memory management compared to arrays.
'''
# Use of Linked list
'''
1. Dynamic Memory Allocation
- Operating Systems: Linked lists are used by operating systems to manage free memory blocks. The memory manager keeps track of free memory segments using a linked list, allowing efficient allocation and deallocation of memory as processes request and release memory.

2. Implementation of Other Data Structures
- Stacks and Queues: Linked lists can be used to implement stacks and queues, allowing for dynamic sizing and efficient insertion and deletion operations.
- Graphs: Adjacency lists, a common way to represent graphs, use linked lists to store the neighbors of each vertex, making the structure dynamic and memory efficient.
- Hash Tables: Linked lists are used to handle collisions in hash tables through chaining. Each bucket in the hash table points to a linked list of entries that hash to the same value.

3. Real-Time Applications
- Music and Video Playlists: Applications like media players use linked lists to manage playlists. Songs or videos can be added or removed dynamically without needing to resize an underlying array.
- Undo/Redo Functionality: Text editors and other applications use linked lists to implement undo and redo functionality. Each action is stored in a node, and moving back and forth through the list allows for undoing and redoing actions.

4. Network Applications
- Packet Buffers: Routers and network devices use linked lists to manage packet buffers. Packets arriving at the router are stored in a linked list while they wait to be processed, allowing for efficient insertion and deletion of packets.

5. Simulation and Real-Time Systems
- Event-Driven Simulations: Linked lists are used in event-driven simulations to manage a list of events scheduled to occur. Events are inserted in order of their scheduled time, allowing for efficient simulation processing.

6. File Systems
- Directory Management: Some file systems use linked lists to manage directories. Each directory entry can point to the next entry, allowing for dynamic addition and removal of files and subdirectories.
Free Space Management: Similar to dynamic memory allocation, linked lists are used to manage free space in storage devices, keeping track of free blocks that can be allocated to files.

7. Real-Time Navigation Systems
- GPS Systems: Linked lists can be used to manage routes in GPS systems. Each node can represent a waypoint, and routes can be dynamically updated as new waypoints are added or removed.

8. Web Browsers
- History Management: Browsers use linked lists to manage the history of visited websites. Each webpage is a node in the list, and moving forward and backward through the list allows users to navigate their browsing history efficiently.

9. Multiplayer Online Games
- Player Management: In multiplayer games, linked lists can be used to manage active players in a game session. Players can join or leave the game, and linked lists allow efficient addition and removal of player entries.

10. Embedded Systems
- Sensor Networks: Linked lists are used in embedded systems to manage data from sensors. As new sensor data arrives, it is added to the list, allowing for dynamic and efficient data handling.
'''
# Types of Linked Lists
'''
Singly Linked List:

Each node points to the next node.
Traversal is only possible in one direction (forward).
The last node points to None, indicating the end of the list.
Example:
[data1] -> [data2] -> [data3] -> None

Doubly Linked List:

Each node contains a reference to both the next and the previous node.
Traversal is possible in both directions (forward and backward).
The first node's previous reference and the last node's next reference are None.
Example:
None <- [data1] <-> [data2] <-> [data3] -> None

Circular Linked List:

The last node points back to the first node, forming a circle.
Can be singly or doubly linked.
No node points to None.
Example (singly linked):
[data1] -> [data2] -> [data3] -> [data1]
'''
