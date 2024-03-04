def spaced(s):
    for c in s:
        return (c, end= " ")

x = spaced("hello")
print(x)