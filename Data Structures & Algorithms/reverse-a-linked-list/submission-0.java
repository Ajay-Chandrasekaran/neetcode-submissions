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
    public ListNode reverseList(ListNode head) {
        if (head == null) return head;
        ListNode tail = null, next = head.next;

        while (next != null) {
            head.next = tail;
            tail = head;
            head = next;
            next = head.next;
        }

        if (head != tail) {
            head.next = tail;
        }

        return head;
    }
}
