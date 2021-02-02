i = 0
n1 = 1
n2 = 1
n3 = 0
s = []
while n3 < 4000000 or n2 < 4000000:
    n3 = n1 + n2
    n2 = n2 + n3
    n1 = n3
    i += 1
    print(n3, n2)
    if n3 % 2 ==0 and n3 < 4000000:
        s.append(n3)
    if n2 % 2 == 0 and n2 < 4000000:
        s.append(n2)
print(s)
print(sum(s))
