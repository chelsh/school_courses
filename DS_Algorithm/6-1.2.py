#Queue 응용 - 55p => 백준 자료구조 카드2 (2164)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, item):
        self.nd = Node(item)
        if self.size == 0:
            self.front = self.nd
            self.rear = self.nd
        else:
            self.rear.next = self.nd
            self.rear = self.nd
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Underflow Error")
        else:
            deletedItem = self.front
            self.front = self.front.next
            self.size -= 1
            if self.size == 0:
                self.rear = None
            return deletedItem

cards = Queue()

N = int(input())

for i in range(1, N + 1):
    cards.enqueue(i)

for _ in range(N - 1):
    cards.dequeue()
    cards.enqueue(cards.dequeue().data)

print(cards.dequeue().data)