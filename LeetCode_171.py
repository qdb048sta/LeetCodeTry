import math
def titleToNumber(columnTitle):
    import math
    list_of_number={"A":1,
                    "B":2,
                    "C":3,
                    "D":4,
                    "E":5,
                    "F":6,
                    "G":7,
                    "H":8,
                    "I":9,
                    "J":10,
                    "K":11,
                    "L":12,
                    "M":13,
                    "N":14,
                    "O":15,
                    "P":16,
                    "Q":17,
                    "R":18,
                    "S":19,
                    "T":20,
                    "U":21,
                    "V":22,
                    "W":23,
                    "X":24,
                    "Y":25,
                    "Z":26
                    }
    pos=0
    count=len(columnTitle)-1
    for i in columnTitle:
        print(count)
        print(math.pow(26,count))
        pos=pos+list_of_number[i]*(math.pow(26,count))
        count=count-1
    return pos
titleToNumber("A")
