class StackImplementation:
    stack = []

    def addTostack(self,element):
        self.stack.insert(0,element)
        print("Element '{0}' inserted to the stack.".format(element))

    def getElementFromThestack(self):
        return self.stack.pop(0)


if __name__ == "__main__":
    s = StackImplementation()

    elementsToBeAddedTostack = [2,4,5,10,17,90,1,0]
    print("ELements to be added to the stack are: {0}".format(elementsToBeAddedTostack))
    index = 0

    while index<=(len(elementsToBeAddedTostack)-1):
        #add every element from the list to the stack
        s.addTostack(elementsToBeAddedTostack[index])
        index += 1

    print("The stack is: {0}".format(s.stack))

    #pop elements one by one
    i = 0
    while s.stack:
        print("Element '{0}' popped. Stack is: {1}".format(s.getElementFromThestack(),s.stack)) 

    

      

    

