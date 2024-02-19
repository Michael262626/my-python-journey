import random

list1 = []
for count in range(10):
    numbers = random.randint(1, 50)
    list1.append(numbers)

print(list1)


def get_length_of_a_list(number):
    scores = 0
    for score in number:
        scores += 1
    return scores


def sum_even_positions(number):
    even = 0
    for num in range(len(number)):
        if num % 2 == 0:
            even += number[num]
    return even


def sum_odd_positions(number):
    odd = 1
    for num in number:
        if num % 2 != 0:
            odd += num
    return odd


def multiple_of_three(number):
    multiply = 1
    for num in number[::3]:
        multiply *= num
    print(multiply)
    return multiply


def average_numbers(number):
    return_value = sum(number) / len(number)
    temp = (f"{return_value:.2f}")
    return_value = float(temp)
    return return_value


def largest_elements(number):
    num1 = number[0]
    for num in range(len(number)):
        if number[num] > num1:
            num1 = number[num]
    return num1


def smallest_elements(number):
    num2 = number[0]
    for num in range(len(number)):
        if number[num] < num2:
            num2 = number[num]
    return num2


def that_function_list_of_strings(strings):
    results = []
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            results.append(string)
    return results


