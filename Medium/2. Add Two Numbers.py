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
        l1_val = []
        l2_val = []
        curr = l1
        # Traverse l1 and store each digit as string in array
        while curr:
            l1_val.append(str(curr.val))
            curr = curr.next
        curr = l2
        # Traverse l2 and store each digit as string in array
        while curr:
            l2_val.append(str(curr.val))
            curr = curr.next
        # Reverses the string from both array to get correct number order
        l1_val = l1_val[::-1]
        l2_val = l2_val[::-1]
        # Converts the reversed strings into integers
        l1_num = int(''.join(l1_val))
        l2_num = int(''.join(l2_val))
        # Add the two numbers and reverse the result
        sum = str(l1_num + l2_num)[::-1]
        # Create a new linked list from the reversed sum string
        dummy = ListNode()
        curr = dummy
        for n in sum:
            curr.next = ListNode(int(n))
            curr = curr.next
        return dummy.next
       
# TC: O(N)
# SC: O(N)