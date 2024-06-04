# Implimentation of queue
'''
using list
using modules
'''
# Using list
'''
- enqueue - use append()
- dequeue - use pop(0)
'''
queue = []

# add element
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
# or for different end
queue.insert(0, 10)
queue.insert(0, 20)
# remove element
queue.pop(0)
queue.pop(0)
# or for different end
queue.pop()
queue.pop()

# check element at rear and front side
queue[0]
queue[-1]

# complete example
queue = []

def enqueue():
    element = eval(input('Enter the element: '))
    queue.append(element)
    print(element, "is added to the queue")

def display():
    print(queue)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0)
        print("removed element is", e)

while True:
    print("Select an operation\n1. add\n2. remove\n3. show\n4. quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Please choose a valid operation")

# using modules
'''
from collections import deque
'''

# using collections module

from collections import deque

q = deque()
# add element to left end
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
# or adding in right end
q.append(10)
q.append(20)
q.append(30)
# remove element from right end
q.pop()
q.pop()
q.pop()
# or remove from left end
q.popleft()
q.popleft()
q.popleft()

# chcek empty or not
not q
# chcek element at front and rear end
q[-1]
q[0]

# using queue module

from queue import Queue

q = Queue(4)
# add element
q.put_nowait(10)
q.put_nowait(20)
q.put_nowait(30)
# remove element
q.get_nowait()
q.get_nowait()
q.get_nowait()
