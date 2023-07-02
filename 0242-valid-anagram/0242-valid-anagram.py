class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for character in s:
            if character not in counter:
                counter[character] = 0
            counter[character] += 1
        for character in t:
            if character not in counter:
                return False
            counter[character] -= 1
            if counter[character] == 0:
                del counter[character]
        return not counter