# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        node_l1 = self.node_reader(l1)
        node_l2 = self.node_reader(l2)

        number_l1 = self.list_to_number(node_l1)
        number_l2 = self.list_to_number(node_l2)

        total_sum = number_l1 + number_l2

        result_value = self.number_to_list(total_sum)

        return self.convert_to_node(result_value)

    def node_reader(self, node):
        number_list = []

        while node:
            number_list.append(node.val)
            node = node.next

        return number_list

    def convert_to_node(self, given_list):
        if len(given_list) == 0:
            return ListNode(0)

        dummy = ListNode(0)
        current = dummy

        for value in given_list:
            current.next = ListNode(value)
            current = current.next

        return dummy.next

    def list_to_number(self, given_list):
        return_number = ""

        for value in given_list[::-1]:
            return_number += str(value)

        return int(return_number)

    def number_to_list(self, give_number):
        return_list = []

        for value in str(give_number):
            return_list.append(int(value))

        return return_list[::-1]