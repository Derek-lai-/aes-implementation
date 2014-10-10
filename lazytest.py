from aes import *
from BitVector import BitVector

spec_key = BitVector(intVal = 0x2b7e151628aed2a6abf7158809cf4f3c, size = 128)
plaintext = BitVector(intVal = 0x3243f6a8885a308d313198a2e0370734, size = 128)
print encrypt(spec_key, plaintext)
