import ast

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())   

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]
        
    def empty(self) -> bool:
        return len(self.s1) == 0


if __name__ == "__main__":
    operations = ast.literal_eval(input().strip())
    arguments = ast.literal_eval(input().strip())

    output = []
    obj = None

    for op, arg in zip(operations, arguments):
        
        if op == "MyQueue":
            obj = MyQueue()
            output.append(None)
        
        elif op == "push":
            obj.push(arg[0])
            output.append(None)
        
        elif op == "pop":
            output.append(obj.pop())
        
        elif op == "peek":
            output.append(obj.peek())
        
        elif op == "empty":
            output.append(obj.empty())

    print(output)