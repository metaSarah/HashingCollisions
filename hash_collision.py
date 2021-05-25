import hashlib
import os

import random
import string

""" hash_collision(k) returns x and y,
such that the SHA256(x) and SHA256(y) match on their final k bits. 

The return variables, x and y, should be encoded as bytes.

os.urandom() randomly generates bits and outputs a python bytes object. 
Each byte generated won't necessarily correspond to an ASCII character, 
but each one can be converted to a numerical value, since each byte 
is a string of bits, and any string of bits can be converted to an integer. 
However, you shouldn't need to convert this output at all!

The intention is that you use os.urandom() to generate x's and y's, 
use those variables to calculate their hashes, check the last k bits of 
those hashes, and repeat until a collision is found (making sure that x != y). 
When a collision is found, return the corresponding x and y. 

The autograder is expecting two bytes objects, so the output from os.urandom() 
is already properly formatted.
"""

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    
    # generate random var x
    x = random.getrandbits(k) # Returns a non-negative integer with k random bits.
    
    # os.urandom
    
    # x_str = ''.join((random.choice(string.ascii_lowercase) for x in range(k)))
    x_rand = os.urandom(k)
    
    # x_utf = str(x_str).encode('utf-8') # convert x to utf-8 byte format
    # x_utf = x_str.encode('utf-8') 
    # x_sha = hashlib.sha256(x_utf).hexdigest()
    x_sha = hashlib.sha256(x_rand).hexdigest()
    
    
    # x = b'\x00'
    
    y_sha = None
    # y_utf = None
    y_rand = None
    
    while y_sha == None:
        y_rand = os.urandom(k)
        # result = hashlib.sha256(y_utf).hexdigest()
        result = hashlib.sha256(y_rand).hexdigest()
        
        if result[-k:] == x_sha[-k:]:
            y_sha = result
            break 
        
    
    # for i in range(100000000):
        # y_utf = str(i).encode('utf-8')
        # result = hashlib.sha256(y_utf).hexdigest()
        #
        # if result[-k:] == x_sha[-k:]:
            # y_sha = result
            # break
    
    # return x_utf, y_utf, x_sha, y_sha
    # return x_rand, y_rand, x_sha, y_sha
    return x_rand, y_rand


# x_utf, y_utf, x_sha, y_sha = hash_collision(4)
# x_rand, y_rand, x_sha, y_sha = hash_collision(4)
x_rand, y_rand = hash_collision(4)

# print(x_rand)
# print(y_rand)
# print(x_sha)
# print(y_sha)
# print(hashlib.sha256(x_utf).hexdigest())
# print(hashlib.sha256(y_utf).hexdigest())
# print(chr(65)) # prints 'A'
