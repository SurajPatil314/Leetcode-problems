{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.17134}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 # Definition for singly-linked list.\par
# class ListNode:\par
#     def __init__(self, x):\par
#         self.val = x\par
#         self.next = None\par
\par
class Solution:\par
    def deleteDuplicates(self, head: ListNode) -> ListNode:\par
        \par
        a=[]\par
        b=[]\par
        prev= None\par
        \par
        if not head:\par
            return None\par
        \par
        \par
        a.append(head.val)\par
        \par
        dummy1= head.next\par
        \par
        dummy2=head\par
        \par
        while(dummy1):            \par
            if dummy1.val in a:\par
                b.append(dummy1.val)\par
                dummy1 = dummy1.next\par
            else:\par
                a.append(dummy1.val)\par
                dummy1=dummy1.next\par
        for q in b:\par
            print("i::"+str(q))\par
        \par
        while(dummy2):\par
            if dummy2.val in b:\par
                if prev:\par
                    prev.next=dummy2.next\par
                else:\par
                    head=dummy2.next\par
                dummy2=dummy2.next\par
            else:\par
                prev=dummy2\par
                dummy2=dummy2.next\par
                \par
        \par
        return head\par
            \par
        \par
}
 