# ###### Slicing Lists And Strings ######

# =================================
# ### Slicing Lists ###

my_list = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
#          0  1  2  3  4  5  6  7  8  9  Positive index
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  Negative index
# ---------------------------------
# list[start:end:steps]

print(my_list[3:6])
print(my_list[1:])
print(my_list[2:-2])
print(my_list[0::2])
print(my_list[-1:-10:-1])
print(my_list[7:3]) # this will print a empty list since start should be less than end

print(my_list[::-1]) # this will reverse the list and print it
# =================================
# ### Slicing Strings ###

# String slicing is same as list slicing

sample_url = 'http://tonystark.com'
print(sample_url)

# reverse the url
print(sample_url[::-1])

# print url without http
print(sample_url[4:])
# =================================
# ### .reversed() method ###

# For Strings:
string = "London"

print(reversed(string)) # this will return a reversed object

# Casting that reversed object to a list
print(list(reversed(string))) 
# Now we have a list of characters from the string in reverse order

# By using .join() method on the list we will get the string in reverse order
print("".join(list(reversed(string)))) 
# =================================
# ### .reverse() method ###

nums = [1, 2, 3, 4, 5]

# To reverse the nums list just apply the reverse method
nums.reverse()
print(nums)

print(nums.reverse()) # this returns None
print(nums) # nums list goes back to original order since we again applied the reverse method on it in the above steps
