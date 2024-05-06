class Rectangle:
    def __init__(self, lenght, width):
        self._length = lenght
        self._widht = width

    
    def area(self):
        return self._length
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, new_len):
        self._lenght = new_len

    @property
    def width 