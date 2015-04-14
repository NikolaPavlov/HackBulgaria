def prepare_meal(number):
    output_string = ''
    count_of_three = 0

    while number % 3 == 0:
        count_of_three += 1
        number /= 3

    output_string += ('spam ' * count_of_three)

    if number % 5 == 0:
        output_string += 'and eggs'

    return output_string


if __name__ == "__main__":
    print(prepare_meal(3))
    print(prepare_meal(9))
    print(prepare_meal(45))