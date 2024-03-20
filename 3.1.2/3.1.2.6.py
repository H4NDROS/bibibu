def triangle(a, b, c, d):
    s = [a, b, c, d]
    s.sort()
    if s[0] + s[1] > s[2] or s[0] + s[1] > s[3] or s[0] + s[2] > s[3] or s[1] + s[2] > s[3]:
        return True
    else:
        return False
print(triangle(12,65,54,0))
