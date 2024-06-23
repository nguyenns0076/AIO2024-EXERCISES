'''
1. Cho một list các số nguyên num_list và một sliding window có kích thước
size k di chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải
có thể nhìn thấy đươc k số trong num_list và tìm số lớn nhất trong k
số này sau mỗi lần trượt k phải lớn hơn hoặc bằng 1
- Input:
    + list số nguyên num_list
    + Sliding window kích thước k
- Output: Kết quả số lớn nhất trong k số sau mỗi lần trược k
'''


def find_max_num_by_sliding_window(num_list=[], k=0):
    """
    Disc:
        Finds max number in list by sliding window.

    Args:
        None.

    Returns:
        None.

    Raises:
        ValueError: None.
        TypeError: None.

    Prompts:
        The user is prompted to enter n number.
        The user is prompted to enter number in list
        The user is prompted to enter sliding window size k

    Prints:
        None.
    """

    # # creating an empty list
    # num_list = []

    # # number of elements as input
    # n = int(input("Enter number of elements: "))

    # # iterating till the range
    # for i in range(0, n):
    #     ele = int(input())
    #     # adding the element
    #     num_list.append(ele)

    # # input size k
    # k = int(input("Enter size k : "))

    result = []

    # find max number in each loop with step = 1
    for i in range(0, len(num_list)):
        max_temp = 0
        end = len(num_list) + 1

        for j in range(i, k):  # loop from i to k  # noqa: E501
            if max_temp < num_list[j]:
                max_temp = num_list[j]
            if j == (k - 1):
                result.append(max_temp)
                k += 1

        if end == k:
            break
    return result
