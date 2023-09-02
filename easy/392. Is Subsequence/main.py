def isSubsequence(s: str, t: str) -> bool:
    s, t = list(s[::-1]), list(t[::-1])


    for i in t[::]:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        elif s[-1] == t[-1]:
            s.pop()
            t.pop()
        elif s[-1] not in t[::]:
            return False
        else:
            t.pop()

    return len(s) == len(t)


assert isSubsequence('abc', 'ahbgdc') == True
assert isSubsequence('axc', 'ahbgdc') == False
assert isSubsequence('aaaaaa', 'bbaaaa') == False
assert isSubsequence('b', 'abc') == True
assert isSubsequence('ab', 'baab') == True

