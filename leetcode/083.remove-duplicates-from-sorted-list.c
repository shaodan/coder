/*
 * @lc app=leetcode id=83 lang=c
 *
 * [83] Remove Duplicates from Sorted List
 *
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
 *
 * algorithms
 * Easy (42.36%)
 * Total Accepted:    367.7K
 * Total Submissions: 846.1K
 * Testcase Example:  '[1,1,2]'
 *
 * Given a sorted linked list, delete all duplicates such that each element
 * appear only once.
 *
 * Example 1:
 *
 *
 * Input: 1->1->2
 * Output: 1->2
 *
 *
 * Example 2:
 *
 *
 * Input: 1->1->2->3->3
 * Output: 1->2->3
 *
 *
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* deleteDuplicates(struct ListNode* head){
    if (head == NULL) {
        return NULL;
    }
    int prev = head->val;
    struct ListNode* prevNode = head;
    struct ListNode* node = head->next;
    while (node) {
        if (node->val != prev) {
            prevNode->next = node;
            prevNode = node;
            prev = node->val;
        }
        node = node->next;
    }
    prevNode->next = NULL;
    return head;
}

