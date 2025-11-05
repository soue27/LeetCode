# Given a binary string s, return true if the longest contiguous segment of 1('s is strictly longer than the longest '
# contiguous segment of 0')s in s, or return false otherwise.
#
# For example, in s = "110100010" the longest continuous segment of 1s has length 2,
# and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered
# to have a length 0. The same applies if there is no 1's.


def checkZeroOnes(s: str) -> bool:
    print(set(s.split("0")), set(s.split("1")))
    print(max(set(s.split("0"))), max(set(s.split("1"))))
    print(len(max(set(s.split("0")))), len(max(set(s.split("1")))))
    if "1" not in s:
        return False
    elif "0" not in s:
        return True
    else:
        if len(max(set(s.split("0")))) > len(max(set(s.split("1")))):
            return True
        else:
            return False


def test_checkZeroOnes():
    assert checkZeroOnes("1101") == True
    assert checkZeroOnes("111000") == False
    assert checkZeroOnes("110100010") == False
    assert checkZeroOnes("1") == True
    assert checkZeroOnes("111111") == True
    assert checkZeroOnes("00000") == False

if __name__ == "__main__":
    test_checkZeroOnes()
    print("OK")
    checkZeroOnes("1")

# 3ms Beats 27.25%

#Best
# class Solution:
#     def checkZeroOnes(self, s: str) -> bool:
#         zeroes = 0
#         ones = 0
#         ones_so_far = 0
#         zeroes_so_far = 0
#         for char in s:
#             if char == '0':
#                 ones = max(ones,ones_so_far)
#                 ones_so_far = 0
#                 zeroes_so_far+=1
#             else:
#                 zeroes = max(zeroes,zeroes_so_far)
#                 zeroes_so_far = 0
#                 ones_so_far +=1
#         ones = max(ones,ones_so_far)
#         zeroes = max(zeroes,zeroes_so_far)
#
#         return ones>zeroes
