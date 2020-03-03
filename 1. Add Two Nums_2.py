# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        currcarry = 0
        prevcarry = 0
        final = ListNode(None)
        tmp = final
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                a = l1.val
                b = l2.val
                tmp.val = int((a+b+prevcarry)%10)
                currcarry = int((a+b+prevcarry)/10)
                if l1.next != None or l2.next != None:
                    tmp.next = ListNode(None)
                    tmp = tmp.next
                elif currcarry > 0:
                    tmp.next = ListNode(None)
                    tmp = tmp.next
                    tmp.val = currcarry
            elif l1 != None and l2 == None:
                a = l1.val
                b = 0
                tmp.val = int((a+b+prevcarry)%10)
                currcarry = int((a+b+prevcarry)/10)
                if l1.next != None:
                    tmp.next = ListNode(None)
                    tmp = tmp.next
                elif currcarry > 0:
                    tmp.next = ListNode(None)
                    tmp = tmp.next
                    tmp.val = currcarry
            elif l1 == None and l2 != None:
                a = 0
                b = l2.val
                tmp.val = int((a+b+prevcarry)%10)
                currcarry = int((a+b+prevcarry)/10)
                if l2.next != None:
                    tmp.next = ListNode(None)
                    tmp = tmp.next
                elif currcarry > 0:
                    tmp.next = ListNode(None)
                    tmp = tmp.next
                    tmp.val = currcarry
            else:
                break

            prevcarry = currcarry   
            try:
                l1 = l1.next
            except:
                pass
            try:
                l2 = l2.next
            except:
                pass

        return(final)