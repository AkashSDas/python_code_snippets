# ###### import time ######

# =================================
# Importing time module
import time
# =================================
# ### time method ###

# The time method returns the number of seconds passed since epoch.

print(time.time())
# This returns a Unix timestamp

# The Unix timestamp is a way to track time as a running total of seconds. This count starts at the Unix Epoch on January 1st, 1970 at UTC.
# It should also be pointed out that this point in time technically does not change no matter where you are located on the globe. This is very useful to computer systems for tracking and sorting dated information in dynamic and distributed applications both online and client side.
# =================================
# ### ctime method ###

# The ctime method takes seconds passed since epoch as an argument and returns a string representing local time.

# ----------------------------------
# seconds passed since epoch
seconds = 1545925769.9618232

local_time = time.ctime(seconds)
print("Local time:", local_time)
# ----------------------------------
# To get current local time

seconds = time.time()

local_time = time.ctime(seconds)
print(f"Local time: {local_time}")
# =================================
# ### sleep method ###

# The sleep method suspends(delays) execution of the current thread for the given number of seconds.

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")
# =================================
# ### time.struct_time Class ###

# Several methods in the time module such as gmtime(), asctime() etc. either take time.struct_time object as an argument or returns it as output.
# ---------------------------------
# Here's an example of how time.struct_time object looks like.

# time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, 
#                    tm_hour=6, tm_min=35, tm_sec=17, 
#                    tm_wday=3, tm_yday=361, tm_isdst=0)

# =================================
# Index	| Attribute	  | Values
# =================================
#  0    | tm_year	    | 0000, ...., 2018, ..., 9999
#  1    | tm_mon	    | 1, 2, ..., 12
#  2    | tm_mday	    | 1, 2, ..., 31
#  3    | tm_hour	    | 0, 1, ..., 23
#  4    | tm_min	    | 0, 1, ..., 59
#  5    | tm_sec	    | 0, 1, ..., 61
#  6    | tm_wday	    | 0, 1, ..., 6; Monday is 0
#  7    | tm_yday	    | 1, 2, ..., 366
#  8    | tm_isdst	  | 0, 1 or -1

# The values(elements) of the time.struct_time object are accessible using both indices and attributes.
# =================================
# ### gmtime method ###

# The gmtime method takes the number of seconds passed since epoch as an argument and returns struct_time object in UTC.

result = time.gmtime(1545925769)

print("result:", result)
print("year:", result.tm_year)
print("tm_hour:", result.tm_hour)
# ----------------------------------
# To get current time results

current = time.time()

result = time.gmtime(current)

print("result:", result)
print("year:", result.tm_year)
print("tm_hour:", result.tm_hour) 
# ----------------------------------
# If no argument or None is passed to gmtime(), the value returned by time() is used.

result = time.gmtime(None)

print("result:", result)
print("year:", result.tm_year)
print("tm_hour:", result.tm_hour)
# =================================
# ### asctime method ###

# The asctime method takes struct_time(or a tuple containing 9 elements corresponding to struct_time) as an argument and returns a string representing it.
# ----------------------------------
# Here's an example:

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)

print("Result:", result)
# =================================
# ### To get execution time of your programs ###

start_time = time.time()

now = time.gmtime()
now = time.asctime(now)
print(now)

end_time = time.time()

print(f"Execution time: {end_time - start_time}")
