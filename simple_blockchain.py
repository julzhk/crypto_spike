import hashlib
from collections import OrderedDict

class BlockChain(object):
    def __init__(self, genesis='None'):
        self.data = OrderedDict()
        self.prev = self.make_hash(genesis)

    def make_hash(self, msg):
        hasher = hashlib.md5()
        hasher.update(u'%s' % msg)
        return hasher.hexdigest()

    def add(self, data):
        data = u'%s:%s' % (data, self.prev)
        key = self.make_hash(data)
        self.data[key] = data
        self.prev = key

    def output(self):
        for k in self.data:
            print '%s : %s' % (k, self.data[k])

    def verify(self):
        return all([k == self.make_hash(self.data[k]) for k in self.data])




bc = BlockChain(genesis='hi')
bc.add('hello')
bc.add('hello world')
bc.add('hello world!')
bc.output()

print bc.verify()

# 716e505b51b115aa7554596127627e50 : hello:49f68a5c8493ec2c0bf489821c21fc3b
# 2d890e63bcecb7e826ac7201aa9a055b : hello world:716e505b51b115aa7554596127627e50
# c6c09a0ecf532c2ee1f1a5dcd8455b0b : hello world!:2d890e63bcecb7e826ac7201aa9a055b
# True
