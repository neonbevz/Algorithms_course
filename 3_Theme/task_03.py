class Heap:
    def get_root(self):
        if self.size > 0:
            return self.array[1]
        else:
            return self.array[0]

    def get_array(self):
        return self.array[1:]

    @staticmethod
    def parent(ind):
        return ind//2

    @staticmethod
    def child_left(ind):
        return ind*2

    @staticmethod
    def child_right(ind):
        return ind*2 + 1

    def is_child_left(self, ind):
        return self.child_left(ind) < len(self.array)

    def is_child_right(self, ind):
        return self.child_right(ind) < len(self.array)


class MaxHeap(Heap):
    def __init__(self):
        self.array = [float("inf")]
        self.size = 0

    def insert(self, el):
        self.array.append(el)
        self.size += 1
        ind = self.size
        while el > self.array[self.parent(ind)]:
            self.array[ind], self.array[self.parent(ind)] = self.array[self.parent(ind)], self.array[ind]
            ind = self.parent(ind)

    def extract_max(self):
        root = self.get_root()
        self.array[1] = self.array.pop()
        self.size -= 1
        self.max_heapify(1)
        return root

    def max_heapify(self, ind):
        largest_ind = ind
        if self.child_left(ind) <= self.size and self.array[self.child_left(ind)] > self.array[largest_ind]:
            largest_ind = self.child_left(ind)
        if self.child_right(ind) <= self.size and self.array[self.child_right(ind)] > self.array[largest_ind]:
            largest_ind = self.child_right(ind)
        if largest_ind != ind:
            self.array[ind], self.array[largest_ind] = self.array[largest_ind], self.array[ind]
            self.max_heapify(largest_ind)


class MinHeap(Heap):
    def __init__(self):
        self.array = [-float("inf")]
        self.size = 0

    def insert(self, el):
        self.array.append(el)
        self.size += 1
        ind = self.size
        while el < self.array[self.parent(ind)]:
            self.array[ind], self.array[self.parent(ind)] = self.array[self.parent(ind)], self.array[ind]
            ind = self.parent(ind)

    def extract_min(self):
        root = self.get_root()
        self.array[1] = self.array.pop()
        self.size -= 1
        self.min_heapify(1)
        return root

    def min_heapify(self, ind):
        smallest_ind = ind
        if self.child_left(ind) <= self.size and self.array[self.child_left(ind)] < self.array[smallest_ind]:
            smallest_ind = self.child_left(ind)
        if self.child_right(ind) <= self.size and self.array[self.child_right(ind)] < self.array[smallest_ind]:
            smallest_ind = self.child_right(ind)
        if smallest_ind != ind:
            self.array[ind], self.array[smallest_ind] = self.array[smallest_ind], self.array[ind]
            self.min_heapify(smallest_ind)


class Median:
    def __init__(self):
        self.low_heap = MaxHeap()
        self.high_heap = MinHeap()

    def add_element(self, value):
        if value > self.high_heap.get_root():
            self.high_heap.insert(value)
        elif value < self.low_heap.get_root():
            self.low_heap.insert(value)
        else:
            if self.low_heap.size >= self.high_heap.size:
                self.high_heap.insert(value)
            else:
                self.low_heap.insert(value)
        dif = self.high_heap.size - self.low_heap.size
        if dif > 1:
            for _ in range(dif - 1):
                self.low_heap.insert(self.high_heap.extract_min())
        elif dif < -1:
            for _ in range(-dif - 1):
                self.high_heap.insert(self.low_heap.extract_max())

    def get_median(self):
        if self.low_heap.size == self.high_heap.size:
            return self.low_heap.get_root(), self.high_heap.get_root()
        elif self.low_heap.size > self.high_heap.size:
            return self.low_heap.get_root()
        else:
            return self.high_heap.get_root()

    def get_maxheap_elements(self):
        return self.low_heap.get_array()

    def get_minheap_elements(self):
        return self.high_heap.get_array()


if __name__ == "__main__":
    pass
