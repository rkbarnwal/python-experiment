class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def getData(self):
        return self.data
    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.currentSize = 0

    def size(self):
        return self.currentSize

    def isEmpty(self):
        return self.size() == 0

    def add(self, value):
        if self.isEmpty():
            self.head = Node(value, None)
            self.tail = self.head
        else:
            self.tail.setNext(Node(value,None))
            self.tail = self.tail.getNext()
        self.currentSize += 1
        return True




