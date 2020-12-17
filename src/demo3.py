def plusOne(digits):
  digit_index = len(digits)-1
  while digit_index >= 0:
    # add one to the current digit
    digits[digit_index] += 1
    # check if this digit overflows (to 10)
    if digits[digit_index] < 10:
      return digits
    else:
      # this value is too large, set it to zero
      # continue the loop
      digits[digit_index] = 0
      digit_index -= 1
  # if we get here, that means we had all 9s and we still need to add 1
  return [1] + digits    

print(plusOne([9]))
print(plusOne([1,2,3,4]))
print(plusOne([9,9,9,9]))
print(plusOne([0,9,1,2,9]))

      