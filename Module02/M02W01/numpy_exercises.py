import numpy as np

# cau 1 a
cau1 = np.arange(0, 10, 1)
print("cau1")
print(cau1)
print(type(cau1))
print("===========================")
# cau 2 c
cau2 = np.full((3, 3), fill_value=True, dtype=bool)
print("cau2")
print(cau2)
print(type(cau2[1, 2]))
print("===========================")
# cau 3 a
cau3 = np.arange(0, 10)
print(cau3[cau3 % 2 == 1])
print("===========================")
# cau 4 b
cau4 = np.arange(0, 10)
cau4[cau4 % 2 == 1] = -1
print(cau4)
print("===========================")
# cau 5 b
cau5 = np.arange(10)
cau5_2d = cau5.reshape(2, -1)
print(cau5_2d)
print("===========================")
# cau 6 a
cau6_1 = np.arange(10).reshape(2, -1)
cau6_2 = np.repeat(1, 10).reshape(2, -1)
cau6 = np.concatenate([cau6_1, cau6_2], axis=0)
print("Result: \n", cau6)
print("===========================")
# cau 7 c
cau7_1 = np.arange(10).reshape(2, -1)
cau7_2 = np.repeat(1, 10).reshape(2, -1)
cau7 = np.concatenate([cau7_1, cau7_2], axis=1)
print("Result: \n", cau7)
print("===========================")
# cau 8 a
cau8 = np.array([1, 2, 3])
print(np.repeat(cau8, 3))
print(np.tile(cau8, 3))
print("===========================")
# cau 9 c
cau9 = np.array([2, 6, 1, 9, 10, 3, 27])
value = np.where((cau9 >= 5) & (cau9 <= 10))
print("result", cau9[value])
print("===========================")
# cau 10 d


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


cau10_a = np.array([5, 7, 9, 8, 6, 4, 5])
cau10_b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(cau10_a, cau10_b))
print(type(pair_max(cau10_a, cau10_b)))
print("===========================")
# cau 11
cau11_a = np.array([5, 7, 9, 8, 6, 4, 5])
cau11_b = np.array([6, 3, 4, 8, 9, 7, 1])
print("Result", np.where(cau11_a < cau11_b, cau11_b, cau10_a))
print(type(np.where(cau11_a < cau11_b, cau11_b, cau10_a)))
print("===========================")
# cau 12
