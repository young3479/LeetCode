class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value = set()

        for n in nums:
            if n in value:
                return True
            value.add(n)
        return False
        