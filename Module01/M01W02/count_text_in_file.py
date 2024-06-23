'''
3. Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
với key là từ và value là số lần từ đó xuất hiện
- Input: Đường dẫn đến file txt
- Output: dictionary đếm số lần các từ xuất hiện
'''


def count_text_in_file(file_path):
    """
        Disc:
            Count word in text

        Args:
            None.

        Returns:
            Word dictionary.

        Prompt:
            None.
        """

    with open(file_path, 'r') as file:
        data = file.read()
        file.close()

    text = data.split(' ')
    word_count = {}

    for word in text:
        if word.lower() in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

