class Solution:
    def insert(self,l,v):
        if l==None:
            l.val=v
        else:
            r=l
            while r.next!=None:
                r=r.next
            tmp=ListNode(v)
            r.next=tmp
    def addTwoNumbers(self, l1, l2):
        res=ListNode(0)
        s,s2='',''
        while l1!=None:
            s+=str(l1.val)
            l1=l1.next
        while l2!=None:
            s2+=str(l2.val)
            l2=l2.next
        s=int(s[::-1])+int(s2[::-1])
        for x in str(s)[::-1]:
            self.insert(res,int(x))
        return res.next
