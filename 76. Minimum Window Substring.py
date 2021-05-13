class Solution:
    def minWindow(self, s: str, t: str) -> str:
        record={}
        for i in t:
            indexing=s.find(i)
            if indexing==-1:
                break
                return ""
            if i not in record:
                record[i]=[indexing]
            else:
                record[i]=record[i].append(indexing)
        numdist=[]
        for k in record.keys():
            numdist=numdist.append(record[k])
        for i in numdist:
            sublength=len(i)
            for            
            
        