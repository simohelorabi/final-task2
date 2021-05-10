def shift_right(string):
    return string[len(string) - 1] + string[:-1]


def shift_left(string):
    return string[1:] + string[0]


def shift_string(string: str, direction: str, shift_amount: int):
    for _ in range(shift_amount):
        if direction == "right ":
            string = shift_right(string)
        else:
            string = shift_left(string)

    return string


print(shift_string('number', 'left', 3))
