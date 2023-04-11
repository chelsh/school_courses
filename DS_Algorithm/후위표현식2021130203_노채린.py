from kiwisolver import Expression


class string_stack:
    def __init__(self):
        self.string = []

    def push(self, item):
        self.string.append(item)
    
    def pop(self):
        if len(self.string) != 0:
            item = self.string.pop(-1)  # stack.pop()
            return item
        else:
            print('stack is empty')
    
    def is_empty(self):
        if self.string == []:
            return False
        else:
            return True
    
    def top(self):
        if len(self.string) != 0:
            return self.string[-1]
        else:
            print('stack is empty')

def cal_postfix(expression):
    stack = string_stack()
    for e in expression:
        # e가 숫자라면 stack에 push
        if e.isdigit():
            stack.push(int(e))
        # e가 연산자라면 stack에서 숫자 두개를 꺼내와 연산자로 계산 후 stack에 push
        else:
            second = stack.pop()
            first = stack.pop()
            if e == '+':
                stack.push(first + second)
            elif e == '-':
                stack.push(first - second)
            elif e == '*':
                stack.push(first * second)
            elif e == '/':
                if second == 0:
                    print('ZeroDivision Error')
                else:
                    stack.push(first // second)
    return stack.pop()  # 최종 값 반환

exp = input()
result = cal_postfix(exp)
print(result)