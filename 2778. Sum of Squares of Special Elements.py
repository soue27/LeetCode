# You are given a 1-indexed integer array nums of length n.

# An element nums[i] of nums is called special if i 
# divides n, i.e. n % i == 0.

# Return the sum of the squares of all special elements of nums.
from typing import List

pl1 = [2,7,1,19,18,3]


def sumOfSquares(nums: List[int]) -> int:
    spec_elem = [nums[i-1] * nums[i-1] for i in range(1, len(nums)+1) if len(nums) % i == 0]
    # for i in range(1, len(nums)+1):
    #     if len(nums) % (i) == 0:
    #         spec_elem.append(nums[i-1] * nums[i-1])
    return sum(spec_elem)

def test_sumOfSquares():
    assert sumOfSquares([1,2,3,4]) == 21
    assert sumOfSquares([2,7,1,19,18,3]) == 63


if __name__ == "__main__":
    test_sumOfSquares()
    print("OK")
    print(sumOfSquares(pl1))

# Best:

# Runtime 0 ms Beats 100.00%
# Memory 17.98 MB Beats 24.59%
