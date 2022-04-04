class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.linked_list={}
        self.recent_key=[]
        self.size=0
        

    def get(self, key: int) -> int:
        try:
            val=self.linked_list[key]
            self.recent_key.append(key)
            if len(self.recent_key)>self.capacity:
                del self.recent_key[0]
            return val
        
        except:
            return -1
    def sub_get(self, key: int) -> int:
        try:
            val=self.linked_list[key]
            return val
        except:
            return -1
                
    def put(self, key: int, value: int) -> None:
        t=self.sub_get(key)
        if t==-1:
            self.linked_list[key]=value
            self.size=self.size+1
            if self.size>self.capacity:
                del self.linked_list[self.recent_key[0]]
                self.size=self.size-1
        else:
            self.linked_list[key]=value
        self.recent_key.append(key)
        if len(self.recent_key)>self.capacity:
            del self.recent_key[0]
        print(self.size,self.linked_list,self.recent_key)
null="null"
action=["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
value=[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
expect=[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,18,null,null,null,-1,null,null,null,20,null,null,null,-1,18,18,null,null,null,null,20,null,null,null,null,null,null,null]
result=[]
for k in range(0,len(action)):
    if action[k]=="LRUCache":
        L=LRUCache(value[k][0])
        result.append(null)
    elif action[k]=="put":
        L.put(value[k][0],value[k][1])
        result.append(null)
    elif action[k]=="get":
        result.append(L.get(value[k]))
for k in range(0,len(result)):
    if result[k]!=expect[k]:
        pass
print(expect)
print(result)
