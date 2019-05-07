#Session 11
#Linked_Lists_and_Stacks

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None    #top stores a Node
    def push(self, x):
        new_node=Node(x)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        popped=self.top.data
        self.top=self.top.next
    def peek(self):
        return self.top.data
    def is_empty(self):
        return self.top==None

#NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input: exec(line)

#Balanced_Parentheses

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None    #top stores a Node
    def push(self, x):
        new_node=Node(x)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        popped=self.top.data
        self.top=self.top.next
    def peek(self):
        return self.top.data
    def is_empty(self):
        return self.top==None
str=input()
stk=Stack()
error=False
for sym in str:
    if sym=="(" or sym=="[" or sym=="{" or sym=="<":
        stk.push(sym)
    else:
        if stk.is_empty():
            error=True
        elif (stk.peek()=="(" and sym==")") or (stk.peek()=="[" and sym=="]") or (stk.peek()=="{" and sym=="}") or (stk.peek()=="<" and sym==">"):
            stk.pop()
        else:
            error=True
print(not error)

#Doubly_Linked_Lists_and_Queue

class Node:
    def __init__(self, init_data): 
       self.data = init_data 
       self.next = None 
       self.previous = None 

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
    def enqueue(self, x):
        if self.back==None:
            self.front=Node(x)
            self.back=self.front
        else:
            self.back.next=Node(x)
            self.back=self.back.next
    def dequeue(self):
        if self.back==None:
            return None
        else:
            temp=self.front.data
            self.front=self.front.next
        return temp
    def is_empty(self):
        return self.front==None

#NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input: exec(line)
