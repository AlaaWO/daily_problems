class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        dummy = str(x)
        y =""
        for _ in range(len(dummy)):
            y += dummy[-1]
            dummy = dummy[:-1]
        
        x= str(x)
        if y == x:
            return True
        else:
            return False

        