s = set([1, 2, 3, 4])
print(type(s))
print(s)

s1 = set()
s1.add(1)
s1.add(1)
s2 = s1.union({1, 2, 3})
print(s1, s2)
s3 = s1.intersection({1, 2, 3})
print(s1, s3)