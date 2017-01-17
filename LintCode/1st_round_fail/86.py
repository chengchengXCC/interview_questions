#!/usr/bin/python

import requests
import pdb
import sys

class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.cur = root

    #@return: True if there has next node, or false
    def hasNext(self):
        return self.root and len(self.stack) > 0

    #@return: return next node
    def next(self):   
        while self.cur:
            stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        nxt = self.cur
        self.cur = self.cur.right
        return nxt        








