from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran=set(ransomNote)
        for i in ran:
            if(magazine.count(i)<ransomNote.count(i)):
                return False
        return True     
