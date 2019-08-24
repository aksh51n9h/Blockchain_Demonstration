import hashlib


class Block:
    def __init__(self, index, data, timestamp, previous_hash=0):
        self.__index = index
        self.__data = data
        self.__timestamp = timestamp
        self.__self_hash = self.__hash_data()
        self.__previous_hash = previous_hash

    def __hash_data(self):
        return hashlib.sha256(str(self.__index) + self.__data + self.__timestamp).hexdigest()
