def words_and_digit(sentence):
    lower_case_letter = 0
    upper_case_letter = 0
    for count in sentence:
        if count.islower():
            lower_case_letter += 1
        if count.isupper():
            upper_case_letter += 1
    return f"UPPER CASE {upper_case_letter} LOWERCASE {lower_case_letter}"


sentence1 = input("Enter a sentence: ")
print(words_and_digit(sentence1))
