#Doubly linked List 
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self, data) :
        node = Node(data)
        self.head = node
        self.tail = self.head
        self.length = 1 

    def append(self, data):
        node = Node(data)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1

    def prepend(self, data):
        node = Node(data)
        temp = self.head 
        temp.prev = node
        node.next = temp
        self.head = node 
        self.length += 1

    def printList(self):
        array = []
        currentNode = self.head
        while currentNode : 
            array.append(currentNode.data)
            currentNode = currentNode.next
        print(array)

    def printRevList(self):
        array = []
        currentNode = self.tail
        while currentNode:
            array.append(currentNode.data)
            currentNode = currentNode.prev
        print(array)

    def insert(self, index, data):
        #check prams if 
        newNode = Node(data)
        currNode = self.head
        prevNode = None
        if index == 0:
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
            return
        for i in range(index):
            prevNode = currNode
            currNode = currNode.next
        prevNode.next = newNode
        currNode.prev = newNode
        newNode.next = currNode
        newNode.prev = prevNode
        self.length += 1
        return

    #remove by data course did remove by index 
    #what about duplicates? not addressed here 
    def remove(self, data):
        currNode = self.head
        prevNode = None
        while currNode:
            if currNode.data == data:
                temp = currNode.next
                if not prevNode:
                    self.head = currNode.next
                    self.head.prev = None
                else:
                    prevNode.next = temp
                    temp.prev = prevNode
                del currNode
                self.length -= 1
                return 

            prevNode = currNode
            currNode = currNode.next