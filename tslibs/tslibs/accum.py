
class MaxAccum(object):
    
    def __init__(self):
        self.__dict__["store"] = []
        self.__dict__["sum"] = 0
        self.__dict__["count"] = 0
        self.__dict__["max"] = 0
        self.__dict__["min"] = float('inf')
        self.__dict__["max_index"] = -1
        self.__dict__["min_index"] = -1

    def __len__(self):
        return len(self.store)

    def __setattr__(self, name, value):
    
        if value is not None and name == "v":
            self.__dict__["store"].append(value)
            self.__dict__["sum"] += value
            self.__dict__["count"] += 1
            if self.__dict__["max"] < value:
                self.__dict__["max"] = value
                self.__dict__["max_index"] = self.__dict__["count"]-1
            if self.__dict__["min"] > value:
                self.__dict__["min"] = value
                self.__dict__["min_index"] = self.__dict__["count"]-1

    def __getattribute__(self, name: str):
        if name == "v":
            return self.store[-1]
        return super().__getattribute__(name)
        
    def __str__(self) -> str:
        end = 5
        if self.count < 5:
            end = self.count
        return f"{self.store[:end]}\nLen: {self.count}\nSum: {self.sum}"

    def normalise(self):
        s = self.__dict__["store"]
        mx = self.__dict__["max"]
        if mx != 0:
            return [i/mx for i in s],mx
        else:
            return [],mx


class NumAccum(object):
    
    def __init__(self):
        self.__dict__["store"] = []
        self.__dict__["sum"] = 0
        self.__dict__["count"] = 0

    def __len__(self):
        return len(self.store)

    def __setattr__(self, name, value):
    
        if value is not None and name == "v":
            self.__dict__["store"].append(value)
            self.__dict__["sum"] += value
            self.__dict__["count"] += 1

    def __getattribute__(self, name: str):
        if name == "v":
            return self.store[-1]
        return super().__getattribute__(name)
        
    def __str__(self) -> str:
        end = 5
        if self.count < 5:
            end = self.count
        return f"{self.store[:end]}\nLen: {self.count}\nSum: {self.sum}"
        


class ObjAccum(object):
    
    def __init__(self):
        self.__dict__["store"] = []
        self.__dict__["count"] = 0

    def __len__(self):
        return len(self.store)

    def __setattr__(self, name, value):
    
        if value is not None and name == "v":
            self.__dict__["store"].append(value)
            self.__dict__["count"] += 1

    def __getattribute__(self, name: str):
        if name == "v":
            return self.store[-1]
        return super().__getattribute__(name)
        
    def __str__(self) -> str:
        end = 5
        if self.count < 5:
            end = self.count
        return f"{self.store[:end]}\nLen: {self.count}"
        
if __name__ == "__main__":
    #Tests

    x = NumAccum()
    y = ObjAccum()
    x.v = 10
    y.v = 100
    print(x,y)

    for i in range(0,1000000):
        x.v = i
        y.v = i+1

    print(x,x.sum,x.count)

    





