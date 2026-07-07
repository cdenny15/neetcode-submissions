class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}

        for letter in s:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
            
        for let in t:
            if let in hashmap:
                hashmap[let] -= 1
        
        return all(val == 0 for val in hashmap.values())

        