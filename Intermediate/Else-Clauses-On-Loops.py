# ###### Else Clauses on Loops ######

# =================================
# else statment after a loop(for and while loops)
# One of the developer of python said else statment in such situation should be named as 'no break' statment
# In if-else statment it is either if or else, only one of them is executed
# But in this case both the loop and the else statment are executed 
# If we break out of the loop then the else statement won't be executed
# =================================
# 1.
num = 3
if num < 2:
    print('num is less than 2')
else:
    print("num is greater than 2")
# =================================    
# 2.
my_list = [1,2,3,4,5]
for i in my_list:
    print(i)
else:
    print("Hit the for/else loop")
# =================================    
# 3.
my_list = [1,2,3,4,5]
for i in my_list:
    print(i)
    if i == 3:
        break
else:
    print("Hit the for/else loop")
# =================================    
# 4.
my_list = [1,2,3,4,5]
for i in my_list:
    print(i)
    if i == 6:
        break
else:
    print("Hit the for/else loop")
# =================================
# 5. With while loop
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 8:
        break
else:
    print("Hit the while/else loop")
# =================================
# 6.
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 4:
        break
else:
    print("Hit the while/else loop")
# ===========================    
# 7. Practical Example

def find_index(to_search, target):
    for i,value in enumerate(my_list):
        if value == target:
            break
    else:
        return "Not there in the list"
    return 1
    
my_list = ['Randy','John','Brock']

index_location = find_index(my_list,'Randy')
print('Location of target is index : {}'.format(index_location))

index_location = find_index(my_list,'Rock')
print('Location of target is index : {}'.format(index_location))
