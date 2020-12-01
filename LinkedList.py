class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, data) :
        node = Node(data)
        self.head = node
        self.tail = self.head
        self.length = 1 

    def append(self, data):
        node = Node(data)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, data):
        node = Node(data)
        temp = self.head 
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
        newNode.next = currNode
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
                else:
                    prevNode.next = temp 
                del currNode
                self.length -= 1
                return 

            prevNode = currNode
            currNode = currNode.next


    #reverse 
    def reverse(self):
        current_node = self.head
        if current_node == None: 
            return current_node
        self.tail = self.head
        first = self.head 
        second = current_node.next
        while(second):
            temp = second.next
            second.next = first 
            first = second
            second = temp

        self.head.next = None
        self.head = first

myLinkedList = LinkedList(3)
myLinkedList.append(5)
myLinkedList.append(6)
myLinkedList.prepend(2)
myLinkedList.insert(2,4)
myLinkedList.insert(0,1)
myLinkedList.insert(8,7)
myLinkedList.remove(1)
print(myLinkedList.head.data)
myLinkedList.printList()
myLinkedList.reverse()
myLinkedList.printList()
