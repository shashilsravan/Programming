class MyLinkedList(object):

    def __init__(self):
        self.v = list()

    def get(self, index):
        return self.v[index] if index < len(self.v) else -1

    def addAtHead(self, val):
        self.v.insert(0, val)

    def addAtTail(self, val):
        self.v.append(val)

    def addAtIndex(self, index, val):
        self.v.insert(index, val)

    def deleteAtIndex(self, index):
        if index < len(self.v):
            self.v.pop(index)