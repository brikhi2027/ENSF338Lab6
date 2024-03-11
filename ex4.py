# 1. Write a class named which uses a Python array as a storage backend for heap nodes
class Heap:
    def __init__(self, inputArray):
        self._array = []
        self.inputArray = inputArray
        self._size = 0

    def heapify(self):
    # receives as input an array of integers, stores into the internal array, and turn it into a heap
        n = len(self.inputArray)
        for k in range(n):
            self._array.append(self.inputArray[k])
            k += 1

        for i in range(n):
            max_indx = n - 1
            for j in range(n-1, i):
                if self._array[j] > self._array[max_indx]:
                    max_indx = j
                self._array[i], self._array[max_indx] = self._array[max_indx], self._array[i]
        return self._array
    
    def enqueue(self, element):
    # adds an element to the heap (while correctly maintaining the heap's properties)
        self._array[self._size] = element
        current_indx = self._size
        while(element < self._array[current_indx // 2]):
            self._array[current_indx], self._array[current_indx // 2] = self._array[current_indx // 2], self._array[current_indx]
            current_indx = current_indx // 2

    def dequeue(self, element):
    # removes an element from the heap (while correctly maintaining the heap's properties)
        temp = element
        pos = -1

        for i in range(0, self._size): # find the position of the element to be removed
            if (self._array[i] == element):
                pos = i
            else:
                print("The element you want to remove does not exist.")
        self._array[i], self._array[self._size - 1] = self._array[self._size - 1], self._array[i] # swap the node to be deleted with the last child
        self._size -= 1 # delete the last child

        current_indx = i
        while(element < self._array[current_indx // 2]): # move the element up the tree if its smaller than its parents
            self._array[current_indx], self._array[current_indx // 2] = self._array[current_indx // 2], self._array[current_indx]
            current_indx = current_indx // 2
        return temp


# 2. Write 3 tests for the following cases: [0.1 pts]
#   • Input array is already a correctly sorted heap
#   • Input array is empty
#   • Input array is a long, randomly shuffled list of integers
# Each test must consist of running the code on an appropriate input, and comparing the
# output (heapified array) with the expected value.
import random

# already sorted array
arr1 = [1, 2, 4, 6, 10, 15]
test1 = Heap(arr1)
test1Output = test1.heapify()
print("Expected: ", arr1)
print("Output:   ", test1Output)

# empty array
arr2 = []
test2 = Heap(arr2)
test2Output = test2.heapify()
print("Expected: ", arr2)
print("Output:   ", test2Output)

# long randomly shuffled list of integers
arr3 = []
for j in range(20):
    arr3.append(random.randint(0, 100))

arr3Copy = arr3
arr3Copy.sort()
test3 = Heap(arr3)
test3Output = test3.heapify()
print("Expected: ", arr3Copy)
print("Output:   ", test3Output)