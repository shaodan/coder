/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *node = head;
        ListNode *prev = NULL;
        while (node != NULL) {
            if (node->val==val) {
                if (prev == NULL) {
                    node = node->next;
                    delete head;
                    head = node;
                } else {
                    prev->next = node->next;
                    delete node;
                    node = prev->next;
                }
            } else {
                prev = node;
                node = node->next;
            }
        }
        return head;
    }
};
