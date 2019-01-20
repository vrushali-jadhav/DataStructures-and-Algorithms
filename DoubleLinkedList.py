class Node:
    def __init__(self,next,prev,value):
        self.next = next
        self.prev = prev
        self.val = value
    
class DoubleLinkedList: 
    head = None
    tail = None

    def insertNode(self,value):
        #1st node
        if self.head == None:
            n = Node(None,None,value)
            self.head = n
            self.tail = n
            print("Node {0} inserted1!".format(n.val))
            return None

        #2nd node (just 1 node present at the moment)
        if self.head == self.tail:
            n = Node(None,self.head,value)
            self.head.next = n
            self.tail = n
            print("Node {0} inserted2!".format(n.val))
            return None

        #rest of the nodes
        n = Node(None,self.tail,value)
        self.tail.next = n
        self.tail = n

        print("Node {0} inserted3!".format(n.val))

    def traverseLinkedList(self):
        tmp = Node(None,None,None)
        tmp = self.head
        
        counter = 0
        while tmp!= None:
            print("Node {0} is: {1}".format(counter,tmp.val))
            counter += 1
            tmp = tmp.next
            

if __name__ == "__main__":
    d = DoubleLinkedList()

    d.insertNode(3)
    d.insertNode(5)
    d.insertNode(0)
    d.insertNode(8)
    d.insertNode(1)
    d.insertNode(25)

    d.traverseLinkedList()
