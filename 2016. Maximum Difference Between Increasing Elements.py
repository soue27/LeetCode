# Given a 0-indexed integer array nums of size n, find the maximum difference
# between nums[i] and nums[j] (i.e., nums[j] - nums[i]),
# such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

from typing import List

test = [87,68,91,86,58,63,43,98,6,40]

def maximumDifference(nums: List[int]) -> int:
    itog = []
    for i, num in enumerate(nums):
        max1 = max(nums[i:])
        itog.append(max1 - num)
    print(itog)
    return -1 if max(itog) == 0 else max(itog)


if __name__ == "__main__":
    print(maximumDifference(test))


# Best
# def maximumDifference(self, nums: List[int]) -> int:
#     res, prev = 0, nums[0]
#     for v in nums:
#         res = max(res, v - prev)
#         prev = min(prev, v)
#     return -1 if res == 0 else res