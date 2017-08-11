from chain.block import Block

class Chain:
    def __init__(self):
        self.chain = list()
        self.chain.append(Block(0, '0000000000000000000000000000000000000000000000000000000000000000', 'first Block'))

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]
