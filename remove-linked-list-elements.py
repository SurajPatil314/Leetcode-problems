{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.17134}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 # Definition for singly-linked list.\par
# class ListNode:\par
#     def __init__(self, x):\par
#         self.val = x
#         self.next = None

class Solution:\par
    def removeElements(self, head: ListNode, val: int) -> ListNode:
       
        dummy= head;
        prev=None
     
        if not head:
            return None
        
      
        
        while (dummy):
            if dummy.val==val:
                if not prev:
                    head= dummy.next
                else:
                    prev.next= dummy.next
                dummy=dummy.next
            else:
                prev=dummy
                dummy=dummy.next
                
        return head
                
                
                
                
        
       
        
        

        
}
 