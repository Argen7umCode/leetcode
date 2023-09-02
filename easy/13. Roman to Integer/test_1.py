from main import Solution

s = Solution()


def test_1():
    n = 121
    assert s.isPalindrome(n) == True

def test_2():
    n = 1231
    assert s.isPalindrome(n) == False

def test_3():
    n = 1
    assert s.isPalindrome(n) == True

def test_4():
    n = 12121
    assert s.isPalindrome(n) == True