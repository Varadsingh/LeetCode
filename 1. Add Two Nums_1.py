# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp1 = l1
        tmp2 = l2
        len1 = 0
        len2 = 0
        
        while tmp1 != None:
            len1 = len1 + 1
            tmp1 = tmp1.next
        while tmp2 != None:
            len2 = len2 + 1
            tmp2 = tmp2.next

        maxlen = max(len1,len2)
        
        tmp1 = l1
        tmp2 = l2
        currcarry = 0
        prevcarry = 0
        final = ListNode(None)
        tmp = final
        while maxlen > 0:
            if tmp1 != None or tmp2 != None:
                if tmp1 != None:
                    a = tmp1.val
                else:
                    a = 0
                if tmp2 != None:
                    b = tmp2.val
                else:
                    b = 0
                    
                main = int((a+b+prevcarry)%10)
                currcarry = int((a+b+prevcarry)/10)
                
                tmp.val = main
                
                if maxlen != 1:
                    tmp.next = ListNode(None)
                    tmp = tmp.next
                    
                if maxlen == 1 and currcarry > 0:
                    tmp.next = ListNode(None)
                    tmp = tmp.next
                    tmp.val = currcarry
                    
                if currcarry > 0:
                    prevcarry = currcarry
                else:
                    prevcarry = 0
                
            maxlen = maxlen - 1
            try:
                tmp1 = tmp1.next
            except:
                pass
            try:
                tmp2 = tmp2.next
            except:
                pass
            
        return(final)