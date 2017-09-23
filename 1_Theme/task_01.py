def sort(lst):
    # Append smaller number to prevent from falling into negative indices:
    lst.append(min(lst) - 1)
    # Iterate elements:
    for i in range(1, len(lst) - 1):
        ind = i
        # Search for correct position:
        while lst[i] < lst[ind - 1]:
            ind -= 1
        if ind == -1:
            # Insert into first position
            lst = [lst[i]] + lst[:i] + lst[i+1:]
        else:
            # ... any other position
            lst = lst[:ind] + [lst[i]] + lst[ind: i] + lst[i+1:]
    return lst[:-1]


if __name__ == "__main__":
    print(sort([30, 19, 9, 15, 55, 24, 3, 78, 46, 41]))
