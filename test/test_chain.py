from blockchain.chain import Chain
from blockchain.block import Block

class TestChain:
    def test_chain_constructor(self):
        test_chain = Chain()

        assert len(test_chain.chain) == 1
        assert type(test_chain.get_latest_block()) == Block
        assert test_chain.get_latest_block().data == 'first Block'
        assert test_chain.get_latest_block().index == 0

    def test_add_new_block(self):
        test_chain = Chain()
        data = 'New Block'

        test_chain.add_new_block(data)

        assert len(test_chain.chain) == 2
        assert type(test_chain.get_latest_block()) == Block
        assert test_chain.get_previous_block().data == 'first Block'
        assert test_chain.get_latest_block().data == 'New Block'
        assert test_chain.get_previous_block().index == 0
        assert test_chain.get_latest_block().index == 1

    def test_all_blocks_are_valid(self):
        test_chain = Chain()
        test_chain.add_new_block('Block one')
        test_chain.add_new_block('Block two')

        valid = test_chain.all_blocks_valid()

        assert valid is True

    def test_changed_index_or_deleted_block_detected(self):
        test_chain = Chain()
        test_chain.add_new_block('Block one')
        test_chain.add_new_block('Block two')
        del test_chain.chain[1]

        valid = test_chain.all_blocks_valid()

        assert valid is False

    def test_changed_previous_hash_detected(self):
        test_chain = Chain()
        test_chain.add_new_block('Block one')
        test_chain.add_new_block('Block two')
        test_chain.chain[1].previous_hash = '76af6354wronghash'

        valid = test_chain.all_blocks_valid()

        assert valid is False

    def test_changed_hash_detected(self):
        test_chain = Chain()
        test_chain.add_new_block('Block one')
        test_chain.add_new_block('Block two')
        test_chain.chain[1].hash = '76af6354wronghash'

        valid = test_chain.all_blocks_valid()

        assert valid is False

    def test_changed_time_stamp_detected(self):
        test_chain = Chain()
        test_chain.add_new_block('Block one')
        test_chain.add_new_block('Block two')
        test_chain.chain[1].time_stamp = '2017-08-14T06:16:23.225877'

        valid = test_chain.all_blocks_valid()

        assert valid is False

    def test_changed_data_detected(self):
        test_chain = Chain()
        test_chain.add_new_block('Block one')
        test_chain.add_new_block('Block two')
        test_chain.chain[1].data = 'Block 42'

        valid = test_chain.all_blocks_valid()

        assert valid is False
