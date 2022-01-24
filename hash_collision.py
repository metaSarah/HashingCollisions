import hashlib
import os
import math
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
        return( b'\x00',b'\x00' ) # converts hex to binary
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    
    x_rand = os.urandom(k) # generate random string of k bytes

    # convert random string x to sha256 in hex form
    x_sha = hashlib.sha256(x_rand).hexdigest() 
    
    # convert hex value to int
    x_sha_to_int = int(x_sha, base=16)

    # convert int to binary str
    x_bin_str = str(bin(x_sha_to_int))[2:]

    # x_K = x_sha[-k:] 
    x_K = x_bin_str[-k:] # get last K bits
    
    # x_bits = str(bin(int(x_sha, 16)))[-(k*4):].zfill(k*4)
    
    y_sha = None
    y_rand = None
    
    memoization = {}
    
    while y_rand == None:
    
        random = os.urandom(k) # generate random string of k bytes

        # convert random string y to sha256 in hex form
        y_sha = hashlib.sha256(random).hexdigest() 

        # convert hex value to int
        y_sha_to_int = int(y_sha, base=16)

        # convert int to binary str
        y_bin_str = str(bin(y_sha_to_int))[2:]

        # get last K bits
        y_K = y_bin_str[-k:]
        
        
        if y_K == x_K and random != x_rand:
            y_rand = random
            break
        
        elif y_sha[-k:] in memoization and random != memoization[y_sha[-k:]]:
            y_rand = random
            x_rand =  memoization[y_sha[-k:]]
            break
        
        else:
            memoization[y_sha[-k:]] = random
        
        

    return x_rand, y_rand       


x_rand, y_rand = hash_collision(20)

# print(x_rand)
# print(y_rand)
# print(hashlib.sha256(x_rand).hexdigest())
# print(hashlib.sha256(y_rand).hexdigest())
