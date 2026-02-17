from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return (Counter(ransomNote)-Counter(magazine))=={}