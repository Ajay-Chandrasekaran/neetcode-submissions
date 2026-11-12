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
    public void reorderList(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        Deque<ListNode> stack = new ArrayDeque<>();
        while (slow != null) {
            stack.push(slow);
            slow = slow.next;
            stack.peek().next = null;
        }

        while (stack.size() > 1) {
            ListNode temp = stack.pop();
            temp.next = head.next;
            head.next = temp;
            head = temp.next;
        }

        // head.next = null;
    }
}
