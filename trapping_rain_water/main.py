from typing import List

def trap(height: List[int]) -> int:
    total = 0
    buffer = 0
    l, r = 0, l + 1

    while l != len(height):
        while height[r] < height[l]:
            if r == len(height):
                buffer = 0
                l += 1
                r = l + 1
            buffer += height[l] - height[r]
            r += 1
        