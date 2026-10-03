class Solution:
    def binary_search(self, spell: int, potions: list[int], success: int):
        left, right = 0, len(potions)
        while left < right:
            mid = (right + left) // 2
            if potions[mid] * spell >= success:
                right = mid
            else:
                left = mid + 1
        return left

    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        potions.sort()
        pairs = []
        length = len(potions)
        for spell in spells:
            pairs.append(length - self.binary_search(spell, potions, success))
        return pairs

