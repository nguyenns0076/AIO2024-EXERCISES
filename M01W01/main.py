import math
import random


# Tự luận
# Exercise_01: function thực hiện đánh giá classification model bằng F1-Score.

def precision_calculate(tp, fp):
    if not isinstance(tp, int):
        print("TP " + str(tp) + " must me int!\n")
        return
    if not isinstance(fp, int):
        print("FP " + str(fp) + " must me int!\n")
        return
    if tp <= 0 or fp <= 0:
        print("TP and FP and FN must greater then zero\n")
        return
    return tp/(tp+fp)


def recall_calculate(tp, fn):
    if not isinstance(tp, int):
        print("TP " + str(tp) + " must me int!\n")
        return
    if not isinstance(fn, int):
        print("FN " + str(fn) + " must me int!\n")
        return
    if tp <= 0 or fn <= 0:
        print("TP and FP and FN must greater then zero\n")
        return
    return tp/(tp+fn)


def f1score_calculate(precision, recall):
    return 2 * ((precision * recall) / (precision + recall))


def exercise_01():
    _tp = input("Input tp: ")
    tp = int(_tp)
    _fp = input("Input fp: ")
    fp = int(_fp)
    _fn = input("Input fn: ")
    fn = int(_fn)

    precision = precision_calculate(tp, fp)
    if not isinstance(precision, float):
        return
    print("Precision is " + str(precision) + "\n")

    recall = recall_calculate(tp, fn)
    if not isinstance(recall, float):
        return
    print("Recall is " + str(recall) + "\n")

    f1score = f1score_calculate(precision, recall)
    print("F1-score is " + str(f1score) + "\n")
    return f1score


# exercise_01()

# ----------------------------------------------------------------------------

# Exercise_02: function mô phỏng theo 3 activation function.

def is_number(x):
    try:
        float(x)
    except ValueError:
        print("x must be a number")
        return False
    return True


def sigmoid_calculate(x):
    if is_number(x) is False:
        return

    _x = float(x)
    s = 1 / (1 + math.exp(-_x))
    print(f"sigmoid: f({_x}) = " + str(s))
    return s


def relu_calculate(x):
    if is_number(x) is False:
        return

    _x = float(x)
    if _x <= 0:
        print(f"relu: f({_x}) = {0}")
        return 0
    else:
        print(f"relu: f({_x}) = {_x}")
        return _x


def elu_calculate(x):
    if is_number(x) is False:
        return

    _x = float(x)
    if _x <= 0:
        _elu = 0.01 * (pow(math.e, _x) - 1)
        print(f"elu: f({_x}) = " + str(_elu))
        return _elu
    else:
        print(f"elu: f({_x}) = {_x}")
        return _x


def exercise_02():
    x = input("Input x = ")
    activation_function = input(
        "Input activation Function ( sigmoid | relu | elu ): ")

    if "sigmoid" in activation_function:
        return sigmoid_calculate(x)
    elif "relu" in activation_function:
        return relu_calculate(x)
    elif "elu" in activation_function:
        return elu_calculate(x)
    else:
        return print(activation_function + " is not supportted")


# exercise_02()


# ----------------------------------------------------------------------------

# Exercise_03: function lựa chọn regression loss function để tính loss

def regression_loss_calculate(num_samples, loss_name):
    for n in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if "MAE" in loss_name:
            loss = abs(predict - target)
        elif "MSE" in loss_name:
            loss = pow(predict - target, 2)
        elif "RMSE" in loss_name:
            loss = math.sqrt(pow(predict - target, 2))
        else:
            return print(loss_name + " is not supportted")

        print(f"loss name: {loss_name}, sample: {n}, \
pred: {predict}, target: {target}, loss: {loss}")

    return


def exercise_03():
    num_samples = input("Input number of samples \
( integer number ) which are generated : ")

    if num_samples.isnumeric() is False:
        return print("number of samples must be an integer number")

    loss_name = input("Input loss name ( MAE | MSE | RMSE) : ")

    regression_loss_calculate(int(num_samples), loss_name)


# exercise_03()


# ----------------------------------------------------------------------------

# Exercise_04: functions để ước lượng các hàm số sau

def factorial_calculate(n):
    f = 1
    if (n == 0 or n == 1):
        return f
    else:
        for i in range(2, n + 1):
            f = f * i
        return f


def approx_sin():
    x = input("Input radian: ")
    _x = float(x)
    n = input("Input num loop ( num > 0 ): ")
    _n = int(n)
    sin = 0

    for i in range(_n):
        temp = (pow(-1, i)) * (pow(_x, 2 * i + 1)) / factorial_calculate(2 * i + 1)  # noqa: E501
        sin += temp

    print("Sin: " + str(sin))
    return sin


def approx_cos():
    x = input("Input radian: ")
    _x = float(x)
    n = input("Input num loop ( num > 0 ): ")
    _n = int(n)
    cos = 0

    for i in range(_n):
        temp = ((-1) ** i) * (pow(_x, 2 * i)) / factorial_calculate(2 * i)
        cos += temp

    print("Cos: " + str(cos))
    return cos


def approx_sinh():
    x = input("Input radian: ")
    _x = float(x)
    n = input("Input num loop ( num > 0 ): ")
    _n = int(n)
    sinh = 0

    for i in range(_n):
        term = (_x ** (2 * i + 1)) / factorial_calculate(2 * i + 1)
        sinh += term
    
    print("Sinh: " + str(sinh))
    return sinh


def approx_cosh():
    x = input("Input radian: ")
    _x = float(x)
    n = input("Input num loop ( num > 0 ): ")
    _n = int(n)
    cosh = 0

    for i in range(_n):
        term = (_x ** (2 * i)) / factorial_calculate(2 * i)
        cosh += term
    
    print("Cosh: " + str(cosh))
    return cosh


# approx_sin()
# approx_cos()
# approx_sinh()
# approx_cosh()


# ----------------------------------------------------------------------------

# Exercise_05:  function thực hiện Mean Difference of nth Root Error

def md_nre_single_sample_calculate():
    y = input("Input y: ")
    _y = float(y)
    y_hat = input("Input y_hat: ")
    _y_hat = float(y_hat)
    n = input("Input square root n: ")
    _n = int(n)
    p = input("Input level p: ")
    _p = int(p)

    md = pow((_y ** (1 / _n)) - (_y_hat ** (1 / _n)), _p)
    print(f"md_nre_single_sample (y = {y}, y_hat = {y_hat}, n = {n}, p = {p})")
    return print(md)


# md_nre_single_sample_calculate()


# ----------------------------------------------------------------------------

# Trắc nghiệm
# Câu hỏi 1
# assert round(exercise_01(), 2) == 0.33
# print(round(exercise_01()), 2)

# Câu hỏi 2
# assert is_number(3) == 1.0
# assert is_number('-2a') == 0.0
# print(is_number(1))
# print(is_number('n'))

# Câu 3
# def c3():
#     x = -2.0
#     if x <= 0:
#         y = 0.0
#     else:
#         y = x
#     print(y)


# c3()

# Câu 4
# assert round(sigmoid_calculate(3), 2) == 0.95
# print(round(sigmoid_calculate(2), 2))

# Câu 5
# assert round(elu_calculate(1)) == 1
# print(round(elu_calculate(-1), 2))

# Câu 6
# assert round(exercise_02(), 2) == 1.0
# print(round(exercise_02(), 2))

# Câu 7
# def calc_ae(y, y_hat):
#     return abs(y - y_hat)


# assert calc_ae(1, 6) == 5
# print(calc_ae(2, 9))

# Câu 8
# def calc_se(y, y_hat):
#     return (y - y_hat)**2


# assert calc_se(4, 2) == 4
# print(calc_se(2, 1))

# Câu 9
# assert round(approx_cos(), 2) == 0.54
# print(round(approx_cos(), 2))

# Câu 10
# assert round(approx_sin(), 4) == 0.8415
# print(round(approx_sin(), 4))

# Câu 11
# assert round(approx_sinh(), 2) == 1.18
# print(round(approx_sinh(), 2))