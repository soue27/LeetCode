# Given a string of English letters s, return the greatest English letter which occurs
# as both a lowercase and uppercase letter in s. The returned letter should be in uppercase.
# If no such letter exists, return an empty string.
# An English letter b is greater than another letter a if b appears after a in the English
# alphabet.
from stringprep import b1_set

tests = ["lEeTcOdE", "arRAzFif", "AbCdEfGhIjK", 'dllcdLpoapP']

def greatestLetter( s: str) -> str:
    upper = sorted({c for c in s if c.isupper()}, reverse=True)
    for bukva in upper:
        if bukva.lower() in s:
            return bukva
    return ''


if __name__ == "__main__":
    for test in tests:
        print(greatestLetter(test))


# best
# from string import ascii_uppercase;
# class Solution:
#     def greatestLetter(self, s: str) -> str:
#         char_list = [x for x in s];
#         for uppercase_char in ascii_uppercase[::-1]:
#             if uppercase_char in char_list and uppercase_char.lower() in char_list:
#                 return (uppercase_char);
#         return ""