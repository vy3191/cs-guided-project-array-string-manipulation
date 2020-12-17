# In-Place

# An in-place function modifies or destroys the state of the input data when it is run. For instance, if you write a function that squares every integer in an input list, an in-place version of this function would change the data in the list that was passed in. It would not create a new list and return the new list. In-place functions are more space-efficient because they don't create new variables directly tied to the input size. However, to get that space-efficiency, you have to risk that the function's user may end up changing state to the input accidentally.

# Imagine a scenario where you have an antique map that you are using to navigate on a hike. You end up needing directions, and when you come across another hiker, you ask them for help. The person helping you has two options. They can take your antique map, use a pen, and mark it up with their notations that will help you navigate. However, you most likely didn't want those annotations to be on your map forever. The other option would be to find another piece of paper and have the person helping you write out their annotations on that. This way, your original antique map doesn't have to be modified. However, now you have two maps that you have to carry around on your hike.

# example:1

def append_exclamation(str_list):
  for idx, item in enumerate(str_list):
    str_list[idx] += "!"

my_list = ["venky", "yagatilee", "venkatesh", "venkat"]
print(f"Before running the function>>>>{my_list}") 
append_exclamation(my_list)   
print(f"After running the function>>>>{my_list}") 