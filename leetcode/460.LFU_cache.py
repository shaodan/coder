# coding: utf-8

DEBUG = True

def dumpArgs(debug):
    def wrapper(func):
        '''Decorator to print function call details - parameters names and effective values'''
        # def __decorator(*func_args, **func_kwargs):
        #     arg_names = func.func_code.co_varnames[:func.func_code.co_argcount]
        #     args = func_args[1:len(arg_names)]
        #     defaults = func.func_defaults or ()
        #     args = args + defaults[len(defaults) - (func.func_code.co_argcount - len(args)):]
        #     params = zip(arg_names, args)
        #     args = func_args[len(arg_names):]
        #     if args:
        #         params.append(('args', args))
        #     if func_kwargs:
        #         params.append(('kwargs', func_kwargs))
        #     print func.func_name + ' (' + ', '.join('%s = %r' % p for p in params) + ' )'
        #     return func(self, *func_args, **func_kwargs)
        def __decorator(self, key, *func_args):
            v = func(self, key, *func_args)
            if func.func_name == 'get' or func.func_name == 'get_one':
                if v == -1:
                    print('get ('+str(key)+') ==> None'),
                else:
                    print('get ('+str(key)+') ==> '+str(v)),
            else:
                print('set ('+str(key)+') <== '+str(func_args[0])),
            self.show()
            return v
        if debug:
            return __decorator
        else:
            return func
    return wrapper


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0

        self.evict = None
        self.data = dict()
        self.freq = dict()
        if capacity == 0:
            self.get = lambda key: -1
            self.set = lambda key, value: None

    @dumpArgs(DEBUG)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.data:
            return -1
        node = self.data[key]
        self.promote(node)
        return node.value

    @dumpArgs(DEBUG)
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.data:
            if self.size < self.capacity:
                node = ListNode(key, value)
                # if self.size == 0:
                #     self.evict = node
                self.size += 1
                self.add_node(node)
            else:
                node = self.pop()
                node.value = value
                node.key = key
            self.data[key] = node
        else:
            node = self.data[key]
            node.value = value
            self.promote(node)

    def promote(self, node):
        freq = node.freq
        if not node.next:               # most
            if not node.prev:               # only one item
                if self.capacity == 1:
                    return
                else:
                    del self.freq[freq]
            elif node.prev.freq == freq:    # has same freq
                self.freq[freq] = node.prev
            else:                           # no same freq
                del self.freq[freq]
        elif node.next.freq > freq+1:   # keep order: freq node & next > freq+1
            if not node.prev:               # least node
                del self.freq[freq]
            elif node.prev.freq == freq:    # has same freq
                self.freq[freq] = node.prev
            else:
                del self.freq[freq]         # no same freq
        else:                           #  others
            if not node.prev:               # least node
                self.evict = node.next
                node.next.prev = None
                if node.next.freq != freq:      # no same freq
                    del self.freq[freq]
            else:
                if node.next.freq > freq:   # freq node & next=freq+1
                    if node.prev.freq == freq:  # has same freq
                        self.freq[freq] = node.prev
                    else:                       # no same freq
                        del self.freq[freq]
                else:                       # not freq node
                    pass
                node.prev.next = node.next
                node.next.prev = node.prev
            if freq+1 in self.freq:
                tmp = self.freq[freq+1]
            else:
                tmp = self.freq[freq]
            if tmp.next:
                tmp.next.prev = node
            node.next = tmp.next
            tmp.next = node
            node.prev = tmp
        node.freq += 1
        self.freq[freq+1] = node
        return

    def pop(self):
        node = self.evict
        del self.data[node.key]
        if not node.next:           # one-size cache
            return node
        if node.freq == 1:          # if exist other freq-1 node
            if node.next.freq == 1: # then change evict
                self.evict = node.next
                self.evict.prev = None
                tmp = self.freq[1]
                node.next = tmp.next
                if tmp.next:
                    tmp.next.prev = node
                node.prev = tmp
                tmp.next = node
            # node.freq[1] doesnt need del
        elif node.next.freq != node.freq:  # since the least node has no same freq prev
            del self.freq[node.freq]       # if next not same freq there is no same freq node
        self.freq[1] = node
        node.freq = 1
        return node

    def add_node(self, node):
        if not self.evict:
            self.evict = node
        elif self.evict.freq > 1:
            node.next = self.evict
            self.evict.prev = node
            self.evict = node
        else:
            tmp = self.freq[1]
            node.next = tmp.next
            if tmp.next:
                tmp.next.prev = node
            node.prev = tmp
            tmp.next = node
        self.freq[1] = node

    def show(self):
        d = sorted([(key, node.freq) for key,node in self.data.items()], key=lambda x: x[1])
        d = ['(%d,%d)'%(x1,x2) for (x1,x2) in d]
        print(''.join(d))
        node = self.evict
        nodes_right = [None] * self.size
        nodes_right[0] = node
        i = 0
        while node.next and i<self.size:
            i += 1
            node = node.next
            nodes_right[i] = node
        nodes_left = [None]*self.size
        nodes_left[i] = node
        while node.prev and i>0:
            i -= 1
            node = node.prev
            nodes_left[i] = node
        d_right = ['(%d, %d)->'%(n.key, n.freq) if n else 'n' for n in nodes_right]
        d_left = ['(%d, %d)<-'%(n.key, n.freq) if n else 'n' for n in nodes_left]
        print(''.join(d_right))
        print(''.join(d_left))


class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


if __name__ == '__main__':
    # case 1
    # func = ["LFUCache","set","set","get","set","get","get","set","get","get","get"]
    # kv = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
    # case 2
    func = ["LFUCache","set","set","get","set","set","get"]
    kv = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    # case 3
    # func = ["LFUCache","set","get"]
    # kv = [[0],[1,1],[1]]


    cache = LFUCache(kv[0][0])
    for fun, k in zip(func[1:], kv[1:]):
        if fun == "set":
            cache.set(k[0], k[1])
        else:
            cache.get(k[0])
