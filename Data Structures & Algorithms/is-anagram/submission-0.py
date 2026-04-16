class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1
        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
            if hashmap[char] == 0:
                del hashmap[char]
        if len(hashmap) == 0:
            return True
        return False