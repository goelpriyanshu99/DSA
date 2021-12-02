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
    ListNode* oddEvenList(ListNode* head) {
        if(head == nullptr || head->next == nullptr || head->next->next == nullptr)
            return head;
        
        ListNode* firstEven = head->next;
        ListNode* first = head;
        ListNode* sec = head->next;

        while(first != nullptr && sec != nullptr) {
            first->next = sec->next;
            if(sec->next != nullptr) {
                sec->next = sec->next->next;
            } 
            else {
                sec->next = nullptr;
            }
            
            if(first->next != nullptr) first = first->next;
            
            sec = sec->next;
        }
        // if(first == nullptr)
        first->next = firstEven;
        return head;
    }
};
