# ###### import random ######

# =================================
# This shouldn't be used for security and crptogrophy 
# It can be used to create random Numbers and Data 
# =================================
# Importing random module
import random
# =================================
# ### random.random() ###

value = random.random() 
# random method will give value between 0 and 1 , 0 is inclusive and 1 is exculsive
print(value)
# =================================
# ### random.uniform() ###

value = random.uniform(1,10) 
# This gives random floating numbers between values specified in the argument
# The first argument is inclusive while the second is exclusive
print(value)
# =================================
# ### random.randint() ###

value = random.randint(1,10) 
# This give random integer numbers between values specified in the argument
# The first argument is inclusive while the second is exclusive
print(value)
# ---------------------------------
toss = random.randint(0,1) 
print(toss)
# =================================
# ### random.choice() ###

greeting = ['Hello','Hi','Hallo','Hola','Howdy']
value = random.choice(greeting)
print(value + " Honey!")
# =================================
# ### random.choices() ###

colors = ['red', 'black', 'pink']
# ---------------------------------
results = random.choices(colors, k=10) 
# k value is the size of the list that will be returned
print(results)
# ---------------------------------
results = random.choices(colors,weights=[5,5,1], k=10) 
# If a weights sequence is specified, selections are made according to the relative weights
# 5+5+1 = 11 so red has chances of 5 outof 11,pink has chances of 1 outof 11
print(results)
# =================================
# ### random.shuffle() ###

# shuffle method shuffle's the list
deck = list(range(1, 53))
# ---------------------------------   
new_deck = random.shuffle(deck)
print(new_deck)
# Above code return's None
# ---------------------------------
random.shuffle(deck)
print(deck)
# Above code return's a shuffeled list
# =================================
# ### random.sample() ###

# sample method gives only unique value
new_deck = random.sample(deck, k=2)
print(new_deck)

# To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead
