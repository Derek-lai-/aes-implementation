#!/usr/env/python

from BitVector import BitVector
from aes import *
import nose

class TestBitVector():
    def test_sbox_lookup(self):
        assert(sbox_lookup(BitVector(intVal = 0xab, size = 8)) == 
                BitVector(bitstring = "01100010"))
        assert(sbox_lookup(BitVector(intVal = 0xcd, size = 8)) == 
                BitVector(bitstring = "10111101"))
        assert(sbox_lookup(BitVector(intVal = 0x1f, size = 8)) == 
                BitVector(bitstring = "11000000"))

    def test_inv_sbox_lookup(self):
        assert(inv_sbox_lookup(BitVector(intVal = 0xab, size = 8)) == 
                BitVector(bitstring = "00001110"))
        assert(inv_sbox_lookup(BitVector(intVal = 0xcd, size = 8)) == 
                BitVector(bitstring = "10000000"))
        assert(inv_sbox_lookup(BitVector(intVal = 0x1f, size = 8)) == 
                BitVector(bitstring = "11001011"))

    def test_sub_key_bytes(self):
        assert(sub_key_bytes(BitVector(intVal = 0x01234567, size = 32)) == 
                BitVector(bitstring = "01111100001001100110111010000101"))
        assert(sub_key_bytes(BitVector(intVal = 0x89ABCDEF, size = 32)) == 
                BitVector(bitstring = "10100111011000101011110111011111"))
        assert(sub_key_bytes(BitVector(intVal = 0xFADBADEE, size = 32)) == 
                BitVector(bitstring = "00101101101110011001010100101000"))

    def test_shift_bytes_left(self):
        assert(shift_bytes_left(BitVector(intVal = 0x01234567, size = 32), 1) == 
                BitVector(bitstring = "00100011010001010110011100000001"))
