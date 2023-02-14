class MyHashMap(object):
    def init(self):
        self.arr = [-1] * 1000001

    def put(self, key, value):
        self.arr[key] = value

    def get(self, key):
        return self.arr[key]

    def remove(self, key):
        self.arr[key] = -1
