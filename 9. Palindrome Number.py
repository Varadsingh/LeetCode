#9. Palindrome Number

# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = 0
        x1 = x
        if x >= 0:
            while x/10 > 0:
                rem = x%10
                x = x//10
                c = c*10 + rem
            if x1 - c == 0:
                return(True)
        return(False)   