
"""Helper class for hashing objects"""
class Hash():
    def __init__(self, object_to_hash):
        """Pass object_to_hash"""
        self.object_to_hash = object_to_hash
    def hash_object(self):
        """Simple usage of a hash function in Python"""
        return hash(self.object_to_hash)
