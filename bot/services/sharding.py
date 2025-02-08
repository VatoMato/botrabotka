# bot/services/sharding.py
from consistent_hash import ConsistentHash  # pip install consistent-hash

class ShardManager:
    def __init__(self, nodes):
        self.ring = ConsistentHash()
        for node in nodes:
            self.ring.add_node(node)

    def get_shard(self, key: int) -> str:
        return self.ring.get_node(str(key))

shard_manager = ShardManager([
    "postgres-shard-0",
    "postgres-shard-1",
    "postgres-shard-2",
    "postgres-shard-3"
])

def get_shard(user_id: int) -> str:
    return shard_manager.get_shard(user_id)