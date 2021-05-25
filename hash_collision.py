import hashlib
import os

import random
import string

""" hash_collision(k) returns x and y,
such that the SHA256(x) and SHA256(y) match on their final k bits. 

The return variables, x and y, should be encoded as bytes.
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
    
    x_str = ''.join((random.choice(string.ascii_lowercase) for x in range(k)))
    
    
    x_utf = str(x_str).encode('utf-8') # convert x to utf-8 byte format
    x_sha = hashlib.sha256(x_utf).hexdigest()
    
    
    # x = b'\x00'
    
    y_sha = None
    y_utf = None
    
    for i in range(10000000):
        y_utf = str(i).encode('utf-8')
        result = hashlib.sha256(y_utf).hexdigest()
        
        if result[-k:] == x_sha[-k:]:
            y_sha = result
            break
    
    return x_utf, y_utf


x, y = hash_collision(5)
print(x)
print(y)
# print(chr(65)) # prints 'A'
