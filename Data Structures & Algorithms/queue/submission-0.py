class Deque:
    
    def __init__(self):
        self.arr = []
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        self.arr.append(value)
        self.size += 1

    def appendleft(self, value: int) -> None:
        self.arr = [value] + self.arr
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        item = self.arr[-1]
        self.arr = self.arr[:-1]
        return item

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        item = self.arr[0]
        self.arr = self.arr[1:]
        return item
