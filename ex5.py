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
        self._before = None
        self._after = None

    def enqueue(self, value):
        new_node = Node(value, None)
        if (self._head is None) or (value <= self._head.getData()) :
            new_node.setNext(self._head)
            self._head = new_node
        else:
            self._before = self._head
            self._after = self._head.getNext()
            while (self._after is not None) and (value > self._after.getData()):
                self._before = self._after
                self._after = self._after.getNext()

            new_node.setNext(self._before.getNext())
            self._before.setNext(new_node)

            
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
        
    def print(self): # used for testing
        current = self._head
        while current is not None:
            print(current.toString())
            current = current.getNext()

# 2. Implement a class HeapPriorityQueue which implements a priority queue using a heap:
# [0.2 pts]
# 1. Can reuse implementation from Exercise 4

class HeapPriorityQueue:
    def __init__(self):
        self._array = []
        self._size = 0

    def enqueue(self, element):
    # adds an element to the heap (while correctly maintaining the heap's properties)
        if self._size == 0:
            self._array.append(element)
            self._size += 1
            return
        
        self._array.append(element)
        self._size += 1
        current_indx = self._size - 1
        while(element < self._array[(current_indx - 1) // 2]  and  current_indx > 0):
            self._array[current_indx], self._array[(current_indx - 1) // 2] = self._array[(current_indx - 1) // 2], self._array[current_indx]
            current_indx = (current_indx - 1) // 2

        return

    def dequeue(self):
        temp = self._array[0] # root node
        if self._size == 0:
            print("Cannot delete from an empty heap.")
            return

        if self._size == 1:
            self._size = 0
            self._array = []
            return temp

        self._array[0], self._array[self._size - 1] = self._array[self._size - 1], self._array[0]
        self._array.pop()
        self._size -= 1

        i = 0
        min_indx = 0
        while(True):
            left_child = (2 * i) + 1
            right_child = (2 * i) + 2
            
            if (left_child < self._size) and (self._array[left_child] < self._array[min_indx]):
                min_indx = left_child
            if (right_child < self._size) and (self._array[right_child] < self._array[min_indx]):
                min_indx = right_child
            if (min_indx != i):
                self._array[i], self._array[min_indx] = self._array[min_indx], self._array[i]
                i = min_indx
            else:
                break
        return temp
    

# 3. Measure execution time of both implementations [0.4 pts]
# 1. Generate a random list of 1000 tasks, where a task is enqueue of a random integer with
# probability 0.7, and dequeue with probability 0.3
    
import random

def generate_list():
    num_enqueue = 0
    num_dequeue = 0
    operations_list = []

    while num_enqueue != 700:
        op = []
        op.append('enqueue')
        op.append(random.randint(0, 100))
        operations_list.append(op)
        num_enqueue += 1
    while num_dequeue != 300:
        op = []
        op.append('dequeue')
        operations_list.append(op)
        num_dequeue += 1
    random.shuffle(operations_list)
    return operations_list

# 2. Use timeit to measure how long it takes for each implementation to process the list. Return
# overall time and average time per task
import timeit

def arraysPerformance(task, arr):
    for operation in task:
        if task[0] == 'enqueue':
            arr.enqueue(task[1])
        else:
            arr.dequeue()

def linkedListsPerformance(task, list):
    for operation in task:
        if task[0] == 'enqueue':
            list.enqueue(task[1])
        else:
            list.dequeue()

array_heap = HeapPriorityQueue()
linked_list_heap = ListPriorityQueue()

tasks = generate_list()

array_times = []
linkedlist_times = []

for task in tasks:
    array_times.append(timeit.timeit(lambda: arraysPerformance(task, array_heap), number = 1))
    linkedlist_times.append(timeit.timeit(lambda: linkedListsPerformance(task, linked_list_heap), number = 1))

sum_array_times = sum(array_times)
sum_list_times = sum(linkedlist_times)

avg_array_times = sum_array_times/1000
avg_list_times = sum_list_times/1000

print("Total array implementation time: ", sum_array_times)
print("Avg array implemenation time: ", avg_array_times)

print("Total linked list implementation time: ", sum_list_times)
print("Avg linked list implemenation time: ", avg_list_times)

# 4. Discuss the results: which implementation is faster? Why do you think is that? [0.2 pts]

# The array implementation is about 10 times faster than the linked list implementation. This is most
# likely because linked list insertion is O(n) while heap insertion is O(logn). Linked lists must traverse 
# through all its elements until it reaches the desired place to insert. This incurs a worst case cost of O(n).
# In the array implementation, however, an insertion is only O(logn) in the worst case, because at worst, 
# the new element will have to swap with its parent logn times. Additionally, to access
# an element, an array can use indexing while a linked list has to traverse through its values.
