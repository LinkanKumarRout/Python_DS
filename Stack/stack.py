# implimenting stack
'''
1. using list
2. using modules
'''
# using list

# creating an empty list
stack = []
# push operation at end use append()
stack.append(10) # [10]
stack.append(20) # [10, 20]
stack.append(30) # [10, 20, 30]
stack.append(40) # [10, 20, 30, 40]
# pop operation use pop()
stack.pop() # 40
stack.pop() # 30
stack.pop() # 20
stack.pop() # 10
# isEmpty use len(stack) == 0, not stack
# peek operation use stack[-1]

# A complete example
stack = []

def push():
    if len(stack) == n:
        print("stack is full")
    else:
        element = eval(input('Enter a element: '))
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element is", e)
        print(stack)

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print(stack[-1])

def isEmpty():
    if not stack:
        return True
    else:
        return False
n = int(input("Enter limit of stack: "))
while True:
    print("Select an operation\n1. push\n2. pop\n3. peek\n4. isEmpty\n5. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        peek()
    elif choice == 4:
        print(isEmpty())
    elif choice == 5:
        break
    else:
        print("Enter a correct option")

# stack using modules
'''
from collections import deque
from queue import LifoQueue
'''
#1. using collections module
from collections import deque

# empty stack
stack = deque()
# add element
stack.append(10)
stack.append(20)
# remove element
stack.pop()
stack.pop()
# peek element
stack[-1]
# isEmpty
not stack, len(stack) == 0

#2. using queue module

from queue import LifoQueue

# empty stack
stack = LifoQueue(3) # maximum 3 element
# add element
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40, timeout=1) # here it will block the execution so we use timeout=1, after 1 sec it will give us the required message
# remove element
stack.get()
stack.get()
stack.get()
stack.get(timeout=1)
# peek element
pe = stack.get()
# isEmpty
stack.empty()
stack.full()
stack.not_full
stack.not_empty
