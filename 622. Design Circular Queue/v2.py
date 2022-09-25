class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.q = [-1] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear % self.k] = value
        self.rear += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.front % self.k] = -1
        self.front += 1
        return True

    def Front(self) -> int:
        return self.q[self.front % self.k]

    def Rear(self) -> int:
        return self.q[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.rear - self.front == self.k


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
1. Runtime: 69 ms, faster than 96.06% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.4 MB, less than 98.10% of Python3 online submissions for Design Circular Queue. 

2. Runtime: 70 ms, faster than 95.11% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.4 MB, less than 98.10% of Python3 online submissions for Design Circular Queue.
"""
