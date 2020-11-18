# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。 
# 
#  示例： 
# 
#  给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#  
# 
#  说明： 
# 
#  给定的 n 保证是有效的。 
# 
#  进阶： 
# 
#  你能尝试使用一趟扫描实现吗？ 
#  Related Topics 链表 双指针 
#  👍 1115 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n < 0:
            return head

        dump = ListNode(0)
        dump.next = head
        pre_node = dump
        for i in range(n):
            if not head:
                return None
            head = head.next
        while head:
            pre_node = pre_node.next
            head = head.next
        pre_node.next = pre_node.next.next
        return dump.next


# leetcode submit region end(Prohibit modification and deletion)
'''
核心是找到删除的节点前一个节点的位置，可以引用一个pre指针变量，使pre指针变量和head指针变量之间相差N个节点，然后同时移动head和pre指针变量，当head为null时，将pre的next指向待删除节点的next

1. 首选移动head节点，使得pre节点和head节点之间相差N个节点
2. 链表上同时移动head和pre直到head为null
3. 修改pre所在节点的next指向删除节点的next节点
'''
