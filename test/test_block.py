from chain.block import Block
import time

class TestBlock:

    def test_block_setup(self):
        previous_hash = '0000000000000000000000000000000000000000000000000000000000000000'
        block = Block(0, previous_hash, 'TestBlock')

        now_in_microseconds = int(time.time() * 1e6)
        assert block.index == 0
        assert block.previous_hash == previous_hash
        assert block.data == 'TestBlock'
        assert block.time_stamp < now_in_microseconds
        assert len(block.hash) == 64


