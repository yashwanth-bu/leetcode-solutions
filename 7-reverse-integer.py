class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        is_sign, updated_number = self.filter_the_requirments(x)

        result = int(updated_number)

        if is_sign:
            result = -result
        
        if result < -(2 ** 31) or result > (2 ** 31 - 1):
            return 0
        
        return result

    def filter_the_requirments(self, x):

        is_sign = False
        nums_list = []
        updated_number = ""

        for value in str(x):
            if "-" == value:
                is_sign = True
                continue
            nums_list.append(int(value))

        reversed_list = nums_list[::-1]

        for value in reversed_list:
            updated_number += str(value)
        
        updated_number = updated_number.lstrip("0")

        if updated_number == "":
            updated_number = "0"

        return is_sign, updated_number
            
        