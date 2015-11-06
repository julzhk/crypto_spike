import hashlib
from collections import defaultdict, OrderedDict


class Hash_Pointer(object):

    def __init__(self):
        self.data = OrderedDict()

    def add(self, data):
        hasher = hashlib.md5()
        hasher.update(u'%s' % data)
        key = hasher.hexdigest()
        self.data[key] = data

    def output(self):
        for k in self.data:
            print '%s : %s' % (k, self.data[k])


i = Hash_Pointer()
i.add('hello')
i.add('hello world')
i.add('hello world!')
i.output()
# 5d41402abc4b2a76b9719d911017c592 : hello
# 5eb63bbbe01eeed093cb22bb8f5acdc3 : hello world
# fc3ff98e8c6a0d3087d515c0473f8677 : hello world!