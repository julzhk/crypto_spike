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
