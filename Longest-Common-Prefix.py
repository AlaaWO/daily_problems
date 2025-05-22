class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        smallest = min(strs, key=len)
        flag = 0
        comparison = ""

        for i in range(len(smallest)):
            flag = 0
            comparison += smallest[i]
            for j in range(len(strs)):
                if strs[j].startswith(comparison):
                    flag +=1
            if flag == len(strs):
                longest = comparison
        return longest

            