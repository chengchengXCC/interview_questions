import pdb

class LinkedNode:    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = None

class LFUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map_freq = {}
        self.hashTable = [LinkedNode(-1, -1) for i in range(1024)]
        self.hashTable_tail = []
        self.map_prev = {}
        for i in range(0, 1024):
            self.hashTable_tail.append(self.hashTable[i])

    def add(self, i, node, freq):
        self.map_prev[node.key] = self.hashTable_tail[i]
        self.map_freq[node.key] = freq
        self.hashTable_tail[i].next = node
        self.hashTable_tail[i] = node

    def removeLFU(self, hashTable):
        for i in range(1, 1024):
            if hashTable[i].next:
                node = hashTable[i].next
                if node.next:
                    self.map_prev[node.next.key] = hashTable[i]
                del self.map_prev[node.key]
                key = hashTable[i].next.key
                hashTable[i].next = hashTable[i].next.next
                if hashTable[i].next == None:
                    self.hashTable_tail[i] = hashTable[i]
                del self.map_freq[key]
                break

    def removeNode(self, key, freq):
        prev = self.map_prev[key]
        node = prev.next
        prev.next = prev.next.next
        if prev.next == None:
            self.hashTable_tail[freq] = prev
        del self.map_prev[key]
        if prev.next:
            self.map_prev[prev.next.key] = prev
        return node

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        node = LinkedNode(key, value)
        if key not in self.map_freq:
            if self.size < self.capacity:
                self.add(1, node, 1)
                self.size += 1
            else:
                self.removeLFU(self.hashTable)
                self.add(1, node, 1)
        else:
            freq = self.map_freq[key]
            node = self.removeNode(key, freq)
            node.value = value
            self.add(freq + 1, node, freq + 1)
        
    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.map_freq:
            return -1
        else:
            freq = self.map_freq[key]
            node = self.removeNode(key, freq)
            self.add(freq + 1, node, freq + 1)
            return node.value

if __name__ == '__main__':
    lfu = LFUCache(1)
    lfu.set(2,1)
    print lfu.get(2)
    #pdb.set_trace()
    lfu.set(3,2)
    print lfu.get(2)
    print lfu.get(3)
