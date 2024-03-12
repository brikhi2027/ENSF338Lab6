import timeit
import random
#1. 
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right
        
        newNode = Node(data, parent)
        if parent is None:
            self.root = newNode
        elif data <= parent.data:
            parent.left = newNode
        else:
            parent.right = newNode
        return newNode
    
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None

def binary_search(arr, first, last, key):
    if first == last:
        if arr[first] > key:
            return first
        else:
            return first
    if first > last:
        return first
    if first <= last:
        mid = (first + last) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binary_search(arr, first, mid - 1, key)
        elif key > arr[mid]:
            return binary_search(arr, mid + 1, last, key)

#2. 
tree = BinarySearchTree()
arr = [i for i in range(10000)]
random.shuffle(arr)

for data in arr:
    tree.insert(data)

totalSearchTime = 0
for i in range(10000):
    searchTime = timeit.timeit(lambda: tree.search(i), number = 10)/10
    totalSearchTime += searchTime

print('BST Total Search Time:', totalSearchTime, 's')
print('BST Average Search Time:', totalSearchTime/10000, 's')

#3. 
arr.sort()

binarySearchTotalTime = 0
for i in range(10000):
    binarySearchTime = timeit.timeit(lambda: binary_search(arr, 0, 10000, i), number = 10)/10
    binarySearchTotalTime += binarySearchTime

print('Binary Search Total Search Time:', binarySearchTotalTime, 's')
print('Binary Search Average Search Time:', binarySearchTotalTime/10000, 's') 

#4. Searching using a Binary Search Tree is faster than Binary Search because the nodes in a Binary Search Tree
#are organized so that the left child is less than or equal to the parent node and the right child is greater than 
#the parent node. This reduces the searching time in a Binary Search Tree because if it is known that a given 
#value is greater or less than a node, the other half of the tree can be disregarded. This is more efficient than
#using Binary Search on a sorted array as Binary Search first determines the midpoint for each sub-array, does 
#a comparison with the given value, and then recursively calls itself. 
