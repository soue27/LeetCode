# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# [3,2,2]  [1,2,2,4]  [1,1] [1,5,3,2,2,7,6,4,8,9]
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
from typing import List


nums_arr = [1,5,3,2,2,7,6,4,8,9]

def findErrorNums(nums: List[int]) -> List[int]:
    output = []
    seen = set()
    for x in nums:
        if x in seen:
            double = x
        seen.add(x)
    output.append(double)
    my_set = set(nums)
    for i in range(1, len(my_set) + 2):
        if i not in my_set:
            output.append(i)
    return output


if __name__ == "__main__":

    print(findErrorNums(nums_arr))