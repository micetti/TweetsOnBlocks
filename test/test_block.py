from chain.block import Block

class TestBlock:

    def test_block_setup(self):
        previous_hash = '0000000000000000000000000000000000000000000000000000000000000000'
        block = Block(0, previous_hash, 'TestBlock')

        assert block.index == 0
        assert block.previous_hash == previous_hash
        assert block.data == 'TestBlock'
        assert len(block.hash) == 64


