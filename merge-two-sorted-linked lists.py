{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.17134}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 /**\par
 * Definition for singly-linked list.\par
 * public class ListNode \{\par
 *     int val;\par
 *     ListNode next;\par
 *     ListNode(int x) \{ val = x; \}\par
 * \}\par
 */\par
class Solution \{\par
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) \{\par
        ListNode c= null;\par
        \par
        if(l1==null && l2==null)\par
        \{\par
            return null;\par
        \}\par
        if(l1==null && l2!=null)\par
        \{\par
            return l2;\par
        \}\par
        if(l1!=null && l2==null)\par
        \{\par
            return l1;\par
        \}\par
        if(l1!=null && l2!=null)\par
        \{\par
            if(l1.val>l2.val)\par
            \{\par
                c= l2;\par
                c.next = mergeTwoLists(l1, l2.next);\par
            \}\par
            else\par
            \{\par
                c= l1;\par
                c.next = mergeTwoLists(l1.next, l2);\par
            \}\par
            \par
            return c;\par
        \}\par
        \par
        return c;\par
    \}\par
\}\par
}
 