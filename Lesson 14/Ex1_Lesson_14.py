class stack:
    def __init__(self):
        self.stack = []        

    def push(self, obj):
        stack.append(obj)
    
    def pop(self):
        obj = self.stack[-1]
        del self.stack[-1]
        return obj
    
    def __str__(self):
        print_str = ""
        