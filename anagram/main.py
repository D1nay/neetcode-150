from collections import Counter

def isAnagram(s: str, t: str) -> bool:

    # Collections API Counter T:O(N) S:O(1)
    # The dict is technically capped at 26 letters, so space complexity is O(1)

    # s_count = Counter(s) # T:O(N) S:O(1) 
    # t_count = Counter(t) # T:O(N) S:O(1)
    # if s_count == t_count: return True # T:O(1) S: 0
    # else: return False

    # Sorted string comparison T:O(N logN) S: O(N)
     
    # s_sorted = sorted(s) # T:O(N log N) S:O(N) 
    # t_sorted = sorted(t) # T:O(N log N) S:O(N)
    # if s_sorted == t_sorted: return True
    # else: return False

    # Vanilla python, no collections
    def get_char_freq_list(string):
        freq_list = {}
        for char in string:
            if freq_list.get(char, 0) == 0:
                freq_list[char] = 1
            else:
                freq_list[char] += 1
        return freq_list
    return get_char_freq_list(s) == get_char_freq_list(t)
