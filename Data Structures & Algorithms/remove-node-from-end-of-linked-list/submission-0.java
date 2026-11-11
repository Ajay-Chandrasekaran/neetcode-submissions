/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = new ListNode(), start = head, result = null;
        temp.next = head;
        head = temp;

        for (int i=0; i<n; i++) {
            head = head.next;
        }

        while (head.next != null) {
            head = head.next;
            temp = temp.next;
        }

        if (temp.next == start) {
            result = temp.next.next;
        } else {
            result = start;
        }

        temp.next = temp.next.next;

        return result;
    }
}
