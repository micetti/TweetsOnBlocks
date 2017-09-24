import logging

from blockchain.block import Block

logger = logging.getLogger(__name__)

class Chain:
    def __init__(self):
        self.chain = list()
        self.chain.append(Block(0, '0000000000000000000000000000000000000000000000000000000000000000', 'first Block'))

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def get_previous_block(self):
        return self.chain[len(self.chain) - 2]

    def add_new_block(self, data):
        new_index = len(self.chain)
        previous_hash = self.get_latest_block().hash
        new_block = Block(new_index, previous_hash, data)
        self.chain.append(new_block)

    def all_blocks_valid(self):
        for index in range(len(self.chain)):
            if index == 0:
                if not self.first_block_is_valid():
                    logger.error('Invalid first block of blockchain')
                    return False
            else:
                if not self.indices_are_correct(index):
                    logger.error('Invalid indices in blockchain at index {}'.format(index))
                    return False
                if not self.is_valid_block(index):
                    logger.error('Invalid block found in blockchain at index {}'.format(index))
                    return False
        return True

    def first_block_is_valid(self):
        first_block = self.chain[0]
        if not (first_block.index == 0 and first_block.data == 'first Block'):
            logger.debug("First block had index {}. Data was {}".format(first_block.index, first_block.data))
            return False
        if not first_block.previous_hash == '0000000000000000000000000000000000000000000000000000000000000000':
            logger.debug("First block had previous hash {}".format(first_block.previous_hash))
            return False
        if not first_block.generate_hash() == first_block.hash:
            logger.debug("First blocks hash was invalid")
            return False
        return True

    def indices_are_correct(self, index):
        if not self.chain[index].index - 1 == self.chain[index - 1].index:
            logger.error("Index incorrect. At index {} compared to previous index".format(index))
            return False
        return True

    def is_valid_block(self, index):
        if not self.chain[index].previous_hash == self.chain[index - 1].hash:
            logger.debug("Previous_hash of block with index {} did not match hash of previous block".format(index))
            return False
        if not self.chain[index].generate_hash() == self.chain[index].hash:
            logger.debug("The generated hash of block with index {} did not match the assigned hash".format(index))
            return False
        return True
