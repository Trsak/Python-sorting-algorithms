def selection_sort(numbers_list):
    list_length = len(numbers_list)
    for i in range(list_length - 1):
        max_index = i
        for j in range(i + 1, list_length):
            if numbers_list[j] < numbers_list[max_index]:
                max_index = j
        numbers_list[i], numbers_list[max_index] = numbers_list[max_index], numbers_list[i]

    return numbers_list


if __name__ == "__main__":
    print(selection_sort([10, 58, 12, 0, 55, 57, 88, 11, 5, 56, 2, 18, 22, -51, -20, 574, -154]))
