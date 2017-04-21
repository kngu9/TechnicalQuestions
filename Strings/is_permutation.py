'''
CTCI 1.2
'''

def isPermutation(s, k):
  s = sorted(s)
  k = sorted(k)

  return s == k

print(isPermutation('god', 'dog'))
