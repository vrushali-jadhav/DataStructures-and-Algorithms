#this tree will take numbers as input from a list
#1st element will be the root 
#smaller numbers will go to the left, larger will go to the right

class Node:
    def __init__(self,value=None):
        self.right = None
        self.left = None
        self.value = value

class TreeStructure:
    root = None
    queue = [] #for deapth 1st traversal
    stack = [] #for breath 1st traversal

    def addNode(self,value):
        if self.root == None:
            self.root = Node(value)
            print("Root node {0} added.".format(value))
        else:   
            self.addNonRootNodes(value,self.root)
    
    def addNonRootNodes(self,value,cur_root):
        #If it's a terminal node
        if value < cur_root.value:
            if cur_root.left == None:
                cur_root.left = Node(value)
                print("Left node {0} added.".format(value))
                return None
            else:
                self.addNonRootNodes(value,cur_root.left)    

        if value > cur_root.value:
            if cur_root.right == None:
                cur_root.right = Node(value)
                print("Right node {0} added.".format(value))
                return None
            else:
                self.addNonRootNodes(value,cur_root.right)

    def printTree(self,root):
        print("Parent root: {0}".format(root.value))
        self.printRestOfTheTree(self.root)

    def printRestOfTheTree(self,cur_root):
        if cur_root != None:
            self.printRestOfTheTree(cur_root.left)
            print("Node: {0}".format(cur_root.value))
            self.printRestOfTheTree(cur_root.right)
    
    def depthFirstTraversal(self,root):
        print("Parent root: {0}".format(root.value))
        self.depFirTravRestNodes(root)

    def depFirTravRestNodes(self,cur_root):
        if cur_root.left != None:
            self.queue.insert(0,cur_root.left.value)
            self.depFirTravRestNodes(cur_root.left)

        if cur_root.right != None:
            self.queue.insert(0,cur_root.right.value)
            self.depFirTravRestNodes(cur_root.right)

    def breathFirstTraversal(self,root):
        print("Parent root: {0}".format(root.value))
        self.breFirTravRestNodes(root)

    def breFirTravRestNodes(self,cur_root):
        """ if cur_root.left!=None and cur_root.right!=None:
            self.stack.append(cur_root.left.value)
            self.stack.append(cur_root.right.value)
            
        self.breFirTravRestNodes(cur_root.left)
        self.breFirTravRestNodes(cur_root.right) """
        self.queue.append(cur_root)
        while self.queue:
            if(self.queue[0].left!=None):
                self.queue.append(self.queue[0].left)
                print("Node: {0}".format(self.queue[0].left.value))
            if(self.queue[0].right!=None):
                self.queue.append(self.queue[0].right)
                print("Node: {0}".format(self.queue[0].right.value))
            self.queue.pop(0)

    
if __name__=="__main__":
    inputToTree = [8,3,1,6,4,10,14,13,7]
    t = TreeStructure()
    count = 0

    while count <= (len(inputToTree)-1):
        t.addNode(inputToTree[count])
        count = count+1 
    
    print("\nPrinting the tree:")
    t.printTree(t.root)

    print("\nDepth 1st traversal:")
    t.depthFirstTraversal(t.root)   
    while t.queue:
        print("Node: {0}".format(t.queue.pop()))

    print("\nBreath 1st traversal:")
    t.breathFirstTraversal(t.root)   
    while t.stack:
        print("Node: {0}".format(t.stack.pop(0)))