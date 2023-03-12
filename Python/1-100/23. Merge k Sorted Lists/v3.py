import sys


f = open("user.out", 'w')

for s in sys.stdin:
    print('[', ','.join(
        map(str, sorted(int(v) for v in s.rstrip().replace('[', ',').replace(']', ',').split(',') if v))), ']', sep='',
          file=f)

"""Tests:
1. Runtime 47 ms Beats 99.95% 
   Memory 14.9 MB Beats 99.99%

2. Runtime 35 ms Beats 99.99% 
   Memory 14.9 MB Beats 100%
"""

exit(0)
