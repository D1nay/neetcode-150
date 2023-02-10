'''
Given an integer array nums, return all the
triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and 
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must 
not contain duplicate triplets.
'''

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # Pointer + two sum solution (neetcode)
    # two nested loops with 'n' elements at worst
    # T: O(nlogn + n^2) = O(n^2) S: O(n)


    nums.sort() # T: O(nlogn) S: O(n) additional space for timsort worst case
    answer = []

    for i, a in enumerate(nums): # T: O(n) S: O(1)
        if i > 0 and nums[i - 1] == a:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r: # T: O(n) S: O(1)
            sum = a + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                answer.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return answer
