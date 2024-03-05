class Node:
    def __init__(self,data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
    

class binarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data, root = None):
        current = root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        
        newnode = Node(data, parent)    
        if self.root is None:
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
    binarySearchTree = 
    for i in range(10000):







