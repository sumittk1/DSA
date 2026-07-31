class Solution(object):
    def minimumPushes(self, word):
        f = {}
        for ch in word:
            if ch in f:
                f[ch] += 1
            else:
                f[ch] = 1
        arr = []
        for value in f.values():
            arr.append(value)
        arr.sort(reverse=True)
        ans = 0
        for i in range(len(arr)):
            if i < 8:
                ans += arr[i] * 1
            elif i < 16:
                ans += arr[i] * 2
            elif i < 24:
                ans += arr[i] * 3
            else:
                ans += arr[i] * 4

        return ans