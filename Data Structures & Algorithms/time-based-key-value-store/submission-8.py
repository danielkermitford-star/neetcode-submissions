class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.map.setdefault(key,{})[timestamp] = value
        self.map.setdefault(key,[]).append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        # return self.map[key][timestamp]
        if key not in self.map:
            return ''
        timestamps = self.map[key]
        if not timestamps or timestamps[0][0] > timestamp:
            return ''
        left, right = 1, len(timestamps)-1
        while left <= right:
            mid = (left + right) // 2
            if timestamps[mid][0] == timestamp:
                return timestamps[mid][1]
            elif timestamps[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1 # might be too far
        if right == -1:
            return ''
        else:
            return timestamps[right][1]