class Jar:
    def __init__(self, capacity=12):
        if type(capacity) is not int:
            raise ValueError("Capacity is not an integer.")
        elif capacity < 0:
            raise ValueError("Capacity is negative!")
        else:
            self._capacity = capacity

        self._size = 0


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if type(n) is not int:
            raise ValueError("n is NOT an integer")
        elif n < 0:
            raise ValueError("n is too big or too small!")
        elif self.size + n > self.capacity:    ###the getters (@property) don't need "()", they act like variables
            raise ValueError ("The Cookie Jar is full!")
        else:
            self._size += n


    def withdraw(self, n):
        if type(n) is not int:
            raise ValueError("n is NOT an integer")
        elif n < 0:
            raise ValueError("n is too small!")
        elif n > self.size:   
            raise ValueError ("The Cookie Jar is full!")
        else:
            self._size -= n

    @property #Side Note: Write about how this should only return what it sees, and NOT assign anything.
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
