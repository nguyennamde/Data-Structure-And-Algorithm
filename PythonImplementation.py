class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def printLinkedList(self):
        dummyNode = self.head
        while dummyNode:
            print(dummyNode.val)
            dummyNode = dummyNode.next
        if self.head is None:
            print("No have any Node in LinkedList")
    def AddAtBegin(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    def AddAtEnd(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        dummyNode = self.head
        while dummyNode.next:
            dummyNode = dummyNode.next
        dummyNode.next = node
    def createLinkedList(self,list_):
        for val in list_:
            self.AddAtEnd(val)
    def insertAfterNodeGiven(self, NodeGiven, val):
        node = Node(val)
        if self.head is None:
            print("LinkedList is empty")
            return
        node.next = NodeGiven.next
        NodeGiven.next = node
    def length(self):
        count = 0
        dummyNode = self.head
        while dummyNode:
            count += 1
            dummyNode = dummyNode.next
        print(count)
    def removeAnNode(self, val):
        temp = self.head
        if temp.val == val and temp is not None:
            self.head = temp.next
            return
        while temp is not None:
            if temp.val == val:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None






