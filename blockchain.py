from block import Block


class BlockChain:
    def __init__(self, index, timestamp, data, prev_hash):
        self.__block_chain = list()
        self.__block_chain.append(Block(index, timestamp, data, timestamp))

    def validate_chain(self):
        for i in range(0, len(self.__block_chain)):
            current_hash = self.__block_chain[i].get_self_hash()
            next_hash = self.__block_chain[i + 1].get_prev_hash()

            if not current_hash == next_hash:
                return False
        return True

    def proof_of_work(self):
        last_proof = self.__block_chain[len(self.__block_chain) - 1].get_data().get_proof_id()
        incrementor = last_proof + 1
        divisor = 11

        while not (incrementor % last_proof == 0 and incrementor % divisor == 0):
            incrementor += 1

        return incrementor

    # def begin_mine(self, tansaction_history:Transaction):
