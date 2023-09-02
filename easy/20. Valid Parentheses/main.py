
def isValid(s: str) -> bool:
    s = list(s)[::-1]
    for f, s in zip(s, s[1:]):
        if any(f == l1 and s != l2 for l1, l2 in zip('}])', '{[(')):
            return False
    return True

print(isValid('()'))
print(isValid('(]'))