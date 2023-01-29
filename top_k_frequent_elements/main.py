from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Hashmap solution vanilla
    # Worst case: all different nums
    # T: O(n logn)
    # S: O(n)

    # Unanswered: what to do when there are several elements with the same frequency?
    # E.g. nums = [1, 2, 2, 3, 3, 3, 4, 4], k = 2
    # Should it return [3, 2], [3, 4] OR [3, 2, 4]? 

    hashmap = {}
    for num in nums: # T: O(n) S: O(n)
        if num in hashmap:
            hashmap[num] += 1
        else: 
            hashmap[num] = 1

    # T: O(n logn) S: O(n)
    sorted_by_value = sorted(hashmap.items(), key=lambda pair: pair[1], reverse=True) 
    return [sorted_by_value[i][0] for i in range(k)]