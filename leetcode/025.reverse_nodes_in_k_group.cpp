#include <iostream>

using namespace std;


struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
  void print() ;
};

void ListNode::print() {
    cout << val <<' ' <<next.print();
}

ListNode* reversKGroup(ListNode* head, int k) {
	if (k<2)
        	return head;
        ListNode *first = head;
        ListNode *last  = NULL;
        ListNode *cur   = NULL;
        ListNode *next  = NULL;
        ListNode *pre   = NULL;
        int i;
        while (true) {
            next = first;
            for (i=k;i>0;i--) {
                cur = next;
                if (cur == NULL)
                    break;
                next = cur->next;
            }
            if (cur == NULL)
                break;
            if (first == head)
                head = cur;
            else
                last->next = cur;
            last = first;
            first = next;
            // reverse list
            pre = last;
            cur = pre->next;
            for (i=k-1;i>0;i--) {
                next = cur->next;
                cur->next = pre;
                pre = cur;
                cur = next;
            }
        }
        return head;
}
int main() {
  ListNode *head = 1;
  ListNode *cur = head;
  for (int i=2; i< 10; i++) {
    cur -> next = new ListNode(i, NULL);
  }
  head->print(); 
}
