import timeit
import random
class Node:
    def __init__(self,data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
    

class binarySearchTree:
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
        

        newnode = Node(data, parent)    
        if parent is None:
            self.root = newnode
        elif data <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode

        return newnode
    
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
    

def main():
    firstTree = binarySearchTree()
    arr = [i for i in range(10000)]
    for element in arr:
        firstTree.insert(element)
    timeForAllSearch = 0
    for i in range(10000):
        timeTaken = timeit.timeit(lambda:firstTree.search(i),number = 10)/10
        timeForAllSearch += timeTaken

    print('Total time for all elements: ', timeForAllSearch, 's')
    print('Average time: ', timeForAllSearch/10000, 's')

    # with shuffling:

    random.shuffle(arr)
    secondTree = binarySearchTree()
    for element in arr:
        secondTree.insert(element)
    timeForAllSearch = 0
    for i in range(10000):
        timeTaken = timeit.timeit(lambda:secondTree.search(i),number = 10)/10
        timeForAllSearch += timeTaken

    print('Total time for all elements (with shuffling): ', timeForAllSearch, 's')
    print('Average time (with shuffling): ', timeForAllSearch/10000, 's')





if __name__ == "__main__":
    main()


#4. Discuss the results. Which approach is faster? Why? [0.2 pts]
# The shuffled insertion approach was faster with an average search time of 6.163979205302902e-07s per element. This is the case since insertion to a binary tree
#  with sorted data may create an unbalanced tree as every element that is being inserted is greater than the previously inserted node, causing the new node to be 
#  inserted always to the right side of its parent. This results in a tree that has an unequal number of nodes on its left and right.
#  Search through a tree like this is comparable to a search through a linked list, O(n). For the shuffled insertion, there is better chance for a balanced tree, as it is not
#  guaranteed that the node being inserted is always greater than the previously inserted node. Due to this, the time complexity of the search is O(logn) as the search space is
#  halved every iteration. Thus, it can be concluded that search with shuffled insertion is quicker.

