# Given a 32-bit integer num, return a string representing its hexadecimal
# representation. For negative integers, two’s complement method is used.
#
# All the letters in the answer string should be lowercase characters, and
# there should not be any leading zeros in the answer except for the zero itself.
#
# Note: You are not allowed to use any built-in library method to directly
# solve this problem.

inttohex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
}

def toHex(num: int) -> str:
    hexstr = ''
    if num == 0:
        return '0'
    elif num > 0:
        while num > 0:
            remainfer = num % 16
            hexstr = inttohex[remainfer] + hexstr
            num = num // 16
        return hexstr
    else:
        # Handle negative numbers using two's complement
        num = (1 << 32) + num  # Convert to 32-bit two's complement
        while num > 0:
            remainder = num % 16
            hexstr = inttohex[remainder] + hexstr
            num = num // 16
        return hexstr.lstrip('0') or '0'


if __name__ == "__main__":
    print(toHex(-1))
    print("OK")


#Решение лучшее, но решил не сам