# -*- coding: utf-8 -*-


from functools import reduce


def print_zero_to_one_hundred_fifty():
    for num in range(0, 151):
        print(num)


def multiples_of_five():
    for num in range(5, 1000001, 5):
        print(num)


def not_fizz_buzz():
    for num in range(1, 101):
        div_ten = num % 10 == 0
        div_five = num % 5 == 0
        if div_five and div_ten:
            print("CodingDojo")
        elif div_ten:
            print("Dojo")
        elif div_five:
            print("Coding")
        else:
            print(str(num))


def huge_sucker():
    print(reduce((lambda acc, val: acc + val),
                 [x for x in range(0, 500001) if not x % 2 == 0]))


def countdown_by_fours():
    for num in range(2018, 1, -4):
        print(num)


def flexible_countdown(low, high, mult):
    for num in [num for num in range(low, high + 1) if num % mult == 0]:
        print(num)


def main():
    print_zero_to_one_hundred_fifty()
    multiples_of_five()
    not_fizz_buzz()
    huge_sucker()
    countdown_by_fours()
# just rmemebered that this assignment is all about for loops. ¯\_(ツ)_/¯
    flexible_countdown(2, 9, 3)  # shouldn't this be countup?


list1 = [3, 5, 1, 2]
for i in list1:
    print(i)
# Prediction: This will print each value in the list on a new line.
# Actual: This prints each value in the list on a new line.


# list2 = [3, 5, 1, 2]
# for i in range(list2):
#     print(i)
# Prediction: This will error because list2 is not a number, it's a list.
# Actual: This errors becase list2 is not a number, it's a list.


list3 = [3, 5, 1, 2]
for i in range(len(list3)):
    print(i)
# Prediction: This will print 0, 1, 2, 3
# Actual: This prints 0, 1, 2, 3


if __name__ == '__main__':
    main()
