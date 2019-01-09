class Node:
    next = None
    nodeVal = None 
    def __init__(self, nodeVal):
        self.next = None
        self.nodeVal = nodeVal        

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtLocation(self,nodeToInsert):
        nodeToTraverse = self.head
        #find where does the node fit 

        while nodeToInsert.nodeVal >= nodeToTraverse.nodeVal and nodeToTraverse.next != None:
            nodeToTraverse = nodeToTraverse.next

        if nodeToInsert.nodeVal >= nodeToTraverse.nodeVal and nodeToTraverse.next == None:
            nodeToTraverse.next = nodeToInsert

        else:
            #IMPORTANT: if you copy the variable, eg. tempNode = nodeToTraverse, if nodeToTraveres is updated, tempNode is updated as well
            tempNode = Node(nodeToTraverse.nodeVal)
            tempNode.next = nodeToTraverse.next 
            #tempNode = nodeToTraverse
            nodeToTraverse.nodeVal = nodeToInsert.nodeVal
            nodeToTraverse.next = tempNode

        self.traverseNode(self.head)
    
    def traverseNode(self,head):
        #traverse the linked list
        traverseNode = head
        i = 0
        while traverseNode != None:
            print("Node{0}: ".format(i) + str(traverseNode.nodeVal))
            i += 1
            traverseNode = traverseNode.next

    def removeNode(self, val):
        #if 1st node is to be removed
        if self.head.nodeVal == val:
            self.head = self.head.next

        else:
            traverseNode = self.head.next
            previousNode = self.head

            #IMPORTANT: match the value of traverseNode and not travereseNode.value or traveseNode.next
            while traverseNode != None:
                if(traverseNode.nodeVal == val):
                    #remove the node
                    previousNode.next = traverseNode.next

                traverseNode = traverseNode.next
                previousNode = previousNode.next
        self.traverseNode(self.head)

if __name__ == "__main__":
    s = SingleLinkedList()

    #create 1st node
    n = Node(3)

    if n.next == None:
        #1st node. Make it head.
        s.head = n
    
    #2nd node
    n1 = Node(5)
    n.next = n1

    #3rd node
    n2 = Node(7)
    n1.next = n2

    print("Traverese node:")    
    s.traverseNode(s.head)
 
    n3 = Node(6)

    print("Insert node:")   
    s.insertNodeAtLocation(n3)

    print("Remove node:")   
    s.removeNode(3)

    print("Trial:")
     

