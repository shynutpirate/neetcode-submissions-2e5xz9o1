class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for w in strs:
            key = ''.join(sorted(w))
            anagrams[key].append(w)
        
        return list(anagrams.values())