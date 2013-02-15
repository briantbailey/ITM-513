"""
Brian T. Bailey
ITM 513 - MP4
Brian's Crypto Module
"""

import array
import base64
from hashlib import sha256


def bb_encrypt(plaintext, key):
    """Encrypts plaintext using key
    
    Method to encrypt plaintext using 256 bit (32 byte) key. Key must be
    256 bits long. Use key_gen method to generate key from a password.
    
    Args:
        plaintext: A String of text to encrypt using key
        key: A 256 bit (32 byte) String based key
    
    Returns:
        A string of encrypted text that has been base64 encoded
    """
    key_array = array.array('B', key)
    
    # Create list of plaintext blocks
    block_count = ((len(plaintext) / 32), (len(plaintext) % 32))
    plaintext_blocks = []
    for i in range(block_count[0]):
        start_index = i * 32
        end_index = (i + 1) * 32
        plaintext_blocks.append(plaintext[start_index : end_index])
    # Perform block padding
    if block_count[1] == 0:
        plaintext_blocks.append(chr(32) * 32)
    else:
        plaintext_blocks.append(plaintext[(block_count[0] * 32) : ] + (chr(32 - block_count[1]) * (32 - block_count[1])))
        
    # Generate ciphertext
    ciphertext = ''
    for block in plaintext_blocks:
        block_array = array.array('B', block)
        block_array.reverse()
        for c in range(len(block_array)):
            block_array[c] ^= key_array[c]
        ciphertext += block_array.tostring()
    
    ciphertext = base64.b64encode(ciphertext)
    
    return ciphertext


def bb_decrypt(ciphertext, key):
    """Decrypts ciphertext using key
    
    Method to decrypt ciphertext using 256 bit (32 byte) key. Key must be
    256 bits long. Use key_gen method to generate key from a password.
    
    Args:
        ciphertext: A String of encrypted text to decrypt using key
        key: A 256 bit (32 byte) String based key
    
    Returns:
        A String of decrypted plaintext
    """
    key_array = array.array('B', key)
    
    ciphertext = base64.b64decode(ciphertext)
    
    # Create list of ciphertext blocks
    block_count = ((len(ciphertext) / 32), (len(ciphertext) % 32))
    ciphertext_blocks = []
    for i in range(block_count[0]):
        start_index = i * 32
        end_index = (i + 1) * 32
        ciphertext_blocks.append(ciphertext[start_index : end_index])
    
    # Generate plaintext
    plaintext = ''
    for block in ciphertext_blocks:
        block_array = array.array('B', block)
        for c in range(len(block_array)):
            block_array[c] ^= key_array[c]
        block_array.reverse()
        plaintext += block_array.tostring()
    
    # Remove padding
    padding_value = ord(plaintext[len(plaintext) - 1])    
    plaintext = plaintext[:-padding_value]
        
    return plaintext


def key_gen(password):
    """Generates a 256 bit (32 byte) key from a password
    
    Method to generate a 256 bit (32 byte) key from a password.
    
    Args:
        password: A String representing the password used.
        
    Returns:
        A String representing the 256 bit (32 byte) key
    """
    key_rounds = 20
    s = sha256()
    s.update(password)
    key = s.digest()
    for i in range(key_rounds):
        h = sha256()
        h.update(key + password)
        key = h.digest()
    return key


# Testing
if __name__ == '__main__':
    print("Testing Brian's Crypto Module\n")
    p1 = "Nobody inspects the spammish repetition... Nobody inspects the spammish repetition"
    p2 = "Nobody inspects the spammish rep"
    print "plain text: " + p1
    print "length: " + str(len(p1))
    print "plain text: " + p2
    print "length: " + str(len(p2))
    
    t1 = bb_encrypt(p1, key_gen('a password'))
    t2 = bb_encrypt(p2, key_gen('a password'))
    print "cipher text: " + t1
    print "length: " + str(len(t1))
    print "cipher text: " + t2
    print "length: " + str(len(t2))
    
    d1 = bb_decrypt(t1, key_gen('a password'))
    d2 = bb_decrypt(t2, key_gen('a password'))
    print "plain text: " + d1
    print "length: " + str(len(d1))
    print "plain text: " + d2
    print "length: " + str(len(d2))