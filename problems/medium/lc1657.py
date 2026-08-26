def get_freq(word: str) -> list:
    freq = [0] * 26
    base = ord("a")
    for char in word:
        freq[ord(char) - base] += 1
    return freq


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_freq = get_freq(word1)
        word2_freq = get_freq(word2)
        for i in range(26):
            if (word1_freq[i] == 0) != (word2_freq[i] == 0):
                return False
        return sorted(word1_freq) == sorted(word2_freq)
