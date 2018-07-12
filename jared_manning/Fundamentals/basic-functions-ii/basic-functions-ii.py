def countdown(num):
    return [x for x in range(num, -1, -1)]


def print_ret(arr):
    head, *tail = arr
    print(head)
    return(tail[0])


def first_plus_length(arr):
    return arr[0] + len(arr)


def greater_than_second(arr):
    return [x for x in arr if x > len(arr)] if len(arr) > 1 else False


def length_and_value(size, value):
    return list(map((lambda _: value), [0] * size))


def main():
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 44, 21, 15, 7, 63, 14, 15, 16, 17]

    print(countdown(7),
          print_ret(test_arr),
          first_plus_length(test_arr),
          greater_than_second(test_arr),
          length_and_value(5, 24),
          sep=', ')


if __name__ == '__main__':
    main()
