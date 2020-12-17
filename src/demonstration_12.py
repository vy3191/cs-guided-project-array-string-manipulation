
def pivot_index(nums):
    total_sum = sum(nums)   
    left_sum = 0
    # loop through the array and keep updating the left sum
    for i in range(len(nums)):
      right_sum = total_sum - left_sum - nums[i]
      if left_sum == right_sum:
        return i
      print(left_sum, right_sum)
      left_sum += nums[i]
    return -1  

print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
        
    

