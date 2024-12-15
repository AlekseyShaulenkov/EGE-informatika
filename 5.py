def r(n):
    R = bin(n)[2:]
    if n % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '01'
    return int(R, 2)
res = []
for n in range(1, 13):
    res.append(r(n))
print(max(res))
    
