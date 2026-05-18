class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_map = defaultdict(list)

        
        for word in strs:
            sorted_s = "".join(sorted(word))
            new_map[sorted_s].append(word)

        
        return list(new_map.values())