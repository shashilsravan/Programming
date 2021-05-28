class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def printList(self):
        printVal = self.headval
        while printVal is not None:
            print(printVal.dataval)
            printVal = printVal.nextval

    def atBeginning(self, newData):
        newNode = Node(newData)
        newNode.nextval = self.headval
        self.headval = newNode

    def atEnd(self, newData):
        newNode = Node(newData)
        if self.headval is None:
            self.headval = newNode
            return
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = newNode

    def atMiddle(self, middle, newData):
        newNode = Node(newData)
        if middle is None:
            print("The mentioned node is absent")
            return
        newNode.nextval = middle.nextval
        middle.nextval = newNode

    def removeNode(self, removeKey):
        head = self.headval

        if head is not None:
            if head.dataval == removeKey:
                self.headval = head.nextval
                head = None

        while head is not None:
            if head.dataval == removeKey:
                break
            prev = head
            head = head.nextval

        if head == None:
            return
        prev.nextval = head.nextval
        head = None

lis1 = SLinkedList()
lis1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thurs")

lis1.headval.nextval = e2
e2.nextval = e3

lis1.atBeginning("Sun")
lis1.atEnd("Fri")
lis1.atMiddle(lis1.headval.nextval.nextval,"Wed")
lis1.removeNode("Fri")
lis1.printList()
