'''
2. Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện
- Input: một từ
- Output: dictionary đếm số lần các chữ xuất hiện
'''


def count_characters(word):
    """
    Disc:
        Count char in word.

    Args:
        None.

    Returns:
        Char dictionary.

    Prompt:
        The user is prompted to enter word.
    """

    # Init dictionary
    char_count = {}

    # Loop through word
    for char in word:
        # Checks char is in dic yet
        if char in char_count:
            # yes, value + 1
            char_count[char] += 1
        else:
            # no, add key = char, value = 1
            char_count[char] = 1

    return char_count


