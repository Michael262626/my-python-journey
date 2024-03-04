def letters_digits(sentence):
    number_of_letters = 0
    number_of_numbers = 0
    for count in sentence:
        if count.isdigit():
            number_of_numbers += 1
        if count.isalpha():
            number_of_letters += 1
    return f"LETTERS {number_of_letters} DIGITS {number_of_numbers}"

#
# sentence1 = input("Enter a sentence: ")
# print(letters_digits(sentence1))
