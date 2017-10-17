def count_inversions(data, x):
    inversions = []
    for user_ind in range(len(data)):
        if user_ind == x:
            continue
        else:
            inversions.append([user_ind, count_inv(data[x], data[user_ind])])
    return inversions


def count_inv(arr1, arr2):
    arr = [arr2.find(mov) for mov in arr1]
    invs = 0

    return invs


if __name__ == "__main__":
    arr = [[3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
           [2, 10, 8, 9, 5, 4, 3, 7, 6, 1],
           [2, 4, 9, 6, 10, 7, 5, 1, 3, 8],
           [3, 9, 10, 6, 7, 4, 1, 2, 5, 8],
           [7, 3, 8, 6, 5, 4, 10, 1, 2, 9]]
    print(count_inversions(arr, 0) == [[2, 14], [3, 16], [4, 19], [1, 22]])
    print(count_inversions(arr, 1) == [[3, 16], [0, 22], [2, 24], [4, 31]])

