class Dequeue(object):

    def __init__(self):
    # do some intialize if necessary
        self.first = None
        self.last = None

    # @param {int} item an integer
    # @return nothing
    def push_front(self, item):
        # Write yout code here
        node = Node(item)
        if self.first == None:
            self.first = node
            self.last = self.first
        else:
            nxt = self.first.next
            self.first.next = node
            node.prev = self.first
            node.next = nxt
            nxt.prev = node

    # @param {int} item an integer
    # @return nothing
    def push_back(self, item):
        # Write yout code here
        node = Node(item)
        if self.first == None:
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            node.prev = self.last

    # @return an integer
    def pop_front(self):
        # Write your code here
        result = self.first.val
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            new_first = self.first.next
            new_first.prev = None
            self.first = new_first
        return result


    # @return an integer
    def pop_back(self):
        # Write your code here
        result = self.last.val
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            new_last = self.last.prev
            new_last.next = None
            self.last = new_last
        return result
        
        
class Node():
    def __init__(self, _val):
        self.next = self.prev = None
        self.val = _val