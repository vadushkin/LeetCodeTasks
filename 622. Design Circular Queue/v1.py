class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.maxSize = k
        self.head = 0
        self.tail = -1

    def enQueue(self, val: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.maxSize
        self.data[self.tail] = val
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head, self.tail = 0, -1
        else:
            self.head = (self.head + 1) % self.maxSize
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.tail == -1

    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.maxSize == self.head


def main():
    myCircularQueue = MyCircularQueue(3)
    print(myCircularQueue.enQueue(1))
    print(myCircularQueue.enQueue(2))
    print(myCircularQueue.enQueue(3))
    print(myCircularQueue.enQueue(4))
    print(myCircularQueue.Rear())
    print(myCircularQueue.isFull())
    print(myCircularQueue.deQueue())
    print(myCircularQueue.enQueue(4))
    print(myCircularQueue.Rear())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 74 ms, faster than 90.18% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.5 MB, less than 85.14% of Python3 online submissions for Design Circular Queue. 

2. Runtime: 69 ms, faster than 96.06% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.5 MB, less than 85.14% of Python3 online submissions for Design Circular Queue.
"""
