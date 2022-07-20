#https://leetcode.com/problems/design-linked-list/
class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.length = 0
        

    def get(self, index: int) -> int:
        
        if self.length <= index or index < 0:
            return -1
        
        itr = self.head
        for _ in range(index + 1):
            itr = itr.next
        return itr.val
            
        

    def addAtHead(self, val: int) -> None:
        
        node = Node(val, self.head.next)
        self.head.next = node
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        
        if self.length == 0:
            self.head.next = Node(val)
            
        itr = self.head
        for _ in range(self.length):
            itr = itr.next
            
        itr.next = Node(val, None)
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if self.length == index:
            self.addAtTail(val)
            return
        if self.length < index:
            return
        itr = self.head
        for _ in range(index ):
            itr = itr.next
        node = Node(val, itr.next)
        itr.next = node
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        
        if self.length <= 0 or self.length <= index:
            return
        
        itr = self.head
        for _ in range(index ):
            itr = itr.next
        
        itr.next = itr.next.next
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
