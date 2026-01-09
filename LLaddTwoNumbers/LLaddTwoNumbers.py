# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = 0
        num2 = 0
        i1 = 1
        i2 = 1
        while l1 != None:
            num1 += i1 * l1.val
            i1 *= 10
            l1 = l1.next
        while l2 != None:
            num2 += i2 * l2.val
            i2 *= 10
            l2 = l2.next
        # print(num1,num2)
        fnum = num1 + num2
        lfnum = len(str(fnum))
        # print(lfnum)
        # Return as a list
        # res = []
        # for i in range(lfnum):
        #     res.append(fnum%10)
        #     fnum = int(fnum/10)
        #     # print(res)
        # return res

        # Return as a linked list
        head = ListNode(0)
        current = head
        for i in range(lfnum):
            digit = fnum % 10
            fnum = fnum // 10
            current.next = ListNode(val=digit)
            current = current.next
        return head.next







