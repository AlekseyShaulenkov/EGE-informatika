from itertools import *
r = '457 46 567 12 136 235 13'.split()
s = 'EF EC CA AB BD CG GF DG'.split()
print('1 2 3 4 5 6 7')
for i in permutations('ABCDEFG'):
    if all(str(i.index(y) + 1) in r[i.index(x)] for x, y in s):
           print(*i)
           
    
    

