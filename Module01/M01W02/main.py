from count_characters import count_characters
from count_text_in_file import count_text_in_file
from find_max_num_by_sliding_window import find_max_num_by_sliding_window
from levenshtein_distance import levenshtein_distance

# "Câu 1 = A"
assert find_max_num_by_sliding_window([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print("Cau 1")
print(find_max_num_by_sliding_window(num_list, k))


# "Câu 2 = A"
assert count_characters("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print("Cau 2")
print(count_characters('smiles'))


# "Câu 3 = C"
file_path = 'Module01\\M01W02\\content\\P1_data.txt'
result = count_text_in_file(file_path)
assert result['who'] == 3
print("Cau 3")
print(result['man'])


# "Cau 4 = C"
assert levenshtein_distance("hi", "hello") == 4
print("Cau 4")
print(levenshtein_distance("hola", "hello"))


# "Cau 5 = A"
def check_the_number(n):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        # adding the element
        list_of_numbers.append(i)
    # Su dung append them i vao trong list_of_number
    if n in list_of_numbers:
        results = "True"
    if n not in list_of_numbers:
        results = "False"
    return results


n = 7
assert check_the_number(n) == "False"
n = 2
results = check_the_number(n)
print("Cau 5")
print(results)


# "Cau 6 = C"
def my_function_c6(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        # Neu i < min thi them min vao result
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
max_num = 1
min_num = 0
assert my_function_c6(max=max_num, min=min_num,
                      data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max_num = 2
min_num = 1
print("Cau 6")
print(my_function_c6(max=max_num, min=min_num, data=my_list))


# "Cau 7 = A"
def my_function_c7(x, y):
    # Your code here
    # Su dung extend de noi y vao x
    # return x
    result = []

    result.extend(x)
    result.extend(y)

    return result


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert my_function_c7(list_num1, my_function_c7(
    list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print("Cau 7")
print(my_function_c7(list_num1, my_function_c7(list_num2, list_num3)))


# "Câu 8 = C"
def my_function_c8(num_list):
    return min(num_list)


my_list = [1, 22, 93, -100]
assert my_function_c8(my_list) == -100

my_list = [1, 2, 3, -1]
print("Cau 8")
print(my_function_c8(my_list))


# Câu 9 = C
def my_function_c9(num_list):
    return max(num_list)


my_list = [1001, 9, 100, 0]
assert my_function_c9(my_list) == 1001

my_list = [1, 9, 9, 0]
print("Cau 9")
print(my_function_c8(my_list))


# Cau 10 = C
def my_function_c10(i, number=1):
    return any(num == number for num in i)


my_list = [1, 3, 9, 4]
assert my_function_c10(my_list, -1) == False

my_list = [1, 2, 3, 4]
print("Cau 10")
print(my_function_c10(my_list, 2))


# Cau 11 = A
def my_function_c11(list_nums):
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)


assert my_function_c11([4, 6, 8]) == 6
print("Cau 11")
print(my_function_c11([0, 1, 2]))


# Cau 12 = A
def my_function_c12(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


assert my_function_c12([3, 9, 4, 5]) == [3, 9]
print("Cau 12")
print(my_function_c12([1, 2, 3, 5, 6]))


# Cau 13 = C
def my_function_c13(y):
    var = 1
    while (y > 1):
        var *= y
        y -= 1
    return var


assert my_function_c13(8) == 40320
print("Cau 13")
print(my_function_c13(4))


# Cau 14 = B:
def my_function_c14(x):
    result = []
    for i in range(len(x)):
        result.append(x[i])
    result.reverse()
    s = ''.join(result)
    return s


assert my_function_c14('I can do it') == 'ti od nac I'
print("Cau 14")
print(my_function_c14('apricot'))


# Cau 15 = C
def function_helper_c15(x):
    if x > 0:
        return 'T'
    else:
        return 'N'


def my_function_c15(data):
    res = [function_helper_c15(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function_c15(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print("Cau 15")
print(my_function_c15(data))


# Cau 16 = A
def function_helper_c16(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def my_function_c16(data):
    res = []
    for i in data:
        if function_helper_c16(i, res):
            res.append(i)

    return res


lst = [10, 10, 9, 7, 7]
assert my_function_c16(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print("Cau 16")
print(my_function_c16(lst))
