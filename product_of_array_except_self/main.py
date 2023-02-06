'''
Given an integer array nums, return an array answer
such that answer[i] is equal to the product of all
the elements of nums except nums[i].

The product of any prefix or suffix of nums is
guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n)
time and without using the division operation.
'''

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    # # Prefix and suffix arrays
    # # T: O(n), S: O(n)

    # # Check for corner cases
    # if not nums: return [0]
    # if len(nums) == 1: return [0]


    # def prodPrefixOrSuffixArray(nums: List[int], isSuffix: bool) -> List[int]:
    #     # T: O(n), S: O(n)

    #     var = 1
    #     result = [1]
    #     if isSuffix: nums = reversed(nums)
    #     for num in nums:
    #         result.append(var * num)
    #         var = var * num
    #     result = result[:-1]
    #     return result

    # result = []
    # prefix = prodPrefixOrSuffixArray(nums, False)
    # suffix = prodPrefixOrSuffixArray(nums, True)

    # # T: O(n), S: O(n)
    # for pref, suff in zip(prefix, reversed(suffix)):
    #     result.append(pref * suff)
    # return result




    # # O(1) space complexity solution using the 'free' output array
    # # T: O(n), S: O(1) (that is, additional complexity) 

    # # Check for corner cases
    # if not nums: return [0]
    # if len(nums) == 1: return [0]
    # def prodPrefixOrSuffixArray(nums: List[int], isSuffix: bool) -> List[int]:
    #     var = 1
    #     result = [1]
    #     if isSuffix: nums = reversed(nums)
    #     for num in nums:
    #         result.append(var * num)
    #         var = var * num
    #     result = result[:-1]
    #     return result
    
    # result = prodPrefixOrSuffixArray(nums, False)

    # suffix_var = 1
    # for index, num in reversed(list(enumerate(nums))):
    #     result[index] = result[index] * suffix_var
    #     suffix_var = suffix_var * num
    # return result


    # Neetcode S: O(1) solution

    # Check for corner cases
    if not nums: return [0]
    if len(nums) == 1: return [0]

    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
