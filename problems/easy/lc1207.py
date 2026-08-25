class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hash_map = {}
        for num in arr:
            hash_map[num] = hash_map.get(num, 0) + 1
        return len(hash_map) == len(set(hash_map.values()))
