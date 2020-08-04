# ###### Subprocess ######

# =================================
# Calling external commands using the subprocess module
# =================================
# Importing subprocess module
import subprocess
# =================================
# We can using the same mehtods of subprocess module to run Linux, Mac and Windows commands
# =================================
# ### run ###

# Running a normal 'ls' command
subprocess.run('ls')
# The ls command prints everything the in the current working directory

# If we are using Windows then running just this --> subprocess.run('dir') --> will give an error, Since dir command is built into the shell
# So in order to make it run we have to pass extra argument of --> shell=True --> i.e. --> subprocess.run('ls', shell=True)

subprocess.run('ls', shell=True)

# By setting the shell argument to True we can pass in an entire command as string
# We can add more agruments to our external commands like below and we would still get our result
subprocess.run('ls -alh', shell=True)
# =================================
# If we are using the shell=True then that can be a security hazard if we are using an untrusted input, So use shell=True only when we pass the commands by ourself and be sure that we are not using it with the user input or anything
# =================================
# But if we are not using the shell arugument the we cannot pass in the entire command as a string
# Instead we need to pass in everything as a list of arguments

subprocess.run(['ls', '-alh'])
# Running the entire command without passing the shell argument
# =================================
# ### Capturing the STDOUT ###

# ---------------------------------
var = subprocess.run(['ls', '-alh'])
# Our output will still appear on the console

# Our var variable is set to a CompletedProcess object
print(var)

# We can do a lot of things with the CompletedProcess object

# To check what arguments were passed in to the original command
print(var.args)

# To check the returncode where the returncode shows us if we got some errors or not
print(var.returncode)
# returncode  of 0 means that our command ran successfully, 0 errors

# To get the stdout
print(var.stdout)
# Here we will get None as stdout, the reason it is sending None is that our output is sent to the console
# ---------------------------------
# To capture the stdout we have to pass in a argument of capture_output and set it to True

var = subprocess.run(['ls', '-alh'], capture_output=True)
# Now we won't get anything in the console by just running the above line
# Now we are capturing the output in the var variable
print(var)

print(var.stdout)
# Our stdout was capture as bytes, if we want our new lines to actually be spaced out then we will have to convert this to string we can use the decode method
print(var.stdout.decode())

# If we don't want to use the decode method then we can use the text argument and set it to True
var = subprocess.run(['ls', '-alh'], capture_output=True, text=True)

print(var.stdout)
# Now we no longer need to use the decode method
# ---------------------------------
# So when we set the capture_output=True what it is actually doing in the background is setting the STDOUT and STDERROR to the subprocess pipe and that allows us to capture those values

# Setting up the STDOUT argument directly, for that instead of setting capture_output to True we set stdout to subprocess.PIPE
var = subprocess.run(['ls', '-alh'], stdout=subprocess.PIPE, text=True)

# stdout=subprocess.PIPE this is what is setting the capture_output=True in the background but it also redirect the STDERROR to that PIPE as well
print(var.stdout)
# ---------------------------------
# We can also redirect stdout to otherplaces as well

# Let's say we want to redirect stdout to a file that can be used to loggin or anything like that
with open("output.txt", "w") as f:
    var = subprocess.run(['ls', '-alh'], stdout=f, text=True)
    # Settign the stdout to the file object (f) will redirect the output to that file

# Let's see if our command isn't successful

# Trying to list content of directory that doesn't exist
var = subprocess.run(['ls', '-alh', 'does-not-exist'], capture_output=True, text=True)
# We don't get any error since we capture that output
# Python doesn't throw an error if external command fails instead is returns a non zero returncode
print(var.returncode)
# =================================
# ### Capturing the STDERR ###

# To check stderr
print(var.stderr)

# If we want Python to throw an error if external command fails then we have to pass in an additional argument of check=True
# var = subprocess.run(['ls', '-alh', 'does-not-exist'], capture_output=True, text=True, check=True)

# Another common thing to do with errors is redirecting them to devnull and this means that we are ignoring that
var = subprocess.run(['ls', '-alh', 'does-not-exist'], stderr=subprocess.DEVNULL, text=True)

# We can also change the input that different commands receive

# Lets say we want output of one command to be input of other command
p1 = subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)

print(p1.stdout)

# To make output of p1 as input of p2 we have to pass in an argument of input and set it to p1.stdout
p2 = subprocess.run(['grep', '-n', 'output'], capture_output=True, text=True, input=p1.stdout)

print(p2.stdout)
