def isIsomorphic(s: str, t: str) -> bool:
    r = {}
    f = {}
    for l1, l2 in zip(s, t):
        if any([(l1 in r.keys() and r[l1] != l2), (l2 in f.keys() and f[l2] != l1)]):
            return False
        r[l1] = l2
        f[l2] = l1
    return True

assert isIsomorphic('badc', 'baba') == False
assert isIsomorphic('egg', 'add') == True
assert isIsomorphic('foo', 'bar') == False
assert isIsomorphic('paper', 'title') == True