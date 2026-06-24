import java.util.*;

class LFUCache {

    class Node {
        int val;
        Node prev;
        Node next;

        Node(int val) {
            this.val = val;
        }

        Node(int val, Node prev, Node next) {
            this.val = val;
            this.prev = prev;
            this.next = next;
        }
    }

    class LinkedList {
        Node left;
        Node right;
        HashMap<Integer, Node> map;

        LinkedList() {
            left = new Node(0);
            right = new Node(0);

            left.next = right;
            right.prev = left;

            map = new HashMap<>();
        }

        int length() {
            return map.size();
        }

        void pushRight(int value) {
            Node node = new Node(value, right.prev, right);

            right.prev.next = node;
            right.prev = node;

            map.put(value, node);
        }

        void pop(int value) {
            if (!map.containsKey(value)) return;

            Node node = map.get(value);

            node.prev.next = node.next;
            node.next.prev = node.prev;

            map.remove(value);
        }

        int popLeft() {
            int value = left.next.val;
            pop(value);
            return value;
        }

        void update(int value) {
            pop(value);
            pushRight(value);
        }
    }

    int cap;
    int lfuCnt;

    HashMap<Integer, Integer> valMap;
    HashMap<Integer, Integer> countMap;
    HashMap<Integer, LinkedList> listMap;

    public LFUCache(int capacity) {
        this.cap = capacity;
        this.lfuCnt = 0;

        valMap = new HashMap<>();
        countMap = new HashMap<>();
        listMap = new HashMap<>();
    }

    private LinkedList getList(int count) {
        listMap.putIfAbsent(count, new LinkedList());
        return listMap.get(count);
    }

    private void counter(int key) {
        int count = countMap.getOrDefault(key, 0);

        countMap.put(key, count + 1);

        getList(count).pop(key);
        getList(count + 1).pushRight(key);

        if (count == lfuCnt && getList(count).length() == 0) {
            lfuCnt++;
        }
    }

    public int get(int key) {
        if (!valMap.containsKey(key)) {
            return -1;
        }

        counter(key);
        return valMap.get(key);
    }

    public void put(int key, int value) {
        if (cap == 0) return;

        if (!valMap.containsKey(key) && valMap.size() == cap) {
            int removeKey = getList(lfuCnt).popLeft();

            valMap.remove(removeKey);
            countMap.remove(removeKey);
        }

        valMap.put(key, value);
        counter(key);

        lfuCnt = Math.min(lfuCnt, countMap.get(key));
    }
}