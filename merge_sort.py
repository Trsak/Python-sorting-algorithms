def merge_sort(numbers_list):
    list_length = len(numbers_list)

    if list_length <= 1:
        return numbers_list

    left = []
    right = []
    for i in range(list_length):
        if i < list_length / 2:
            left.append(numbers_list[i])
        else:
            right.append(numbers_list[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    while len(left) > 0:
        result.append(left[0])
        left.pop(0)

    while len(right) > 0:
        result.append(right[0])
        right.pop(0)

    return result


if __name__ == "__main__":
    print(merge_sort([10, 58, 12, 0, 55, 57, 88, 11, 5, 56, 2, 18, 22, -51, -20, 574, -154]))
