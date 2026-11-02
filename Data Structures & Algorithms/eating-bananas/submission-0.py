class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        
        r = piles[-1]
        l = 1
        least_k = -1

        while l <= r:
            hrs = 0
            m = (l + r) // 2

            for b in piles:
                hrs += math.ceil(b / m)
            
            if hrs > h:
                l = m + 1
            else:
                least_k = m
                r = m - 1
        return least_k
