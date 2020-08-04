# ###### Variable Scope ######

# =================================
""" LEGB --> (local,enclosing,global,buit-in) """

# ---------------------------------
x = 'global x'

def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()
print(x)
# ---------------------------------
# ### global keyword - It is used to create global variables from a non-global scope i.e inside a function ###

x = 'global x'

def outer():
    global x
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()
print(x)
# ---------------------------------
# ### nonlocal keyword - The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. ###

x = 'global x'

def outer():
    x = 'outer x'
    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()
print(x)
# =================================
# 1. global statement makes variable value global

# 2. nonlocal statement makes the variable nonlocal for enclosing function  

# 3. nonlocal statement can be usefull to change the state of closure and decorater

# 4. nonlocal overwrite the varible content
