# ###### Comprehensions ######

# =================================
# ### List Comprehensions ###

nums = [1,2,3,4,5,6,7,8,9,10]

# ---------------------------------
# If we want list of each element in the list nums i.e. if we want 'n' for each 'n' in nums

# Without using comprehension
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# With using comprehension
my_list = [n for n in nums]
print(my_list)
# ---------------------------------
# If we want list of square of each element in the list nums i.e. if we want 'n*n' for each 'n' in nums

# Without using comprehension
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

# With using comprehension
my_list = [n*n for n in nums]
print(my_list)
# ---------------------------------
# If we want list of even numbers in the list nums i.e. if we want 'n' for each 'n' in nums if 'n' is even

# Without using comprehension
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

# With using comprehension
my_list = [n for n in nums if n%2 == 0]
print(my_list)
# ---------------------------------
# If we want a (letter, num) pair for each letter in 'abcd' with each number in [1, 2, 3, 4]

# Without using comprehension
my_list = []
for letter in 'abcd':
    for num in [1,2,3,4]:
        my_list.append((letter,num))
print(my_list)

# With using comprehension
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)
# =================================
# ### Dictionary Comprehensions ###

hero = ['batman','ironman','spiderman','deadpool']
name = ['bruce','tony','peter','wade']

# ---------------------------------
# ## zip function ##

# this would return a zip object
print(zip(name,hero)) 

# casting the zip object to a list
print(list(zip(name,hero)))

# Using zip function in dictionary comprehensions
# ---------------------------------
# If we want a dictionary where each value of hero list will be a key and its value will be the corresponding element in the name list i.e. if we want dict{'name':'hero'} for each name,hero in zip(name,hero)

# Without using comprehension
my_dict = {}
for name,hero in zip(name,hero):
    my_dict[name] = hero
print(my_dict)

# With using comprehension
my_dict = {name:hero for name,hero in zip(name, hero) if name != 'peter'}
# Here we have added a condition that name should not be equal to 'peter'
print(my_dict)
# =================================
# ### Set Comprehensions ###

nums = {1,2,3,1,3,0,6,8,2,5,9,1}

# Without using comprehension
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# With using comprehension
my_set = {n for n in nums}
print(my_set)
# =================================
# ### Generator Expressions ###

nums = [1,2,3,4,5,6,7,8,9,10]

# If we want to yield square of each element in the nums list i.e. if we want to yield 'n*n' for each 'n' in nums

# Without using comprehension
def gen_func(nums):
    for n in nums:
        yield n*n
    
my_gen = gen_func(nums)
print(my_gen)
# it returns a generator object

# With using comprehension
my_gen = (n*n for n in nums)
print(my_gen) 
# it returns a generator object

# Looping through the generator and printing out each i
for i in my_gen:
    print(i)
