class Stack:
    def __init__(self,size):
        self.data = []
        self.size = size
    def isEmpty(self):
        return len(self.data) == 0
    def isFull(self):
        return len(self.data) == self.size
    def push(self, value):
        if not self.isFull():
            self.data.append(value)
    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
    def Peek(self):
        if not self.isEmpty():
            return self.data[-1]

def cal_postfix(expression: str):
    s = Stack(len(expression))
    for e in expression:
        if e.isdigit():
            s.push(int(e))
        else:
            second = int(s.pop())
            first = int(s.pop())
            if e == '+':
                s.push(first + second)
            elif e == '-':
                s.push(first - second)
            elif e == '*':
                s.push(first * second)
            elif e == '/':
                if second == 0:
                    print('ZeroDivisionError')
                else:
                    s.push(first / second)
    return s.pop()
    
if __name__ == "__main__":
    exp = input()
    result = cal_postfix(exp)
    print(result)