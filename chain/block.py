import datetime
import hashlib

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.time_stamp = datetime.datetime.utcnow().isoformat()
        self.hash = self.generate_hash()

    def generate_hash(self):
        hash = hashlib.sha256()
        hash.update(str(self.index).encode())
        hash.update(self.previous_hash.encode())
        hash.update(self.data.encode())
        hash.update(self.time_stamp.encode())
        return hash.hexdigest()
