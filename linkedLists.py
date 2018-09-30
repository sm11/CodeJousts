class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData
    
    def setNext (self, newNext):
        self.next = newNext
    
    

class LinkedList(Node):
    def __init__(self, data):
        self.head = Node(data)


    def isEmpty(self):
        return self.head == None

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
    
    def printList(self):
        curr = self.head
        while (curr.next):
            print (str(curr.getData())+" -> ", end="")
            curr = curr.next 
        print (curr.getData())


if __name__ == "__main__":
    linked = LinkedList(5)
    linked.printList()
    linked.addFront(33)
    linked.addFront(44)
    linked.addEnd(11)
    linked.printList()


