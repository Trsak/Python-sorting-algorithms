def bubble_sort(list):
    list_length = len(list)
    for i in range(list_length - 1):
        for j in range(list_length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


if __name__ == "__main__":
    print(bubble_sort([10, 58, 12, 0, 55, 57, 88, 11, 5, 56, 2, 18, 22, -51, -20, 574, -154]))
