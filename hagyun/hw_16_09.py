class Limited_queue:
    def __init__(self,max:int):
        self.limited_queue=[None]*max
        self.max=max
        self.rear=0
        self.frontp=0
    def enqueue(self,data):
        if not self.is_full():
            self.limited_queue[self.rear]=data
            if self.rear+1<self.max:
                self.rear+=1
            else:
                self.rear=0
    def dequeue(self):
        if not self.is_empty():
            popped=self.limited_queue[self.frontp]
            if self.frontp+1<self.max:
                self.frontp+=1
            else:
                self.frontp=0
            return popped
        else:
            return -1
    def front(self):
        if not self.is_empty():
            return self.limited_queue[self.frontp]
        else:
            return -1
    def is_empty(self):
        if self.rear==self.frontp:
            return True
        else:
            return False
    def is_full(self):
        if (self.rear+1)%self.max==self.frontp:
            return True
        else:
            return False