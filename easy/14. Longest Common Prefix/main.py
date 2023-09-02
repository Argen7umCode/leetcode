class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = ''
        for letters in zip(*strs):
            s = set(letters)
            if len(s) == 1:
                result += list(s)[0]
            else:
                break
        return result