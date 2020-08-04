# ###### Multiprocessing Module ######

# ==============================
# Why will we use multiprocessing?
#   We will use threading whenever it will significantly speed up our program
#   Now this speed up comes from running different task running in parallel
# ==============================
# ### Basic Example of running some sleep methods concurrently ###
# ==============================
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# Since we are running the do_something function one time and since it is sleeping for 1 second therefore our script takes 1 second to complete
# ==============================
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# Here we are using the do_something function 2 times therefore our program is sleeping for 2 seconds

# So each time we are adding the do_something function it is adding 1 second to our script but it's not really doing anything on the CPU in that function, it's just sleeping
# So Our script is just waiting around and sleeping for a second and once that's done it goes on runs the next function and again we are waiting for another 1 second since it is sleeping and once that is done our script is done
# ==============================
# CPU bound tasks is when there is a lot of computation and it is using CPU
# IO bound tasks are things that are waiting for input and output operations to be completed and not really using CPU that much

# If we don't want our program to run synchronusly then we can split the task to other CPU's and run them in parallel
# ==============================
# Older way of doing multiprocessing

import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

# Making two process object instead of simply calling the function
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

# In order to make our process run we have to use the "start" method
p1.start()
p2.start()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# This will not do eaxactly what we think it should do

# Output:
    # Finished in 0.0 second(s)
    # Sleeping 1 second...
    # Sleeping 1 second...
    # Done Sleeping...
    # Done Sleeping...

# Our script actually took around 1 second to complete but it says that it took 0 second since it started both of our processes and while processes were sleeping our script ran concurrently and continued with the rest of the script and calculated our finish time and printed out our last print statement as processes were sleeping and when that 1 second was up processes continued on and both printed that they were done sleeping
# Our process didn't even started and it moved to the other codes of our script there we got our finish time and print statement being executed first and then our function got completed
# ==============================
# ### join method ###

# The join method will make sure that the processes are completed before moving ahead in the script

import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

t1 = multiprocessing.Process(target=do_something)
t2 = multiprocessing.Process(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# ==============================
# If we ran do_something function 10 times synchronusly then it will take 10 seconds but with usprocesses it will still take 1 second

import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    # We cannot do p.join() within the loop because it would join on the process before looping through, creating and starting the next process in the loop, which would same as running the code synchronusly
    # We need a way that we can start all of thprocesses in one loop and then loop through processes again and run the join method on them so that they all finish before the end of our script
    # For this we are going to append each process to a list
    processes.append(p)
    # Once this loop is completed we will be having a list of all thread that we started

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# Our computers have way of switiching between cores when one of them isn't too busy
# ==============================
# ### Passing in an argument ###

import multiprocessing
import time

# Unlprocesses, in order to pass arguments to a multiprocessing process the arguments must be able to serailized using pickel
# Basically serailizing means that we are converting python objects in to a format where that can be deconstructed and resconstructed in an another python script

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

processes = []

for _ in range(10):
    # The args parameter we pass the list of arguments that we want to pass into our function
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# ==============================
# The above are manual and older ways of making processes

# In ProcessPoolExecutor which is in lot of cases is going to be easy and efficient way of running these processes and it also allows us to easily switch over multiple thread instead of processes depending on the problem we are trying to solve

# For this we have to import concurrent.futures module
import concurrent.futures
import time

# When using ProcessPoolExecutor it's best to use them with a context manager

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executor:
    # If we want to execute the function once at a time then we can use the "submit" method
    # The "submit" method scedule a function to be executed and returns a future object
    # A future object basically encapsulate the execution of our function and it allows us check in on it after its being schedule. So we can check if it is running or done and check the results
    f1 = executor.submit(do_something, 1)
    # Second parameter is the number of seconds

    # To print the return value of the "submit" method we will use the "result" method
    print(f1.result())
    # If we add the result method then it will actually wait around until the function compeletes

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# ==============================
# If we want to run the function multiple times then we have to run submit method multiple times

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)

    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# ==============================
# If we want to run the submit method 10 times then we can use list

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]
    # Our list comprehension is running the do_something function 10 different times with an argument of 1 second

    # In order to get the results we can use another method from the concurrent.futures module called as_completed, Now this will give an iterator that we can loop over that will yield the results of our thread as they are completed
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# ==============================
# Now to proof that these are comming in as they are completed we will pass different range of seconds to our do_something function and it should print them in order they are completed

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# Output
    # Sleeping 5 second(s)...
    # Sleeping 4 second(s)...
    # Sleeping 3 second(s)...
    # Sleeping 2 second(s)...
    # Sleeping 1 second(s)...
    # Done Sleeping...2
    # Done Sleeping...3
    # Done Sleeping...1
    # Done Sleeping...4
    # Done Sleeping...5
    # Finished in 5.01 second(s)

# Now our 5 seconds function ran first but since we used the as_completed method it printed out our results in order they were completed
# With the submit method it is submitting each function at a time but in order to run submit on an entire list we need to do qa loop or comprehension like we did up there but we do the same work with the built-in "map" method, we can use the "map" method to run the function over a list of values
# Now that the map method of executor is similar to that Python's built-in map method instead it use thread insead of function
# So it runs the function with every item in the iterable that we pass in
# ==============================
# Using the map method

# Mapping our function to the list of seconds

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    results = executor.map(do_something, secs)
    # What map method is going to do is that it will run the do_something function with every value of the secs list

    # When we use the "submit" method it returns a future object but when we use the "map" method it returns the result
    # Now "map" method will run resutls concurrently only but instead of running the results as they completed like before "map" method is going to return the results in order they were started

    # Looping over the result
    for result in results:
        print(result)

        # While waiting for the first result of function didn't slowed us, our script will be completed almost at the same time

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# ==============================
# Handeling exceptions

# If our function raises an exception then it won't raise the exception while running the process, the exception will be raised while retriving the values from the results iterator
# ==============================
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    results = executor.map(do_something, secs)

    # Even if we don't grab all of our results in the context manager, it still automatically going to join all of those and let them finish once the context manager is ended
    # for result in results:
    #     print(result)

    # Since even if we commented the results loop it will still wait for our ProcessPoolExecutor to be completed


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# ==============================
# ### Practical Example ###

# ------------------------------
# Downloading Images

import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
# ------------------------------
# Performing CPU bound operations on those downloaded images
# Without using multiprocessing

import time
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)

for img_name in img_names:
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
# ==============================
# With using multiprocessing

import concurrent.futures
import time
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)

def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
# ==============================
# With using threading
import requests
import time
import concurrent.futures

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
# ==============================
# We can do experiments to find which way our script will run faster

# Benifit with using the concurrent.futures module it that we can switch over from threads to processes and vice-versa
