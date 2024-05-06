class queue:
    def __init__(self):
        self.queue = []        

    def enqueue(self, obj):
        self.queue.append(obj)
    
    def dequeue(self):
        queue_front = self.queue[0]
        del self.queue
        return queue_front
    
    def __str__(self):
        print(self.queue)
        return str(self.queue)

q1= queue()
q1.enqueue(1)
