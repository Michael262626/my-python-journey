from python_code.InvalidInputError import InvalidInputError

asterisk = {
    '0': ('####', '#  #', '#  #', '#  #', '#  #', '#  #', '####'),
    '1': ('   #', '   #', '   #', '   #', '   #', '   #', '   #'),
    '2': ('####', '   #', '   #', '####', '#   ', '   #', '####'),
    '3': ('####', '   #', '   #', '####', '   #', '   #', '####'),
    '4': ('#  #', '#  #', '#  #', '####', '   #', '   #', '   #'),
    '5': ('####', '#   ', '#   ', '####', '   #', '   #', '####'),
    '6': ('####', '#   ', '#   ', '####', '#  #', '#  #', '####'),
    '7': ('####', '   #', '   #', '   #', '   #', '   #', '   #'),
    '8': ('####', '#  #', '#  #', '####', '#  #', '#  #', '####'),
    '9': ('####', '#  #', '#  #', '####', '   #', '   #', '   #'),
    'A': ('####', '#  #', '#  #', '####', '#  #', '#  #', '#  #'),
    'b': ('#   ', '#  #', '####', '#  #', '#  #', '#  #', '####'),
    'C': ('####', '#   ', '#   ', '#   ', '#   ', '#   ', '####'),
    'd': ('   #', '   #', '   #', '####', '#  #', '#  #', '####'),
    'E': ('####', '#  #', '#  #', '####', '#  #', '#  #', '####'),
    'F': ('####', '#  #', '#  #', '####', '   #', '   #', '   #'),
    'H': ('#  #', '#  #', '#  #', '####', '#  #', '#  #', '#  #'),
    'I': ('#  ', '#   ', '#    ', '#   ', '#   ', '#   ', '#   '),
    'L': ('#   ', '#   ', '   #', '   #', '   #', '   #', '####'),
    'P': ('####', '#  #', '#  #', '####', '#   ', '#   ', '#   '),
    'U': ('#  #', '#  #', '#  #', '#  #', '#  #', '#  #', '####')
}


def zero_segment_display(binary):
    if binary == validate_input("11111101"):
        key = '0'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("00000000"):
        print(' ')


def one_segment_display(binary):
    if binary == validate_input("01100001"):
        key = '1'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("01100000"):
        print(' ')
    return ""


def two_segment_display(binary):
    if binary == validate_input("11011001"):
        key = '2'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("11011000"):
        print(' ')
    return ""


def three_segment_display(binary):
    if binary == validate_input("11110001"):
        key = '3'
        print('\n'.join(asterisk[key]))
    elif binary == '11110000':
        print(' ')
    return ""


def four_segment_display(binary):
    if binary == validate_input("01100111"):
        key = '4'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("01100110"):
        print(' ')
    return ""


def five_segment_display(binary):
    if binary == validate_input("10110111"):
        key = '5'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("10110110"):
        print(' ')
    return ""


def six_segment_display(binary):
    if binary == validate_input("10111111"):
        key = '6'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("10111110"):
        print(' ')
    return ""


def seven_segment_display(binary):
    if binary == validate_input("11100001"):
        key = '7'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("11100000"):
        print(' ')
    return ""


def eight_segment_display(binary):
    if binary == validate_input("11111111"):
        key = '8'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("11111110"):
        print(' ')
    return ""


def nine_segment_display(binary):
    if binary == validate_input("11100101"):
        key = '9'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("11100100"):
        print(' ')
    return ""


def letter_a_display(binary):
    if binary == validate_input("11101101"):
        key = 'A'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input("11101100"):
        print(' ')
    return ""


def letter_b_display(binary):
    if binary == validate_input('00111111'):
        key = 'b'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input('00111110'):
        print(' ')
    return ""


def letter_c_display(binary):
    if binary == validate_input('10011101'):
        key = 'C'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input('10011100'):
        print(' ')
    return ""


def letter_d_display(binary):
    if binary == validate_input("01111011"):
        key = 'd'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input('01111010'):
        print(' ')
    return ""


def letter_e_display(binary):
    if binary == validate_input("10011111"):
        key = 'E'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input('10011110'):
        print(' ')
    return ""


def letter_f_display(binary):
    if binary == validate_input("10001101"):
        key = 'F'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input('10001100'):
        print(' ')
    return ""


def letter_h_display(binary):
    if binary == validate_input('01101101'):
        key = 'H'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input('01101100'):
        print(' ')
    return ""


def letter_i_display(binary):
    if binary == validate_input('00001101'):
        key = 'I'
        print('\n'.join([key]))
    elif binary == validate_input('00001100'):
        print(' ')
    return ""


def letter_l_display(binary):
    if binary == validate_input("00011011"):
        key = 'L'
        print('\n'.join([key]))
    elif binary == validate_input('00011010'):
        print(' ')
    return ""


def letter_p_display(binary):
    if binary == validate_input('11001111'):
        key = 'P'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input('11001110'):
        print(' ')
    return ""


def letter_u_display(binary):
    if binary == validate_input('01111101'):
        key = 'U'
        print('\n'.join(asterisk[key]))
    elif binary == validate_input('01111100'):
        print(' ')
    return ""


def validate_input(binary):
    if len(binary) != 8:
        raise InvalidInputError('input mismatch')
    for items in binary:
        if items not in ('0', '1'):
            raise InvalidInputError('input mismatch')
    return binary


def print_asterisk(word):
    print(zero_segment_display(word))
    print(one_segment_display(word))
    #
    # print(two_segment_display(word))
    # print(three_segment_display(word))
    # print(four_segment_display(word))
    # print(five_segment_display(word))
    # print(six_segment_display(word))
    # print(seven_segment_display(word))
    # print(eight_segment_display(word))
    # print(nine_segment_display(word))
    # print(letter_a_display(word))
    # print(letter_u_display(word))
    # print(letter_p_display(word))
    # print(letter_h_display(word))
    # print(letter_i_display(word))
    # print(letter_b_display(word))
    # print(letter_c_display(word))
    # print(letter_l_display(word))
    # print(letter_e_display(word))
    # print(letter_d_display(word))
    return ""
