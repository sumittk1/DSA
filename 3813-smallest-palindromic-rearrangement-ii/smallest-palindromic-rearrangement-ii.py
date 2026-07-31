import collections

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s, k):
        a = collections.Counter(s)

        if not self.ok(a):
            return ""

        b, c = self.half(a)

        d = self.count(b)

        if k > d:
            return ""

        e = self.build(b, k)

        return "".join(e) + c + "".join(e[::-1])

    def ok(self, a):
        b = 0
        for c in a.values():
            if c % 2:
                b += 1
        return b <= 1

    def half(self, a):
        b = [0] * 26
        c = ""

        for d, e in a.items():
            b[ord(d) - ord('a')] = e // 2
            if e % 2:
                c = d

        return b, c

    def count(self, a):
        return self.ways(a)

    def build(self, a, k):
        b = sum(a)
        c = []

        for _ in range(b):
            for d in range(26):
                if a[d] == 0:
                    continue

                a[d] -= 1
                e = self.ways(a)

                if e >= k:
                    c.append(chr(d + ord('a')))
                    break
                else:
                    k -= e
                    a[d] += 1

        return c

    def ways(self, a):
        b = sum(a)
        c = 1

        for d in a:
            c *= self.nck(b, d)

            if c >= self.MAX:
                return self.MAX

            b -= d

        return c

    def nck(self, a, b):
        c = 1

        for d in range(1, min(b, a - b) + 1):
            c = c * (a - d + 1) // d

            if c >= self.MAX:
                return self.MAX

        return c