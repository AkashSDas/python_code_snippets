# ###### Generators ######

# =================================
# When you enter a large amount of data and ask for result:
# 1. In case of list it will take more memory and more time
# 2. In case of generator it will take almost same memory as before excution and less time, since in case of generators it doesn't store all results, it just give one result at a time therefore it takes almost same memory as before the execution
# 3. By converting a generator into a list you lose all of these advantages
# You will notice effects by entering millions of data
# =================================
# square_numbers function returning a list

# ---------------------------------
# Without using generators
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)
# ---------------------------------
# With using generators

# At a glance, the yield statement is used to define generators, replacing the return statement in a function to provide a result to its caller without destroying local variables. Unlike a function, where on each call it starts with new set of variables, a generator will resume the execution where it was left off

def square_numbers(nums):
    for i in nums:
        yield(i*i)
        
my_nums = square_numbers([1,2,3,4,5]) 
# For this we will not get a list. Reason(generators don't hold entire result in memory it yield's one result at a time)

# This will show the generator object
print(my_nums)

# Use the next method to get the next result
print(next(my_nums))  
print(next(my_nums))
print(next(my_nums))
print(next(my_nums)) 
# Once you got out of values and then if you use the next method then you will get StopIteration error

# We can use for loop in generator because StopIteration Error will be taken care off by for loop
for num in my_nums:
    print(num)  
# =================================
# ### Using list comprehensions ###

my_nums = [x*x for x in [1,2,3,4,5]] 
# Due to square brackets it gives list. We created a list
print(my_nums)

# Creating a generator by using the parenthese() instead of using square-brackets[]
my_nums = (x*x for x in [1,2,3,4,5]) 
print(my_nums)

# By casting of my_nums into list you will lose the performance advantages that you get by using generators
print(list(my_nums)) 
# =================================
# ### Performance difference ###

# ---------------------------------
# This will make a list
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors),
        }
        result.append(person)
    return result
# ---------------------------------    
# This will make a generator
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors),
        }
    yield person
