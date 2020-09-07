def shell_sort(numbers_list):
    list_length = len(numbers_list)
    list_gap = int(list_length / 2)

    while list_gap > 0:
        for i in range(list_length - list_gap):
            j = i + list_gap
            temp = numbers_list[j]
            while j >= list_gap and temp < numbers_list[j - list_gap]:
                numbers_list[j] = numbers_list[j - list_gap]
                j -= list_gap
            numbers_list[j] = temp

        if list_gap == 2:
            list_gap = 1
        else:
            list_gap = int(list_gap / 2.2)

    return numbers_list


if __name__ == "__main__":
    print(shell_sort([10, 58, 12, 0, 55, 57, 88, 11, 5, 56, 2, 18, 22, -51, -20, 574, -154]))
