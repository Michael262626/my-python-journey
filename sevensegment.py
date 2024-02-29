from python_code.InvalidInputError import InvalidInputError


def first_method(word):
    # if validate_method(word):
    if (word[0]) == '1':
        return '# # # #'
    if (word[0]) == '0':
        return "       "


def second_method(word):
    # if validate_method(word):
    if (word[6]) == '1':
        return '# # # #'
    if (word[6]) == '0':
        return "       "


def third_method(word):
    if validate_method(word):
        if (word[3]) == '1':
            return '# # # #'
    if (word[3]) == '0':
        return "       "


def fourth_method(word):
    # if validate_method(word):
    if (word[1] == '1' and word[5]) == '1':
        return '#     #'
    if (word[1] == '0' and word[5]) == '0':
        return "       "

    if (word[1] == '0' and word[5]) == '1':
        return '      #'
    if (word[1] == '1' and word[5]) == '0':
        return '#      '
    return "       "


def fifth_method(word):
    if validate_method(word):
        if (word[2] == '1' and word[4]) == '1':
            return '#     #'
        if (word[2] == '0' and word[4]) == '0':
            return "       "
        if (word[2] == '1' and word[4]) == '0':
            return '#      '
        if (word[2] == '0' and word[4]) == '1':
            return '      #'
        return "       "


def validate_method(word):
    if len(word) != 8:
        raise InvalidInputError('Input mismatch')
    for items in word:
        if items not in ('0', '1'):
            raise InvalidInputError('Input mismatch')
    return True


def is_on(number):
    if number[7] == '1':
        return True
    return False


def shape(number):
    if is_on(number):
        return (f"{first_method(number)}\n{fifth_method(number)}"
                f"\n{third_method(number)}\n{fourth_method(number)}" +
                f"\n{second_method(number)}")
    return "       "


def segment(number):
    print(shape(number))


number1 = (input('Enter 0 or 1: '))
print(segment(number1))
