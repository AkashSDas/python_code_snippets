# ###### Hashing Passwords ######

# ==============================
# ### Generating a Salt ###

import os

# To generate a salt, use the os.urandom function as it returns random bytes suitable for cryptographic use.
# This function does not use pseudo-random number generators so the return value is unpredictable, exactly what is required.

salt = os.urandom(32)
print(salt)

# 32 is the size returned in bytes. We can chose any size but it is recommended to make it over 16 bytes
# ==============================
# ### Hashing ###

import os
import hashlib

salt = os.urandom(32)
password = 'password123'

key = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    100000 # It is recommended to use atleast 100,000 iteration of SHA-256
    )

print(key)

# Since no key length was provided, the digest size of the hash algorithm is used in this case, we use SHA-256 so the size will be 64 bytes.
# If we require a longer key for something like using this key in AES then we have to pass the desired key size to dklen after the iteration in hashlib.pbkdf2_hmac
# ==============================
# ### Providing a key length ###

import os
import hashlib

salt = os.urandom(32)
password = 'password123'

key = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    100000, # It is recommended to use atleast 100,000 iteration of SHA-256
    dklen=128 # Get a 128 byte key
    )

print(key)
# ==============================
# ### Storing the Hash and Salt ###

# We need to store the salt and key.
# In terms of storage, we can use any method; JSON, SQL, CSV or even a raw text file.
# Make sure that we do not store the password as that is the goal of all of this, not having to store the actual password.

# If we are restricted to only one field for storage then we can add the salt and password together and then store them.
# When reading them out, we can then separate them as we know the length of the salt and key.

import os
import hashlib

# Generation of salt and key
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', 'mypassword'.encode('utf-8'), salt, 100000)

# Storing
storage = salt + key

# Getting the values back out
salt_from_storage = storage[:32]
key_from_storage = storage[32:]

print(storage)
print(salt_from_storage)
print(key_from_storage)

# If it is possible to use two fields in our situation (most situations we can), then use two fields as it makes things less complicated
# ==============================
# ### Verification ###

# After the user has supplied their password for the first time and we generated a salt for them, computed the key using the password and salt and then stored this password and salt, we can now check if further passwords are correct.
# ------------------------------
salt = b'\x9b[\xf9\x85xq~`s<\xea\x1b\xc9\xaa\x13\xf2F\xfa\x0b=\x89\xe9\xd5W\xda~s\xa6\xbf\x02t-'
key = b'\xfb(\x9b\x95G\x93\xa7\xb1\x9am\x84\xae\x84$\xae\x81\x10\x1f\x85Q)lU\xbb\x94\xac\xd4\x11\xca\xe3d\x07'

password_to_check = 'mypassword'

new_key = hashlib.pbkdf2_hmac('sha256', password_to_check.encode('utf-8'), salt, 100000)

if new_key == key:
    print("Correct Password")
else:
    print("Incorrect Password")
# ------------------------------
salt = b''
key = b''

password_to_check = 'mypassword'

new_key = hashlib.pbkdf2_hmac('sha256', password_to_check.encode('utf-8'), salt, 100000)

if new_key == key:
    print("Correct Password")
else:
    print("Incorrect Password")
