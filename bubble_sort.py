def bubble_sort(numbers_list):
    list_length = len(numbers_list)
    for i in range(list_length - 1):
        for j in range(list_length - i - 1):
            if numbers_list[j] > numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]

    return numbers_list


if __name__ == "__main__":
    print(bubble_sort([10, 58, 12, 0, 55, 57, 88, 11, 5, 56, 2, 18, 22, -51, -20, 574, -154]))
