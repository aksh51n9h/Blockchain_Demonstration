import hashlib


class Block:
    def __init__(self, index, data, timestamp, previous_hash=0):
        self.__index = index
        self.__data = data
        self.__timestamp = timestamp
        self.__self_hash = self.__hash_data()
        self.__previous_hash = previous_hash

    def __hash_data(self):
        encoded_data = (str(self.__index) + str(self.__data) + str(self.__timestamp)).encode()
        return hashlib.sha256(encoded_data).hexdigest()

    def get_self_hash(self):
        return self.__self_hash
