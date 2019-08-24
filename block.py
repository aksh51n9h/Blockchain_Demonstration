class Block:
    def __init__(self, index, data, timestamp, previous_hash=0):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
