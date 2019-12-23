# this function return True if it an acceptable number and False otherwise
# An Acceptable string is 4 characters long, an actual number, not all
# the number are the same, and is positive


def input_validation(number):
    number = str(number)
    if len(number) != 4:
        return False
    elif not number.isdigit():
        return False
    elif number.count(number[0]) == 4:
        return False
    else:
        return True


# this function take the string digit_list and breaks it
# into a list of 4 if there is not that many characters
# in the string then it will add 0's
def break_into_list(digit_list):
    digit_list = list(str(digit_list))
    length = len(digit_list)
    zeroes_needed = 4 - length
    zeroes_list = ['0']*zeroes_needed
    digit_list.extend(zeroes_list)
    return digit_list


# assign place values to list digit_list to be able
# to convert to an int
def assign_place_values(digit_list):
    full_number = 0
    for i in range(0, len(digit_list)):
        each_digit = int(digit_list[i])
        full_number += each_digit * 10 ** (len(digit_list) - i - 1)

    return full_number


# A Kaprekar Operation is the difference of all the digits in a
# a number being sorted greatest to least and sorted least to greatest
def kaprekar_operation(digits):
    # make it work for the just in case 999< to 0999)
    digits = break_into_list(digits)
    sorted_list = sorted(digits)
    backwards_sort = list(reversed(sorted_list))

    sorted_list = assign_place_values(sorted_list)
    backwards_sort = assign_place_values(backwards_sort)

    return (backwards_sort, sorted_list, backwards_sort-sorted_list)


# main program starts here
def main():
    message = "Give a four digit, positive number "
    message += "in which not all the digits are alike: "
    number = input(message)

    while True:
        try:
            if input_validation(number):
                number = int(number)
                break
            else:
                message = "Try again: make sure the number is four digits, "
                message += "positive, and not all the numbers are the same: "
                number = input(message)
        except ValueError:
            number = input("Try again: give an integer: ")

    all_numbers = kaprekar_operation(number)
    print(all_numbers[0], "-", all_numbers[1], "=", all_numbers[2])

    while all_numbers[2] != 6174:
        all_numbers = kaprekar_operation(all_numbers[2])
        print(all_numbers[0], "-", all_numbers[1], "=", all_numbers[2])
    print("finished! You have reached 6174, the four-digit Kaprekar Kernel")


# calls main
if __name__ == '__main__':
    main()
