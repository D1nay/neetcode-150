from typing import List
from collections import defaultdict

def twoSum(nums: List[int], target: int) -> List[int]:
    
    # # Brute
    # # Check every possible pair 
    # # T: O(n^2) S: O(1)
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i != j:
    #             if nums[i] + nums[j] == target: return [i, j]

    # Look up in hashmap value:index  my implementation
    # T: O(N) S: O(N)
    # def create_indices_dict(lst: List):
    #     index_dict = defaultdict(list)
    #     for index, elem in enumerate(lst):
    #         index_dict[elem].append(index)
    #     return dict(index_dict)

    # hashmap = create_indices_dict(nums)
    # for i in range(len(nums)):
    #     summand = target - nums[i]
    #     if summand in hashmap:
    #         summand_indices = hashmap[summand]
    #         if (summand == nums[i]):
    #             if (len(summand_indices) > 1):
    #                 return [i, summand_indices[1]]
    #         else:
    #             return [i, summand_indices[0]]


    # Look up in hashmap value:index neetcode
    # T: O(N) S: O(N)
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
