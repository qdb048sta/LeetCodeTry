class Solution:
    def minWindow(self, s: str, t: str) -> str:
        record=[]
        for i in t:
            indexing=s.find(i)
            if indexing==-1:
                break
                return ""
            
        