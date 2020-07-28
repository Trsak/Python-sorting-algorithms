def quick_sort(numbers_list):
    list_length = len(numbers_list)

    if list_length <= 1:
        return numbers_list

    pivot = numbers_list[0]
    bigger_numbers = []
    smaller_numbers = []
    for i in range(1, list_length):
        if numbers_list[i] > pivot:
            bigger_numbers.append(numbers_list[i])
        else:
            smaller_numbers.append(numbers_list[i])

    return quick_sort(smaller_numbers) + [pivot] + quick_sort(bigger_numbers)


if __name__ == "__main__":
    print(quick_sort([10, 58, 12, 0, 55, 57, 88, 11, 5, 56, 2, 18, 22, -51, -20, 574, -154]))
