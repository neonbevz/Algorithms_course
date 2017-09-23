def sort(lst):
    lst.append(0)
    for i in range(1, len(lst) - 1):
        ind = i
        while lst[i] < lst[ind - 1]:
            ind -= 1
        if ind == -1:
            lst = [lst[i]] + lst[:i] + lst[i+1:]
        else:
            lst = lst[:ind] + [lst[i]] + lst[ind: i] + lst[i+1:]
    return lst[:-1]

if __name__ == "__main__":
    print(sort([30, 19, 9, 15, 55, 24, 3, 78, 46, 41]))
