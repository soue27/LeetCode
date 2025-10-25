# Given a 0-indexed integer array nums, determine whether there exist
# two subarrays of length 2 with equal sum. Note that the two subarrays must begin at
# different indices.
#
# Return true if these subarrays exist, and false otherwise.
#
# A subarray is a contiguous non-empty sequence of elements within an array.



from typing import List


def findSubarrays(nums: List[int]) -> bool:
    sums = []
    for i in range(len(nums) - 1):
        rez = nums[i] + nums[i + 1]
        if rez in sums:
            return True
        sums.append(rez)
    return False



def test_findSubarrays():
    assert findSubarrays([4,2,4]) == True
    assert findSubarrays([1,2,3,4,5]) == False
    assert findSubarrays([0,0,0]) == True


if __name__ == "__main__":
    test_findSubarrays()
    print("OK")
    # print(findSubarrays([0,0,0]))


# Best
# class Solution:
#     def findSubarrays(self, nums: List[int]) -> bool:
#         sums = set()
#         n = len(nums)
#         for i in range(n):
#             if i + 2 <= n:
#                 curr_sum = sum(nums[i:i + 2])
#                 if curr_sum in sums:
#                     return True
#                 else:
#                     sums.add(curr_sum)
#
#         return False