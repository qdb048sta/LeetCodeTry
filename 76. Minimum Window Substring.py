class Solution:
    def minWindow(self, s: str, t: str) -> str:
        record=[]
        for i in t:
            indexing=s.find(i)
            record.append(indexing)
        if -1 in record:
            return ""
        else:
            record=sorted(record)
            maximum=record[-1]
            minimum=record[0]
            substring=s[minimum:maximum]
            return substring
        