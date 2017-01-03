#include <stdio.h>
#include <malloc.h>

#define NewNode(n, x) n=(struct ListNode*)malloc(sizeof(struct ListNode));n->val=x;n->next=NULL;
/**
 * Definition for singly-linked list.
 */
 struct ListNode {
     int val;
     struct ListNode *next;
 };

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int bias = 0;
    struct ListNode *l3,*l4;
    int num;
    if (l1==NULL) {
        return l2;
    }
    l3 = l1;
    while(1) {
        if (l2==NULL) {
           if (bias) {
               num = l1->val+1;
               if (num>=10) {
                   bias=1;
                   l1->val=0;
               } else {
                   break;
               }
           } else {
               break;
           }
        } else {
            num = l1->val + l2->val + bias;
            if (num>=10) {
                l1->val = num-10;
                bias = 1;
            } else {
                l1->val = num;
                bias = 0;
            }
            l2 = l2->next;
        }
        if (l1->next==NULL) {
            if (l2==NULL) {
                if (bias) {
                   NewNode(l4, 1);
                   l1->next = l4;
                } 
                break;
            } else {
                l1->next = l2;
                l2=NULL;
            }
        }
        l1 = l1->next;
    }
    return l3;
}

struct ListNode* newNode(int x) {
  struct ListNode *node;
  node =(struct ListNode*)malloc(sizeof(struct ListNode));
  node->val = x;
  return node;
}

struct ListNode* arrayToList(int* a, int size) {
  struct ListNode *head, *n1, *n2;
  int i;
  if (!size)
    return NULL;
  //head = newNode(a[0]);
  NewNode(head, a[0]);
  n1 = head;
  for (i=1;i<size;i++) {
    //n2 = newNode(a[i]);
    NewNode(n2, a[i]);
    n1->next=n2;
    n1=n2;
  }
  return head;
}

void printList(struct ListNode* head) {
  while (head){
    printf("%d,", head->val);
    head = head->next;
  }
  printf("\n");
}

int main() {
  int a[] = {5};
  int b[] = {5}; 
  struct ListNode* l1 = arrayToList(a, sizeof(a)/sizeof(int));
  struct ListNode* l2 = arrayToList(b, sizeof(b)/sizeof(int));
  l1 = addTwoNumbers(l1, l2);
  printList(l1);
}

