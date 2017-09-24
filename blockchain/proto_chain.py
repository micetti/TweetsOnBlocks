from blockchain import blockchain_pb2

from blockchain.block import Block

PROTOBUF_FILE = "./blockchain_local"

class ProtoChain:

    def __init__(self):
        self.chain = blockchain_pb2.BlockChain()
        try:
            f = open(PROTOBUF_FILE, "rb")
            self.chain.ParseFromString(f.read())
            f.close()
        except IOError:
            print("No existing protobuf file found. Creating new one")
            first_block = self.chain.blocks.add()
            Block(0, '0000000000000000000000000000000000000000000000000000000000000000', 'first Block').add_to_proto(first_block)

    def get_latest_block(self):
        return self.chain.blocks[len(self.chain.blocks) - 1]

    def get_previous_block(self):
        return self.chain.blocks[len(self.chain.blocks) - 2]

    def add_new_block(self, data):
        new_index = len(self.chain.blocks)
        previous_hash = self.get_latest_block().hash
        Block(new_index, previous_hash, data).add_to_proto(self.chain.blocks.add())
        try:
            f = open(PROTOBUF_FILE, "wb")
            f.write(self.chain.SerializeToString())
            f.close()
        except IOError:
            print("No existing protobuf file found. Creating new one")

proto_chain = ProtoChain()
proto_chain.add_new_block("Hello")
