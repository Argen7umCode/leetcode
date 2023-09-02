class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = int(len(x) / 2)
        result = True
        for f, s in zip(x[:l], x[l:][::-1]):
            if f != s:
                result = False
                break
        return result

s = Solution()
print(s.isPalindrome(1231))
