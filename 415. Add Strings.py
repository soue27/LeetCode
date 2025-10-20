# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
import sys


sys.set_int_max_str_digits(10000)

def addStrings(num1: str, num2: str) -> str:
    return str(int(num1) + int(num2))


if __name__ == "__main__":
    print(addStrings('1', '123'))