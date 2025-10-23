# You are given a string num consisting of only digits.
# A string of digits is called balanced if the sum of the digits at even indices
# is equal to the sum of digits at odd indices.
#
# Return true if num is balanced, otherwise return false.

tests = ["1234", "24123"]

def isBalanced(num: str) -> bool:
    # even, odd = 0, 0
    # for i, digit in enumerate(num):
    #     if i % 2 == 0:
    #         even += int(digit)
    #     else:
    #         odd += int(digit)
    # return True if even == odd else False
    even = num[0::2]
    odd = num[1::2]
    return True if sum(map(int, even)) == sum(map(int, odd)) else False


if __name__ == "__main__":
    for test in tests:
        print(isBalanced(test))