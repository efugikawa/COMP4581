# Stack and Queue Abstract Data Types
# Elizabeth Fugikawa, summer 2022

from collections import deque


class MyStack:
    def __init__(self, stackType):
        self.state = []
        self.elemType = stackType

    def __str__(self):
        return f"{self.state}"

    def push(self, elem):
        assert type(elem) == self.elemType
        self.state.append(elem)

    def pop(self):
        if not self.is_empty():
            return self.state.pop()
        else:
            raise ValueError("Stack is empty")

    def top(self):
        if self.is_empty():
            raise ValueError("Empty stack")
        else:
            return self.state[-1]

    def is_empty(self):
        return len(self.state) == 0


class MyQueue:
    def __init__(self, queueType):
        self.state = deque()
        self.elemType = queueType

    def __str__(self):
        return f"{self.state}"

    def enqueue(self, elem):
        assert type(elem) == self.elemType
        self.state.append(elem)

    def dequeue(self):
        if not self.is_empty():
            return self.state.popleft()
        else:
            raise ValueError("Queue is empty")

    def front(self):
        if self.is_empty():
            raise ValueError("Empty queue")
        else:
            return self.state[0]

    def is_empty(self):
        return len(self.state) == 0


def main():
    print("test MyStack")
    s = MyStack(int)
    print(s.is_empty())
    s.push(5)
    s.push(8)
    print(s.pop())
    s.push(3)
    print(s.is_empty())
    print(s.top())
    print(s.pop())
    print(s.pop())
    # print(s.pop()) # raises error b/c stack is empty

    print("test MyQueue")
    q = MyQueue(int)
    print(q.is_empty())
    q.enqueue(5)
    q.enqueue(8)
    print(q.dequeue())
    q.enqueue(3)
    print(q.is_empty())
    print(q.front())
    print(q.dequeue())
    print(q.dequeue())
    # print(q.dequeue()) # causes an error b/c queue is empty


if __name__ == '__main__':
    main()
