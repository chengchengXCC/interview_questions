import Queue
class Solution:
    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def getH(self, root):
        if root == None:
            return 0
        lH = self.getH(root.left)
        rH = self.getH(root.right)
        return max(lH, rH) + 1

    def serialize(self, root):
        # write your code here
        result = ""
        q = Queue.Queue()
        q.put(root)
        n = self.getH(root)
        for i in range(0, h):
            n = q.qsize()
            for j in range(0, n):
                node = q.get()
                if node == None:
                    result += "#"
                else:
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)
        return result


    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        root = None
        if data == None or len(data) == 0 or data[0] == '#':
            return root
        i = 0
        q = Queue.Queue()
        root = TreeNode(int(data[i]))
        q.put(root)
        i += 1
        while i < len(data):
            n = q.qsize()
            for j in range(0, n):
                node = q.get()
                val = data[i]
                if val == '#':
                    node.left = None
                else:
                    node.left = TreeNode(int(data[i]))
                    q.put(node.left)
                i += 1
                val = data[i]
                if val == '#':
                    node.right = None
                else:
                    node.right = TreeNode(int(data[i]))
                    q.put(node.right)
                i += 1
        return root






