class Queue(object):
    def __init__(self) -> None:
        """post : creates an empty FIFO queue """
        self.items: list[object] = []

    def enqueue(self, x: object) -> None:
        """post : adds x at back of queue"""
        self.items.insert(0, x)

    def dequeue(self) -> object:
        """pre: self.size() > 0 
        post: removes and returns the front item"""
        if self.items:
            return self.items.pop()
        return None
    
    def front(self) -> object:
        """pre: self.size() > 0 
        postcondition: returns first item in queue"""
        return self.items[len(self.items)-1]

    def size(self) -> int:
        """postcondition: return number of items in queue"""
        return len(self.items)