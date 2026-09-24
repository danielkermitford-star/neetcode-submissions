class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            sstr = "".join(sorted(str))
            anagrams[sstr].append(str)
        return list(anagrams.values())