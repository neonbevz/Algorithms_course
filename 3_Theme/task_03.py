class HeapNode:
    def __init__(self, value, index):
        self.value = value
        self.parent, self.child_left, self.child_right = index//2, 2*index, 2*index + 1


class Heap:
    def __init__(self, *args):
        self.array = []
        self.size = 0
        if args:
            for i in args:
                self.insert(i)

    def insert(self, element):
        index = 0
        node = HeapNode(element, index)


if __name__ == "__main__":
    pass
