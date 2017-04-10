"""
Given an array find the pair of elements that add up to the target
arr = [8, 7, 2, 5, 3, 1]
sum = 10
answer = [8, 2]

If there are multiples, return all combinations.
"""

def findElements(arr, target):
    h = {}
    ans = []

    for el in arr:
        h[el] = 1

    for el in arr:
        need = target - el

        if need in h:
            temp = [el, need]
            ans.append(temp)

    return ans

if __name__ == '__main__':
    arr = [8, 7, 2, 5, 3, 1]
    target = 10

    print(findElements(arr, target))


