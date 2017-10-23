class Tree:
    # def __init__(self, value, parent, child_left, child_right):
    #     self.ind, self.parent, self.child_left, self.child_right = value, parent, child_left, child_right
    def __init__(self, ind):
        self.ind = ind


class BinarySearchTree:
    def __init__(self, array):
        self.array = array
        inorder_inds = self.inorder(0)
        values = sorted([el for el in self.array if el != 0])
        bst_array = array[:]
        for ind in range(len(inorder_inds)):
            bst_array[inorder_inds[ind]] = values[ind]
        self.array = bst_array

    def key_ind(self, x):
        return self.array[x]

    def left_ind(self, x):
        ind = x + 1
        return ind if self.array[ind] else None

    def right_ind(self, x):
        l = self.left_ind(x)
        ind = x + self.count_children(l) + 2 if l else x + 2
        return ind if self.array[ind] else None

    def count_children(self, x):
        count = 0
        l = self.left_ind(x)
        count += self.count_children(l) + 1 if l else 1
        r = self.right_ind(x)
        count += self.count_children(r) + 1 if r else 1
        return count

    def parent_ind(self, x):
        for i in range(x):
            if self.array[i] and (self.left_ind(i) == x or self.right_ind(i) == x):
                return i
        return None

    def inorder(self, x):
        arr = []
        l = self.left_ind(x)
        if l:
            arr += self.inorder(l)
        arr.append(x)
        r = self.right_ind(x)
        if r:
            arr += self.inorder(r)
        return arr

    def root(self):
        return Tree(0)

    def parent(self, tr):
        p = self.parent_ind(tr.ind)
        return Tree(p) if p else None

    def left(self, tr):
        l = self.left_ind(tr.ind)
        return Tree(l) if l else None

    def right(self, tr):
        r = self.right_ind(tr.ind)
        return Tree(r) if r else None

    def key(self, tr):
        return self.array[tr.ind]

    # def find_sum(self, sum):
        # for ind in range(len(self.array)):
        #     if not self.array[ind]:
        #         continue
        #     l_sum = self.array[ind]
        #     while
        #     l = self.left_ind(ind)
        #     r = self.right_ind(ind)




if __name__ == "__main__":
    # bst = BinarySearchTree([1, 4, 6, 10, 0, 0, 0, 7, 0, 8, 0, 0, 2, 5, 0, 0, 3, 9, 0, 0, 0])
    # bst2 = BinarySearchTree([2, 7, 2, 0, 0, 6, 5, 0, 0, 11, 0, 0, 5, 0, 9, 4, 0, 0, 0])
    bst3 = BinarySearchTree([1, 2, 7, 8, 0, 0, 10, 0, 0, 0, 3, 4, 6, 0, 0, 0, 5, 9, 0, 0, 0])

