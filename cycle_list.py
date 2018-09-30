class Node:
    def __init__(self, val):
        self.value = val 
        self.next = None

    def setNext(self, new_next):
        self.next = new_next

    def setVal(self, new_val):
        self.value = new_val

    def getNext(self):
        return self.next


class LinkedList:
    def __init__(self, data = None):
        self.head = Node(data)
        self.next = None

    def getNext(self):
        return self.next

    def append(self, new_val):
        curr = self.head
        while (curr.next):
            curr = curr.next
        curr.next = Node(new_val)

    def prepend(self, new_val):
        temp = Node(new_val)
        temp.setNext(self.head)
        self.head = temp

    def insert(self, node_val, new_val):
        curr = self.head
        prev = None

        while (curr.value != node_val):
            prev = curr
            curr = curr.next
        temp = Node(new_val)
        temp.setNext(prev.next)
        prev.next = temp

    def printList(self):
        curr = self.head
        while (curr.next):
            print(str(curr.value), end ='->')
            curr = curr.next
        print(str(curr.value))

    



if __name__ == "__main__":
    d = LinkedList(5)
    d.append(7)
    d.append(10)
    d.prepend(7)
    d.prepend(20)
    d.insert(5, 3)
    d.printList()


    

