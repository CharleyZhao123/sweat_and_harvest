# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = l1
        carry = 0
        while l2 != None:
            l1_num = l1.val
            l2_num = l2.val
            l1.val = (carry + l1_num + l2_num)%10
            carry = (carry + l1_num + l2_num)//10

            if carry != 0:
                if l2.next == None:
                    l2.next = ListNode(0, None)
                if l1.next == None:
                    l1.next = ListNode(0, None)
            else:
                if l2.next != None and l1.next == None:
                    l1.next = ListNode(0, None)
                if l1.next != None and l2.next == None:
                    l2.next = ListNode(0, None)
            
            l1 = l1.next
            l2 = l2.next
        
        return l3


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    l3 = s.addTwoNumbers(l1, l2)
    while l3 != None:
        print(l3.val)
        l3 = l3.next