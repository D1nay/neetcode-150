from typing import List
from collections import Counter
from pprint import pprint

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        # fast to implement:
        # k words n letters max

        # T: O(k * n) - creating a list of frequency lists
        # S: O(k) - space complexity for freq lists
        # General complexity is the same
    anagram_map = {}
    for word in strs:
        word_freq = frozenset(Counter(word))
        pprint(word_freq)
        if anagram_map.get(word_freq, 0) != 0:
            anagram_map[word_freq] = anagram_map[word_freq].append(word) 
        else:
            anagram_map[word_freq] = [word]
    return [value for value in anagram_map.values()]

     
