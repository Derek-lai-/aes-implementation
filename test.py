#!/usr/env/python

from BitVector import BitVector
from aes import *
from nose.tools import with_setup
import nose

class TestBitVector():
    def setup(self):
        global values
        values = [
            BitVector(intVal = 0xab, size = 8),
            BitVector(intVal = 0xcd, size = 8),
            BitVector(intVal = 0x1f, size = 8),
            BitVector(intVal = 0x01234567, size = 32),
            BitVector(intVal = 0x89ABCDEF, size = 32),
            BitVector(intVal = 0xFADBADEE, size = 32),
            BitVector(intVal = 0x3e, size = 8),
            BitVector(intVal = 0xa4, size = 8),
        ]

    @with_setup(setup)
    def test_sbox_lookup(self):
        assert(sbox_lookup(values[0]) == BitVector(bitstring = "01100010"))
        assert(sbox_lookup(values[1]) == BitVector(bitstring = "10111101"))
        assert(sbox_lookup(values[2]) == BitVector(bitstring = "11000000"))

    @with_setup(setup)
    def test_inv_sbox_lookup(self):
        assert(inv_sbox_lookup(values[0]) == BitVector(bitstring = "00001110"))
        assert(inv_sbox_lookup(values[1]) == BitVector(bitstring = "10000000"))
        assert(inv_sbox_lookup(values[2]) == BitVector(bitstring = "11001011"))

    @with_setup(setup)
    def test_sub_key_bytes(self):
        assert(sub_key_bytes(values[3]) == 
               BitVector(bitstring = "01111100001001100110111010000101"))
        assert(sub_key_bytes(values[4]) == 
               BitVector(bitstring = "10100111011000101011110111011111"))
        assert(sub_key_bytes(values[5]) == 
               BitVector(bitstring = "00101101101110011001010100101000"))

    @with_setup(setup)
    def test_shift_bytes_left(self):
        assert(shift_bytes_left(values[3], 1) == 
               BitVector(bitstring = "00100011010001010110011100000001"))
        assert(shift_bytes_left(values[4], 2) == 
               BitVector(bitstring = "11001101111011111000100110101011"))
        assert(shift_bytes_left(values[5], 3) == 
               BitVector(bitstring = "11101110111110101101101110101101"))

    @with_setup(setup)
    def test_shift_bytes_right(self):
        assert(shift_bytes_right(values[3], 1) == 
               BitVector(bitstring = "01100111000000010010001101000101"))
        assert(shift_bytes_right(values[4], 2) == 
               BitVector(bitstring = "11001101111011111000100110101011"))
        assert(shift_bytes_right(values[5], 3) == 
               BitVector(bitstring = "11011011101011011110111011111010"))

    @with_setup(setup)
    def test_gf_mult(self):
        assert(gf_mult(values[0], 0xcd) == BitVector(intVal = 0xBB, size = 8))
        assert(gf_mult(values[1], 0x3e) == BitVector(intVal = 0x06, size = 8))
        assert(gf_mult(values[2], 0xa4) == BitVector(intVal = 0xA8, size = 8))
