class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tort = head
        hare = head
        while hare!=None and hare.next!= None:
            tort = tort.next
            hare = hare.next.next
            if tort == hare:
                return True
        return False
if __name__ == "__main__":
    linked_list = ListNode(5)
    linked_list.next = ListNode(6) # use ListNode constructor to create a new node in linked list
    linked_list.next.next = ListNode(7)
    linked_list.next.next.next = linked_list # point back to existing value
    sol = Solution()
    assert sol.hasCycle(linked_list)==False, "wrong output"

