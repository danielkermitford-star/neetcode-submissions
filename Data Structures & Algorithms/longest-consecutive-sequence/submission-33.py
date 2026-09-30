class Solution:
    # classic DP problem if the order mattered
    # Let LCS(n) be the length of the LCS ending with 
    # the current value, n.
    # LCS(n) = 1 if n-1 is not left of n in the list
    # LCS(n) = 1 + LCS(n-1) otherwise
    # Since it doesn't you could sort it, but this takes O(nlgn)

    # you could create linked lists of consecutive elements
    # or just keep track of the consecutive ranges of numbers

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     lcs = {}
    #     if not nums:
    #         return 0
    #     for n in sorted(set(nums)):
    #         lcs[n] = 1 + lcs.get(n - 1, 0)
    #     return max(lcs.values())

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     i = {}  # map from start to end of sequence
    #     d = {}  # map from end to start of sequence
    #     for n in nums:
    #         if n-1 in d and n+1 in i:
    #             s = d[n-1]
    #             e = i[n+1]
    #             i[s] = e
    #             d[e] = s
    #             del d[n-1]
    #             del i[n+1]
    #         elif n+1 in i:
    #             e = i[n+1]
    #             i[n] = e
    #             d[e] = n
    #             del i[n+1]
    #         elif n-1 in d:
    #             s = d[n-1]
    #             d[n] = s
    #             i[s] = n
    #             del d[n-1]
    #         elif n not in d and n not in i:
    #             i[n] = n
    #             d[n] = n

    #     lcs = 0
    #     for k,v in i.items():
    #         if lcs < v + 1 - k:
    #             lcs = v + 1 - k
    #         # lcs = max(lcs, v+1-k)
        
    #     return lcs

    # per the, last, hint, use a single map that contains 
    # all the numbers seen so far and maps every endpoint 
    # of a known sequence to the length of said sequence. 
    # Iterate through nums, ignoring values that have already
    # been seen, and are hence part of a known sequence - or
    # iterate through a the set of unique elements in nums. 
    # If n-1 is part of a known sequence, then, because n is not,
    # n-1 is the larger end of a known sequece that will be 
    # extended by n.  Similarly, if n+1 is part of a known sequence
    # then it is the smaller end and will be extended by n. Note 
    # that if both n-1 and n+1 are both part of a known sequence, 
    # then n joins the two known sequences whose new length is one 
    # more than the sum of the lengths of the two joined sequences. 
    # In only one of n-1 or n+1 is part of a known sequence then 
    # the length of the new sequence will increase by 1 because of 
    # the addition of n. 
    # How can we quickly find out if n-1 and n+1 are part of a known
    # sequence and also get the length of these sequences?  A hash map! 
    # If n becomes an endpoint of a sequence, add n as a key to the
    # map whose value is the length of the sequence. If n adds to 
    # an existing sequence, or combines two sequences, query the 
    # endpoints in the map for the length of the old sequence, and
    # update the values of the endpoints of the new sequence with 
    # its length. 
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     seq_lengths = {}
    #     for n in set(nums):
    #         # if n not in seq_lengths:
    #             if n-1 in seq_lengths and n+1 in seq_lengths:
    #                 start = n - seq_lengths[n-1]
    #                 end = n + seq_lengths[n+1]
    #                 length = 1 + seq_lengths[n-1] + seq_lengths[n+1]
    #                 seq_lengths[start] = length
    #                 seq_lengths[end] = length
    #                 seq_lengths[n] = length
    #             elif n-1 in seq_lengths:
    #                 start = n - seq_lengths[n-1]
    #                 length = 1 + seq_lengths[n-1]
    #                 seq_lengths[start] = length
    #                 seq_lengths[n] = length
    #             elif n+1 in seq_lengths:
    #                 end = n + seq_lengths[n+1]
    #                 length = 1 + seq_lengths[n+1] 
    #                 seq_lengths[end] = length
    #                 seq_lengths[n] = length
    #             else:
    #                 seq_lengths[n] = 1
    #     if seq_lengths:
    #         return max(seq_lengths.values())
    #     else:
    #         return 0
            
    # # or put them all in a hash set and remove 'adjacent' values
    # # like in a depth first search in both directions
    # # incrementing by one and then decrementing by one
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     num_set = set(nums)
    #     max_length = 0
    #     while num_set:
    #         n = num_set.pop()
    #         right = n+1
    #         while right in num_set:
    #             num_set.discard(right)
    #             right += 1
    #         left = n-1
    #         while left in num_set:
    #             num_set.discard(left)
    #             left -=1
    #         max_length = max(max_length, right-1-left)
    #     return max_length
    
    # or put them all in a hash set, loop through the numbers,
    # n, that could start a sequence, i.e. where n-1 is not in 
    # the set, and just search forward like before. 
    # This is literally half as long because you only have to 
    # search forward and you don't have to remove any elements,
    # at the cost of an if statement.
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        max_length = 0
        for n in nums:
            if n-1 not in set_of_nums:
                end = n+1
                while end in set_of_nums:
                    end += 1
                max_length = max(max_length, end - n)
        return max_length

            