class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.keys.get(key, False):
            self.keys[key].append([value,timestamp])
        else:
            self.keys[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        if self.keys.get(key , False):
            array = self.keys[key]
        else:
            return res
        l = 0
        r = len(array)- 1
        mid = -1
        while l <= r:
            mid = math.floor((l + r) / 2)
            if array[mid][1] > timestamp:
                r = mid -1
            elif array[mid][1] <= timestamp:
                l = mid + 1
                res = array[mid][0]
        
        return res