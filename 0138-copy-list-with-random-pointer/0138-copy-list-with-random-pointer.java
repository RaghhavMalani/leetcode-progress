/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        HashMap <Node, Node> oldcopy = new HashMap<>();
        oldcopy.put(null,null);

        Node curr =  head;
        while (curr != null){
            oldcopy.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        curr = head;
        while(curr != null){
            Node copy = oldcopy.get(curr);
            copy.next = oldcopy.get(curr.next);
            copy.random = oldcopy.get(curr.random);
            curr = curr.next;
        }

        return oldcopy.get(head);
    }
}