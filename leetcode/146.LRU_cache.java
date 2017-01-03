class LRUCache {
    protected java.util.HashMap<Integer, ListNode> _cache;
    protected int _size;
    protected int _capacity;
    protected ListNode _tail=null;
    protected ListNode _head=null;

    public static void main(String[] args) {
        String input = "10, [set(10,13),set(3,17),set(6,11),set(10,5),set(9,10),get(13),set(2,19),get(2),get(3),set(5,25),get(8),set(9,22),set(5,5),set(1,30),get(11),set(9,12),get(7),get(5),get(8),get(9),set(4,30),set(9,3),get(9),get(10),get(10),set(6,14),set(3,1),get(3),set(10,11),get(8),set(2,14),get(1),get(5),get(4),set(11,4),set(12,24),set(5,18),get(13),set(7,23),get(8),get(12),set(3,27),set(2,12),get(5),set(2,9),set(13,4),set(8,18),set(1,7),get(6),set(9,29),set(8,21),get(5),set(6,30),set(1,12),get(10),set(4,15),set(7,22),set(11,26),set(8,17),set(9,29),get(5),set(3,4),set(11,30),get(12),set(4,29),get(3),get(9),get(6),set(3,4),get(1),get(10),set(3,29),set(10,28),set(1,20),set(11,13),get(3),set(3,12),set(3,8),set(10,9),set(3,26),get(8),get(7),get(5),set(13,17),set(2,27),set(11,15),get(12),set(9,19),set(2,15),set(3,16),get(1),set(12,17),set(9,1),set(6,19),get(4),get(5),get(5),set(8,1),set(11,7),set(5,2),set(9,28),get(1),set(2,2),set(7,4),set(4,22),set(7,24),set(9,26),set(13,28),set(11,26)]";
        String[] a = input.split(",",  2);
        int capacity = Integer.parseInt(a[0]);
        java.util.List<TestCase> cases = LRUCache.parse(a[1]);
        LRUCache cache = new LRUCache(capacity);
        for (TestCase c : cases) {
            c.act(cache);
        }
    }

    static java.util.List<TestCase> parse(String input) {
        int key, value, action;
        java.util.ArrayList<TestCase> cases = new java.util.ArrayList<TestCase>();
        for (String s : input.split("\\)") ) {
            if (s.equals("]"))
                break;
            String s1 = s.split("\\(")[1];
            String[] s2 = s1.split(",");
            if (s2.length>1) {
                action = 0;
                key = Integer.parseInt(s2[0]);
                value = Integer.parseInt(s2[1]);
            } else {
                action = 1;
                key = Integer.parseInt(s2[0]);
                value = 0;
            }
            cases.add(new TestCase(key, value, action));
        }
        return cases;
    }

    private static class TestCase {
        int key;
        int value;
        int action;

        TestCase(int key, int value, int action) {
            this.key = key;
            this.value = value;
            this.action = action;
        }

        void act(LRUCache cache) {
            if (action == 0) {
                cache.set(key, value);
//                System.out.println("set("+key+","+value+")");
//                cache.printState();
            } else {
//                System.out.println("get("+key+"):"+cache.get(key));
//                cache.printState();
                System.out.print(cache.get(key) + ",");
            }
        }

    }

    public LRUCache(int capacity) {
        this._capacity = capacity;
        this._size = 0;
        this._cache = new java.util.HashMap<Integer, ListNode>(capacity+1);
    }

    public void printState() {
        ListNode cur = _head;
        System.out.print("head:("+_head.key+","+_head.value+")->");
        cur = cur.next;
        while(cur!=null) {
            System.out.print("("+cur.key+","+cur.value+","+cur.prev.key+")->");
            cur = cur.next;
        }
        System.out.println("tail:("+_tail.key+","+_tail.value+")");
    }

    public int get(int key) {
        if (!_cache.containsKey(key))
            return -1;
        return this.head(key).value;
    }

    public void set(int key, int value) {
        if (_cache.containsKey(key)) {
            // exist key: 1 change value 2 head key
            ListNode node = this.head(key);
            node.value = value;
            //this.head(key).value = value;
        } else {
            // not exist key
            if (_size < _capacity) {
                // still empty room, create new key node
                ListNode newNode = new ListNode(key, value, _head);
                if (_size == 0) {
                    _tail = newNode;
                } else {
                    _head.prev = newNode;
                }
                _head = newNode;
                _cache.put(key, newNode);
                _size += 1;
            } else {
                // full, replace tail node
                this.replace(key, value);
                // ListNode node = _cache.get(_tailKey);
                // _cache.remove(_tailKey);
                // _cache.put(key, node);
                // head(key);
                // node.value = value;
            }
        }
    }

    protected void replace(int key, int value) {
        _tail.value = value;
        _cache.remove(_tail.key);
        _tail.key = key;
        _cache.put(key, _tail);
        if (_capacity != 1) {
            _head.prev = _tail;
            _tail.next = _head;
            _head = _tail;
            _tail = _tail.prev;
            _tail.next = null;
        }
    }

    protected ListNode head(int key) {
        ListNode node = _cache.get(key);
        if (_head != node) {
            if (_tail == node) {
                // if key is tail, reset to its prev
                _tail = node.prev;
            }
            node.derail();
            _head.prev = node;
            node.next = _head;
            _head = node;
        }
        return node;
    }

    public class OneCache extends LRUCache {
        protected int _key;
        protected int _value;

        public OneCache() {
            super(0);
        }

        @Override
        public int get(int key) {
            if (_size !=9 && _key == key)
                return _value;
            return -1;
        }

        @Override
        public void set(int key, int value) {
            if (_size == 0) {
                _key = key;
                _value = value;
                _size = 1;
            } else if (_key == key) {
                _value = value;
            } else {
                _key = key;
                _value = value;
            }
        }

    }


    private class ListNode {
        int value;
        int key;
        ListNode prev = null;
        ListNode next = null;

        ListNode( int key, int value, ListNode next){
            this.key = key;
            this.value = value;
            this.next = next;
        }

        void derail() {
            ListNode tmp1 = this.prev;
            ListNode tmp2 = this.next;
            if (tmp1 != null) {
                tmp1.next = tmp2;
            }
            if (tmp2 != null)
                tmp2.prev = tmp1;
        }
    }
}
