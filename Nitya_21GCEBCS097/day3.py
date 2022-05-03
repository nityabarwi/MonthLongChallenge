class Solution:
    def findUnsortedSubarray(self, N: List[int]) -> int:
        lenN, left, right = len(N) - 1, -1, -1
        maxN, minN = N[0], N[lenN]
        for i in range(1, len(N)):
            a, b = N[i], N[lenN-i]
            if a < maxN: right = i
            else: maxN = a
            if b > minN: left = i
            else: minN = b
        return max(0, left + right - lenN + 1)
