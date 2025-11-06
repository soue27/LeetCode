# You are given an integer array nums of even length. 
# You have to split the array into two parts nums1 and nums2 such that:
# 
# nums1.length == nums2.length == nums.length / 2.
# nums1 should contain distinct elements.
# nums2 should also contain distinct elements.
# Return true if it is possible to split the array, and false otherwise.
from typing import List
from collections import Counter

def isPossibleToSplit(nums: List[int]) -> bool:
    counts = Counter(nums)
    result = [k for k, v in counts.items() if v > 2]
    if result:
        return False
    return True


def test_checkZeroOnes():
    assert isPossibleToSplit([1,1,2,2,3,4]) == True
    assert isPossibleToSplit([1,1,1,1]) == False

if __name__ == "__main__":
    test_checkZeroOnes()
    print("OK")
    # isPossibleToSplit([1,1,2,2,3,4, 1])


# 0 ms Beats 100.00%
# 17.84 MB Beats 40.62%