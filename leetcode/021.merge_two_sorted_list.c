#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

// Definition for singly-linked list.
struct ListNode {
   int val;
   struct ListNode *next;
}Node, *pNode;

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *newList, *node;
    //newList = (struct ListNode*)malloc(sizeof(struct ListNode));
    //node = newList;
    if (l1==NULL)
        return l2;
    if (l2==NULL)
        return l1;
    if (l1->val <= l2->val) {
        newList = l1;
        node = l1;
        l1 = l1->next;
    } else {
        newList = l2;
        node = l2;
        l2 = l2->next;
    }
    while (l1!= NULL && l2!=NULL) {
        if (l1->val <= l2->val) {
            node->next = l1;
            node = l1;
            l1 = l1->next;
        } else {
            node->next = l2;
            node = l2;
            l2 = l2->next;
        }
    }
    if (l1 == NULL) {
        node->next = l2;
    } else if (l2 == NULL) {
        node->next = l1;
    }
    // node = newList->next;
    // free(newList);
    return newList;
}

void printLinkedList(struct ListNode* l) {
    while (l != NULL) {
        printf("%d -> ", l->val);
        l = l->next;
    }
    printf("NULL\n");
}

int main() {
    struct ListNode *l1=NULL, *l2=NULL, *node, *prev;
    int a1[] = {1, 2, 3, 6};
    int a2[] = {0, 4, 5, 8};
    int n1, n2, i, j;
    n1 = sizeof(a1)/sizeof(int);
    n2 = sizeof(a2)/sizeof(int);
    for (i=0;i<n1;i++) {
        node = (struct ListNode*)malloc(sizeof(Node));
        node->val = a1[i];
        node->next = NULL;
        if (l1==NULL) {
            l1 = node;
            prev = node;
        } else {
            prev->next = node;
            prev = node;
        }
    }
     for (i=0;i<n2;i++) {
        node = (struct ListNode*)malloc(sizeof(Node));
        node->val = a2[i];
        node->next = NULL;
        if (l2==NULL) {
            l2 = node;
            prev = node;
        } else {
            prev->next = node;
            prev = node;
        }
    }
    l1 = mergeTwoLists(l1, l2);
    printLinkedList(l1);
}
