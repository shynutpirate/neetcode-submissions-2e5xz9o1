class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for ele in s:
            count[ele] = count.get(ele, 0) + 1
        
        for ele in t:
            if ele not in count:
                return False
            count[ele] -= 1
            if count[ele] < 0:
                return False
        return True

            
        