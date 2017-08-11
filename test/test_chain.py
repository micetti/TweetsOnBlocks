from chain.chain import Chain
from chain.block import Block

class TestChain:
    def test_chain_constructor(self):
        test_chain = Chain()

        assert len(test_chain.chain) == 1
        assert type(test_chain.get_latest_block()) == Block
        assert test_chain.get_latest_block().data == 'first Block'
        assert test_chain.get_latest_block().index == 0
