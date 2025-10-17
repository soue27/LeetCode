# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

from typing import List

test = [37,12,28,9,100,56,80,5,12]


def arrayRankTransform(arr: List[int]) -> List[int]:
    slovar = {k : v for v, k in enumerate(sorted(set(arr)))}
    output_list = [slovar.get(num)+1 for num in arr]
    return output_list


if __name__ == "__main__":
    print(arrayRankTransform(test))