# Given a string s, calculate its reverse degree.
#
# The reverse degree is calculated as follows:
#
# For each character, multiply its position in the reversed
# alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
# Sum these products for all characters in the string.
# Return the reverse degree of s.

import string

def reverseDegree(s: str) -> int:
    reverse_degree = 0
    letters = string.ascii_lowercase
    reverse_degree = sum([(len(letters) - letters.find(char)) * (i + 1) for i, char in enumerate(s)])
    return reverse_degree

def test_reverseDegree():
    assert reverseDegree("abc") == 148
    assert reverseDegree("zaza") == 160


if __name__ == "__main__":
    # test_reverseDegree()
    # print("OK")
    print(reverseDegree("zaza"))


# 12 ms Beats 14.04%
# 17.73 MB Beats 54.07%
#Best
    # def reverseDegree(self, s: str) -> int:
    #     dic = {'a': 26, 'b': 25, 'c': 24, 'd': 23, 'e': 22, 'f': 21, 'g': 20, 'h': 19, 'i': 18, 'j': 17, 'k': 16,
    #            'l': 15, 'm': 14, 'n': 13, 'o': 12, 'p': 11, 'q': 10, 'r': 9, 's': 8, 't': 7, 'u': 6, 'v': 5, 'w': 4,
    #            'x': 3, 'y': 2, 'z': 1}
    #
    #     total = 0
    #     for i in range(len(s)):
    #         raIndex = dic.get(s[i])
    #         product = ((i + 1) * raIndex)
    #         total += product
    #     return total