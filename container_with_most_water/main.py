'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form 
a container, such that the container contains the 
most water.

Return the maximum amount of water a container can 
store.

Notice that you may not slant the container.
'''

from typing import List

def maxArea(height: List[int]) -> int:
    def area(leftPointer, rightPointer, height):
        return abs(rightPointer - leftPointer) * min(height[leftPointer], height[rightPointer])

    # # Brute force solution
    # # T: O(n^2) S: O(1)
    # l, r = 0, len(height) - 1

    # currMax = 0
    # for l in range(len(height) - 1):
    #     for r in range(l + 1, len(height)):
    #         currMax = max(currMax, area(l, r, height))
    # return currMax


    # Two pointers
    # T: O(n), S: O(1)
    l, r = 0, len(height) - 1
    currMax = 0

    while l < r:
        currMax = max(currMax, area(l, r, height))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return currMax
