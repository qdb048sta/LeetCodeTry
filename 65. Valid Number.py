class Solution:
    def isNumber(self, s: str) -> bool:
        if s.count("e")==1 :
            l=s.split("e")
            if l[1].count("+")==1 or l[1].count("-")==1 or ("+" not in l[1] and "-" not in l[1]):
                try:
                    int(l[1])
                    if l[0].count("+")==1 or l[0].count("-")==1 or ("+" not in l[0] and "-" not in l[0]):
                            try:
                                float(l[0])
                                return True
                            except:
                                return False
                    else:
                        return False
                    
                except:
                    return False
            else:
                return False
        elif s.count("E")==1:
            l=s.split("E")
            if l[1].count("+")==1 or l[1].count("-")==1 or ("+" not in l[1] and "-" not in l[1]):
                try:
                    int(l[1])
                    if l[0].count("+")==1 or l[0].count("-")==1 or ("+" not in l[0] and "-" not in l[0]):
                            try:
                                float(l[0])
                                return True
                            except:
                                return False
                    else:
                        return False
                    
                    
                except:
                    return False
        elif "inf" in s.lower():
            return False
        else:
            if s.count("+")==1 or s.count("-")==1 or ("+" not in s and "-" not in s):
                    try:
                        float(s)
                        return True
                    except:
                        return False
            else:
                return False
        