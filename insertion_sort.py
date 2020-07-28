def insertion_sort(numbers_list):
    list_length = len(numbers_list)

    for i in range(0, list_length - 1):
        j = i + 1
        temp = numbers_list[j]
        while j > 0 and temp < numbers_list[j - 1]:
            numbers_list[j] = numbers_list[j - 1]
            j -= 1
        numbers_list[j] = temp

    return numbers_list


if __name__ == "__main__":
    print(insertion_sort([10, 58, 12, 0, 55, 57, 88, 11, 5, 56, 2, 18, 22, -51, -20, 574, -154]))
