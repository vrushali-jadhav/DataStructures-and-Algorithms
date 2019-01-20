class QueueImplementation:
    queue = []

    def addToQueue(self,element):
        self.queue.insert(0,element)
        print("Element '{0}' inserted to the queue.".format(element))

    def getElementFromTheQueue(self):
        return self.queue.pop()


if __name__ == "__main__":
    q = QueueImplementation()

    elementsToBeAddedToQueue = [2,4,5,10,17,90,1,0]
    print("ELements to be added to the queue are: {0}".format(elementsToBeAddedToQueue))
    index = 0

    while index<=(len(elementsToBeAddedToQueue)-1):
        #add every element from the list to the queue
        q.addToQueue(elementsToBeAddedToQueue[index])
        index += 1

    print("The queue is: {0}".format(q.queue))

    #pop elements one by one
    i = 0
    while q.queue:
        print("Element '{0}' popped. Queue is: {1}".format(q.getElementFromTheQueue(),q.queue)) 

    

      

    

