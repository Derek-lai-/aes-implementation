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
        assert(gf_mult(values[0], 0xCD) == BitVector(intVal = 0xBB, size = 8))
        assert(gf_mult(values[1], 0x3E) == BitVector(intVal = 0x06, size = 8))
        assert(gf_mult(values[2], 0xA4) == BitVector(intVal = 0xA8, size = 8))

class TestStateArray():
    def setup(self):
        global keys
        global arrays
        global values
        keys = [
            BitVector(intVal = 0xBADFADDABADCD234EBCAF936EFFFE999, size = 128),
            BitVector(intVal = 0x3E9CFF00CBC44EE23927184839289184, size = 128),
            BitVector(intVal = 0xABCDEF01234567890ABCDEF123456790, size = 128),
            BitVector(intVal = 0x01234567247128947BCDEFABECCEEFF2, size = 128),
            BitVector(intVal = 0x89ABCDEFBEDEBEEDEEFADDAF92318002, size = 128),
            BitVector(intVal = 0xFADBADEE3482EABCFEBBCEFA8921EC83, size = 128),
            BitVector(intVal = 0x3ECBEA83BECDEFEABCE93EACE21BCDE3, size = 128),
            BitVector(intVal = 0xA4BCDE28ADCEDFE291EADCEFEDF92ECD, size = 128),
        ]
        arrays = [init_state_array(bv) for bv in keys]
        values = [
            BitVector(intVal = 0x3CBE31BC, size = 32),
            BitVector(intVal = 0xBCE3CEBF, size = 32),
            BitVector(intVal = 0xA82BEC09, size = 32),
            BitVector(intVal = 0xBAC92FEB, size = 32),
            BitVector(intVal = 0xACB9FEDE, size = 32),
            BitVector(intVal = 0x10EB93EF, size = 32),
            BitVector(intVal = 0x9382EBCE, size = 32),
            BitVector(intVal = 0x92A4915E, size = 32),
            BitVector(intVal = 0x92A4915E, size = 32),
        ]
    
    @with_setup(setup)
    def test_sub_bytes(self):
        results = ['f49e9557f486b518e9749905df161eee',
                'b2de16631f1c2f9812ccad521234815f',
                '62bddf7c266e85a767651da1266e8560',
                '7c266e8536a3342221bddf62ce8bdf89',
                'a762bddfae1dae55282dc1794fc7cd77',
                '2db9952818138765bbea8b2da7fdceec',
                'b21f87ecaebddf87651eb29198afbd11',
                '49651d34958b9e98818786df559931bd']
        assert(results == [state_str(sub_bytes(array)) for array in arrays])

    @with_setup(setup)
    def test_inv_sub_bytes(self):
        results = ['c0ef187ac0937f283c106924617debf9',
                'd11c7d525988b63b5b3d34d45beeac4f',
                '0e80610932680af2a3789c2b32680a96',
                '0932680aa62ceee70380610e83ec6104',
                'f20e80615a9c5a539914c91b742e3a6a',
                '149f18992811bb780cfeec14f27b8341',
                'd159bb415a8061bb78ebd1aa3b44804d',
                '1d789cee18ecef3bacbb93615369c380']
        assert(results == [state_str(inv_sub_bytes(array)) for array in arrays])

    @with_setup(setup)
    def test_shift_rows(self):
        results = ['badcf999bacae9daebffad34efdfd236', 
                '3ec41884cb2791003928ffe2399c4e48', 
                'ab45de9023bc67010a45ef8923cd67f1', 
                '0171eff224cdef677bce4594ec2328ab', 
                '89dedd02befa80efee31cded92abbeaf', 
                'fa82ce8334bbeceefe21adbc89dbeafa', 
                '3ecd3ee3bee9cd83bc1beaeae2cbefac', 
                'a4cedccdadea2e2891f9dee2edbcdfef']

        assert(results == [state_str(shift_rows(array)) for array in arrays])

    @with_setup(setup)
    def test_inv_shift_rows(self):
        results = ['bafff934badfe936ebdcad99efcad2da',
                '3e2818e2cb9c914839c4ff8439274e00',
                'ab45de8923cd67f10a45ef9023bc6701',
                '01ceef942423efab7b7145f2eccd2867',
                '8931ddedbeab80afeedecd0292fabeef',
                'fa21cebc34dbecfafe82ad8389bbeaee',
                '3e1b3eeabecbcdacbccdeae3e2e9ef83',
                'a4f9dce2adbc2eef91cedecdedeadf28']

        assert(results == [state_str(inv_shift_rows(array)) for array in arrays])

    @with_setup(setup)
    def test_add_round_key(self):

        v = 'e9f74eec023020f61bf2ccf2353c21c7'
        k = '000102030405060708090a0b0c0d0e0f'
        s = '549932d1f08557681093ed9cbe2c974e'
        ss = init_state_array(key_bv(s))
        assert(v == state_str(add_round_key(ss, k)))

        '''assert(results == [state_str(add_round_key(arrays[i], values[i])) for i in xrange(8)])'''

class TestRound(): 
    def setup(self):
        global spec_key
        global plaintext
        spec_key = BitVector(intVal = 0x2b7e151628aed2a6abf7158809cf4f3c, size = 128)
        plaintext = BitVector(intVal = 0x3243f6a8885a308d313198a2e0370734, size = 128)

    @with_setup(setup)
    def test_round_one(self):
        key_sched = init_key_schedule(spec_key)
        state_array = init_state_array(plaintext)
        state_array = add_round_key(state_array, key_sched[0:4])
        assert(state_str(state_array) == "193de3bea0f4e22b9ac68d2ae9f84808")

class TestCryption():
    def test_encrypt_one(self):
        test_key = '2b7e151628aed2a6abf7158809cf4f3c'
        test_plaintext = '3243f6a8885a308d313198a2e0370734'
        result = '3925841d02dc09fbdc118597196a0b32'
        assert(encrypt(test_key, test_plaintext) == result)

    def test_encrypt_two(self):
        test_plaintext = '3243f6a2315a308acb3198a2e0343213'
        test_key = '1a2b151242aed2a6abf715abc31f4f3c'
        result = '8492f7a07e0535b3eb523cf0cce736e2'
        assert(encrypt(test_key, test_plaintext) == result)

    def test_decryption_one(self):
        result = '00112233445566778899aabbccddeeff'
        test_key = '000102030405060708090a0b0c0d0e0f'
        test_plaintext = '69c4e0d86a7b0430d8cdb78070b4c55a'
        assert(decrypt(test_key, test_plaintext) == result)

    def test_decryption_two(self):
        result = '3243f6a2315a308acb3198a2e0343213'
        test_key = '1a2b151242aed2a6abf715abc31f4f3c'
        test_plaintext = '8492f7a07e0535b3eb523cf0cce736e2'
        assert(decrypt(test_key, test_plaintext) == result)