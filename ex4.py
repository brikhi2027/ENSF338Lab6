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
            self._size += 1

        for i in range(n):
            max_indx = n - 1
            for j in range(n-1, i):
                if self._array[j] > self._array[max_indx]:
                    max_indx = j
                self._array[i], self._array[max_indx] = self._array[max_indx], self._array[i]
        return self._array
    
    def enqueue(self, element):
    # adds an element to the heap (while correctly maintaining the heap's properties)
        self._array.append(element)
        self._size += 1
        current_indx = self._size - 1
        while(element < self._array[(current_indx - 1) // 2]):
            self._array[current_indx], self._array[(current_indx - 1) // 2] = self._array[(current_indx - 1) // 2], self._array[current_indx]
            current_indx = (current_indx - 1) // 2

    def dequeue(self, element):
    # removes an element from the heap (while correctly maintaining the heap's properties)
        temp = element
        pos = -1

        if self._size == 1:
            self._array = []
            return temp
        
        i = 0
        for i in range(0, self._size): # find the position of the element to be removed
            if (self._array[i] == element):
                pos = i
                break
        if pos == -1: 
            print("The element you want to remove does not exist.")
        self._array[i], self._array[self._size - 1] = self._array[self._size - 1], self._array[i] # swap the node to be deleted with the last child
        self._array.pop() # delete the last child
        self._size -= 1 

        current_indx = i
        while(element < self._array[(current_indx - 1) // 2]): # move the element up the tree if its smaller than its parents
            self._array[current_indx], self._array[(current_indx - 1) // 2] = self._array[(current_indx - 1) // 2], self._array[current_indx]
            current_indx = current_indx // 2
        return temp


# 2. Write 3 tests for the following cases: [0.1 pts]
#   • Input array is already a correctly sorted heap
#   • Input array is empty
#   • Input array is a long, randomly shuffled list of integers
# Each test must consist of running the code on an appropriate input, and comparing the
# output (heapified array) with the expected value.
import random

# 1. already sorted array

arr1 = [1, 2, 4, 6, 10, 15]
test1 = Heap(arr1)
# heapifying
test1Output = test1.heapify()
print("TEST1")
print("Expected: ", arr1)
print("Output:   ", test1Output,'\n')
# enqueuing
test1enqueue = test1.enqueue(3)
print("Expected: [1, 2, 3, 6, 10, 15, 4]")
print("Output:  ", test1._array,'\n')
# dequeueing
test1dequeue = test1.dequeue(4)
print("Expected: [1, 2, 3, 6, 10, 15]")
print("Output:  ", test1._array,'\n')



# 2. empty array
arr2 = []
test2 = Heap(arr2)
# heapifying
test2Output = test2.heapify()
print("TEST2")
print("Expected: ", arr2)
print("Output:   ", test2Output,'\n')
# enqueuing
test2.enqueue(1)
print("Expected: [1]")
print("Output:  ", test2._array,'\n')
# dequeueing
test2.dequeue(1)
print("Expected: []")
print("Output:  ", test2._array,'\n')


# 3. long randomly shuffled list of integers

arr3 = []
for j in range(20):
    arr3.append(random.randint(0, 100))

arr3Copy = arr3
arr3Copy.sort()
test3 = Heap(arr3)
# heapifying
test3Output = test3.heapify()
print("TEST3")
print("Expected: ", arr3Copy)
print("Output:   ", test3Output)