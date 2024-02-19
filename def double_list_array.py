def double_list_array(elements):
    length = len(elements*2)
    double_list = []
    for i in range(length):
        double_list.append(0)
    return double_list
def double_list_array_2(elements):
    double_list = []
    for i in range(len(elements)):
        double_list[i] = elements[i]
        double_list[i+(len(elements))] = elements[i] * 2
    return double_list