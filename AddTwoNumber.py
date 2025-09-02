from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0


        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            suma = v1 + v2 + carry
            carry = suma // 10
            suma = suma % 10

            curr.next = ListNode(suma)
            curr = curr.next

           
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next



def printList(node: Optional[ListNode]) -> None:
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))



if __name__ == "__main__":
    # Lista 1: 2 -> 4 -> 3
    l1 = ListNode(2, ListNode(4, ListNode(3)))

    # Lista 2: 5 -> 6 -> 4
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    res = Solution()
    result = res.addTwoNumbers(l1, l2)

    print("Resultado de la suma:")
    printList(result)  # 7 -> 0 -> 8
