class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData
    
    def setNext (self, newNext):
        self.next = newNext
    
    def setPrev(self, newPrev):
        self.prev = newPrev
    

class LinkedList(Node):
    def __init__(self, data=None):
        self.head = Node(data)
        
       #Node.__init__(data)

    def isEmpty(self):
        return self.head.getData() == None

    def addFront (self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp
    
    def addEnd(self, data):
        temp = Node(data)
        curr = self.head
        while (curr.next):
            curr = curr.next
        curr.setNext(temp)

    def insertPrev(self, data):
        if self.prev == None:
            self.addFront(data)
        else:

            prev = self.prev
            


    def insertAfter(self):
        pass

    def printList(self):
        curr = self.head
        while (curr.next):
            curr_val = curr.getData()
            print (str(curr_val)+ " -> ", end="")
            curr = curr.next 
        print (curr.getData())


if __name__ == "__main__":
    ll = LinkedList()
    print (ll.isEmpty())
    ll.printList()
    linked = LinkedList(5)
    linked.addFront(33)
    linked.addFront(44)
    linked.addEnd(11)
    linked.printList()


