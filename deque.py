#Question =>
class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k + 1
        self.deque = [0] * self.capacity
        self.front = 0
        self.rear = 0
        

    def insertFront(self, value: int) -> bool:
        

        if  self.isFull():
            return False
            
        self.deque[ (self.front - 1) % self.capacity] = value
        self.front = (self.front - 1)% self.capacity
        return True

   
        
        
    def insertLast(self, value: int) -> bool:
        
        
        if self.isFull():
            return False
            
        self.deque[ self.rear ] = value
        self.rear = (self.rear + 1)%self.capacity    
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
            
        self.front = (self.front+1)%self.capacity
        return True
        
            
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear-1)%self.capacity
        return True
        
    def getFront(self) -> int:
        
        return  -1 if self.isEmpty() else self.deque[self.front] 
        

    def getRear(self) -> int:
        
        return  -1 if self.isEmpty() else self.deque[self.rear - 1] 
        

    def isEmpty(self) -> bool:
        
        return self.rear == self.front
        

    def isFull(self) -> bool:
        
        return abs(self.rear - self.front +1 ) % self.capacity == 0
    


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
