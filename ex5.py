# 1. Implement a class ListPriorityQueue which implements a priority queue using a linked
# list: [0.2 pts]
# • enqueue must insert an element in order
# • dequeue must retrieve the first (smallest) element on a list

class Node:
    def __init__(self, data, next):
        self._data = data
        self._next = next
    def getData(self):
        return self._data
    def setData(self, data):
        self._data = data
    def getNext(self):
        return self._next
    def setNext(self, next):
        self._next = next
    def toString(self):
        return str(self._data)

class ListPriorityQueue:
    def __init__(self):
        self._head = None

    def enqueue(self, value):
        if self._head == None: # if inserting to empty list
            self._head = Node(value, None)
            return
        else:
            new_node = Node(value, None)
            current = self._head
            while new_node.getData() > current.getData(current.getNext()):
                current.setNext(current.getNext())
            new_node.setNext(current.getNext())
            current.setNext(new_node)

    def dequeue(self):
        if self._head == None:
            print("Queue is empty" )
            return
        if self._head.getNext() == None:
            self._head == None
        else:
            temp = self._head.getData()
            delete = self._head
            self._head = self._head.getNext()
            delete._next = None
            delete = None
            return temp

# 2. Implement a class HeapPriorityQueue which implements a priority queue using a heap:
# [0.2 pts]
# 1. Can reuse implementation from Exercise 4

