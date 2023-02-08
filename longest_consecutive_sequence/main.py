'''
Given an unsorted array of integers nums, return
the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    # Lookup in set
    # T: O(n) S: O(n)

    numsSet = set(nums) # T: O(n) S: O(n)
    maxSeqSize = 0
    for num in numsSet: # T: O(n + n) S: O(1); goes over every element at most twice
        if (num - 1) not in numsSet:
            nextNum = num
            while nextNum in numsSet:
                nextNum += 1
            seqSize = nextNum - num
            if maxSeqSize < seqSize: maxSeqSize = seqSize
    return maxSeqSize
    
