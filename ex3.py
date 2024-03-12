import sys


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
        if data.isdigit():
            self.root = self.insert_number(self.root, data)
        elif data in ['+', '-', '*', '/']:
            self.root = self.insert_operator(self.root, data)

    
        
    def insert(self, data):
        current = self.root
        parent = None
    
        while current is not None:
            parent = current
            if current.right is None:
                current.right = Node(data, parent)
                return
            elif current.left is None:
                current.left = Node(data, parent)
                return
            current = current.left
        if parent is None:
            self.root = Node(data)
  
    def eval(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

        left = self.eval(root.left)
        right = self.eval(root.right)

        if root.data == '+':
            root.data = int(left)+ int(right)
        elif root.data == '-':
            root.data = int(left)- int(right)
        elif root.data == '*':
            root.data = int(left) * int(right)
        elif root.data == '/':
            root.data = int(left)/int(right)

        return root.data

       
   
    # def insertSubTree(self, subtree):
    #     current = self.root
    #     parent = None

    #      while current is not None:
    #         parent = current
    #         if data <= current.data:
    #             current = current.left
    #         else:
    #             current = current.right
        

if len(sys.argv) != 2:
    sys.exit(1)

operations_list = ['+','-','*','/']
expression = sys.argv[1]
tree = binarySearchTree()
# expression = "5 + ( 3 /1) "
digitsAndOpsOnly = []
stack = []
print(expression)
i = 0


while i<len(expression):
    
    if expression[i].isdigit():
        num = ''
        while i<len(expression) and expression[i].isdigit():
            num += expression[i]
            i+=1
           
        digitsAndOpsOnly.append(num)
        
    # boundary check after possibly incrementing i to the max above
    if i>= len(expression):
        break
    
    if expression[i] in operations_list:
        digitsAndOpsOnly.append(expression[i])
    
    if i == len(expression) -1  or expression[i] ==')':
        
        if len(digitsAndOpsOnly) >= 3:
            oplist = []
          
            j = 3
            while j > 0:
                if digitsAndOpsOnly[-j].isdigit():
                    stack.append(digitsAndOpsOnly[-j])
                elif digitsAndOpsOnly[-j] in operations_list:
                    oplist.append(digitsAndOpsOnly[-j])
                j -=1
            oplistLength = len(oplist)
            for c in range(oplistLength):
                stack.append(oplist.pop())
            for k in range(3):
                digitsAndOpsOnly.pop()
           

            
          
        elif len(digitsAndOpsOnly) == 2:
            op = ''
            j = 2
            while j > 0:
                if digitsAndOpsOnly[-j].isdigit():
                    stack.append(digitsAndOpsOnly[-j])
                else:
                    op = digitsAndOpsOnly[-j]
                j -=1
            stack.append(op)
           
            digitsAndOpsOnly.pop()
            digitsAndOpsOnly.pop()
        elif len(digitsAndOpsOnly) ==1:
            stack.append(digitsAndOpsOnly.pop())
        
    


    i+=1
k = len(digitsAndOpsOnly)

saved_k = k
if k > 0:
    oplist = []
    while k>0:
        if digitsAndOpsOnly[-k].isdigit():
            stack.append(digitsAndOpsOnly[-k])
        elif digitsAndOpsOnly[-k] in operations_list:
            oplist.append(digitsAndOpsOnly[-k])
        k-=1
    oplistLength = len(oplist)
    for c in range(oplistLength):
        stack.append(oplist.pop())


           

original_len = len(stack)
for i in range(original_len):
    tree.insert(stack.pop())

print(tree.eval(tree.root))

