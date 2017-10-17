def count_inversions(data, user_1):
    inversions = []
    for user_2 in range(len(data)):
        if user_2 == user_1:
            continue
        else:
            array = [data[user_2][data[user_1].index(mov)] for mov in range(1, len(data[user_1]) + 1)]
            inversions.append([user_2, merge_count(array, 0, len(array))])
    return sorted(inversions, key=lambda x: x[1])


def merge_count(array, start, end):
    invs = 0
    if end - start >= 2:
        mid_ind = (end - start) // 2 + start
        invs += merge_count(array, start, mid_ind)
        invs += merge_count(array, mid_ind, end)
        invs += merge(array, start, end, mid_ind)
    return invs


def merge(array, start, end, mid):
    invs = 0
    new_arr = []
    temp_left = array[start:mid]
    temp_right = array[mid:end]
    for i in range(end - start):
        if len(temp_right) == 0:
            new_arr.append(temp_left.pop(0))
        elif len(temp_left) == 0:
            new_arr.append(temp_right.pop(0))
            invs += mid - ((mid-start) - len(temp_left)) - start
        elif temp_left[0] >= temp_right[0]:
            new_arr.append(temp_right.pop(0))
            invs += mid - ((mid-start) - len(temp_left)) - start
        else:
            new_arr.append(temp_left.pop(0))
    array[start:end] = new_arr
    return invs
