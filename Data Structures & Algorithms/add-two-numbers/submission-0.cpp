/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int add = 0;
        while (l1 != NULL || l2 != NULL || add != 0) {
            int s1 = (l1 != NULL) ? l1->val : 0;
            int s2 = (l2 != NULL) ? l2->val : 0;
            int sum = s1+s2;

            if (sum + add > 9) {
                curr->next = new ListNode((sum + add) % 10);
                curr = curr->next;
                add = 1;
            } else {
                curr->next = new ListNode(sum + add);
                curr = curr->next;
                add = 0;
            }
            if (l1 != NULL) l1 = l1->next;
            if (l2 != NULL) l2 = l2->next;
        }
        return dummy->next;
    }
};
