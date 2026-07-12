class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Create rank mapping
        rank = {}
        sorted_arr = sorted(set(arr))

        for i, num in enumerate(sorted_arr):
            rank[num] = i + 1

        # Build answer
        a = []
        for num in arr:
            a.append(rank[num])

        return a