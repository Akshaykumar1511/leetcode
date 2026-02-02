class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin=defaultdict(list)
        for word in strs:
            key=tuple(sorted(Counter(word).items()))
            fin[key].append(word)
        return list(fin.values())