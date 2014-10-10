from aes import *
from BitVector import BitVector

spec_key = BitVector(intVal = 0x2b7e151628aed2a6abf7158809cf4f3c, size = 128)
plaintext = BitVector(intVal = 0x3243f6a8885a308d313198a2e0370734, size = 128)
ciphertext = BitVector(intVal = 0x3925841d02dc09fbdc118597196a0b32, size = 128)
badcipher = BitVector(intVal = 0xe21a02a05dbb645a47a55cff0df224fb, size = 128)
print encrypt(spec_key, plaintext)
print decrypt(spec_key, badcipher)
print state_str(init_state_array(plaintext))
