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
        ListNode temp = new ListNode(), start = temp;
        temp.next = head;
        head = temp;

        for (int i=0; i<n; i++) {
            head = head.next;
        }

        while (head.next != null) {
            head = head.next;
            temp = temp.next;
        }

        temp.next = temp.next.next;

        return start.next;
    }
}
