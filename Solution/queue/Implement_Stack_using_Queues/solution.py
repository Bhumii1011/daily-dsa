from collections import deque
import ast

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self) -> int:
        return self.q1.popleft()
        
    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return len(self.q1) == 0


if __name__ == "__main__":
    operations = ast.literal_eval(input().strip())
    arguments = ast.literal_eval(input().strip())

    output = []
    obj = None

    for op, arg in zip(operations, arguments):
        
        if op == "MyStack":
            obj = MyStack()
            output.append(None)
        
        elif op == "push":
            obj.push(arg[0])
            output.append(None)
        
        elif op == "pop":
            output.append(obj.pop())
        
        elif op == "top":
            output.append(obj.top())
        
        elif op == "empty":
            output.append(obj.empty())

    print(output)