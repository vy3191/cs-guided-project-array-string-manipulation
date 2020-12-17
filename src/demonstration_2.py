"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here
    # have the last index in the array
    digit_index = len(digits) - 1
    # loop through the given list from end to start
    while digit_index >= 0:
        # increase the last digit by 1
        digits[digit_index] += 1
        # if the last digit is less than 10 no need to carry over just return the list
        if digits[digit_index] < 10:
            return digits
        else:
            digits[digit_index] = 0
            digit_index -= 1
    return [1] + digits        
            
    
print(plusOne([9]))
print(plusOne([1,2,3,4]))
print(plusOne([9,9,9,9]))
print(plusOne([0,9,1,2,9]))
