'''
CTCI 1.1
'''

def isUnique(s):
  if len(s) <= 1:
    return True

  s = sorted(s)

  for i in range(1, len(s)):
    if s[i-1] == s[i]:
      return False

  return True

print(isUnique('helo'))
