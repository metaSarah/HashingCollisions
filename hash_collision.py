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
    
    x_rand = os.urandom(k)
    
    x_sha = hashlib.sha256(x_rand).hexdigest()
    
    # x_bits = str(bin(int(x_sha, 16)))[-(k*4):].zfill(k*4)
    
    y_sha = None
    y_rand = None
    
    x_K = x_sha[-k:]
    
    while y_rand == None:
    
        random = os.urandom(k)
        y_sha = hashlib.sha256(random).hexdigest()
        y_K = y_sha[-k:]
        
        if y_K == x_K:
            y_rand = random
            break

    return x_rand, y_rand       


x_rand, y_rand = hash_collision(5)

print(x_rand)
print(y_rand)

print(hashlib.sha256(x_rand).hexdigest())
print(hashlib.sha256(y_rand).hexdigest())
# print(chr(65)) # prints 'A'
