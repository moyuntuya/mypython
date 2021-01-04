# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) #Creating result LinkedList
        curr = dummy #Current pointer
        c = 0 #Carryover

        while l1 or l2 or c:
            if l1:
                c += l1.val
                l1 = l1.next
                #print(c)

            if l2:
                c += l2.val
                l2 = l2.next
                #print(c)

            curr.next = ListNode(c % 10)
            print(linked_list_str(curr))
            #print(linked_list_str(curr.next))
            curr = curr.next
            c = c // 10

            print(c)

        return dummy.next

# Recursively print linked list
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)

# Make first linked list.
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
#print(linked_list_str(l1))

# Make second linked list.
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
#print(linked_list_str(l2))

sum = Solution()
l3 = sum.addTwoNumbers(l1, l2)
print(linked_list_str(l3))