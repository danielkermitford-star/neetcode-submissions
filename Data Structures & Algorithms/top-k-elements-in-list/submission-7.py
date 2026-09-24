class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for i in range(len(nums)+1)]
        for num, freq in Counter(nums).items():
            freq_list[freq].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            result += freq_list[i]
            if len(result) == k:
                return result
        
        # return [n for n,_ in Counter(nums).most_common(k)]