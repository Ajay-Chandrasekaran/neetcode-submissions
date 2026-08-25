class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for num, count in counter.items():
            freq[count].append(num)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result