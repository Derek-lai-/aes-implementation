from aes import *
from BitVector import BitVector

spec_key = "2b7e151628aed2a6abf7158809cf4f3c"
plaintext = "3243f6a8885a308d313198a2e0370734"
ciphertext = "3925841d02dc09fbdc118597196a0b32"
print encrypt(spec_key, plaintext)
print ciphertext
print decrypt(spec_key, ciphertext)
print plaintext
#print state_str(init_state_array(plaintext))
