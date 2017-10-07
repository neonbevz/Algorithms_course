def sort(lst):
    new_evens, new_odds = [], []
    for el in lst:
        target = new_evens if el % 2 == 0 else new_odds
        if len(target) == 0 or el > target[-1]:
            target.append(el)
        else:
            ind = 0
            while el > target[ind]:
                ind += 1
            target.insert(ind, el)
    return new_evens + list(reversed(new_odds))


if __name__ == "__main__":
    print(sort([30, 19, 9, 15, 55, 24, 3, 78, 46, 41]))
