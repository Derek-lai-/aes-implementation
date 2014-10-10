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
        assert(shift_bytes_left(BitVector(intVal = 0x89ADCDEF, size = 32), 1) == 
               BitVector(bitstring = "10101101110011011110111110001001"))
        assert(shift_bytes_left(BitVector(intVal = 0xFADBADEE, size = 32), 1) == 
               BitVector(bitstring = "11011011101011011110111011111010"))

    def test_shift_bytes_right(self):
        assert(shift_bytes_right(BitVector(intVal = 0x01234567, size = 32), 1) == 
               BitVector(bitstring = "01100111000000010010001101000101"))
        assert(shift_bytes_right(BitVector(intVal = 0x89ADCDEF, size = 32), 1) == 
               BitVector(bitstring = "11101111100010011010110111001101"))
        assert(shift_bytes_right(BitVector(intVal = 0xFADBADEE, size = 32), 1) == 
               BitVector(bitstring = "11101110111110101101101110101101"))

    def test_gf_mult(self):
        val_a = (BitVector(intVal = 0xab, size = 8))
        val_b = (BitVector(intVal = 0xcd, size = 8))
        val_c = (BitVector(intVal = 0xef, size = 8))
        val_d = (BitVector(intVal = 0x04, size = 8))
        val_e = (BitVector(intVal = 0xc5, size = 8))
        assert(gf_mult(val_a, 0xcd) == val_a.gf_mult(val_b))
        assert(gf_mult(val_c, 0x04) == val_c.gf_mult(val_d))
        assert(gf_mult(val_e, 0xab) == val_e.gf_mult(val_a))
