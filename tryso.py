#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Sep 30, 2016 '
__author__= 'samuel'

import os
import ctypes
from ctypes import *
from ctypes.util import find_library
from ctypes import (
        c_int, c_void_p, c_char_p,
        c_ubyte, c_char,
        )
from ctypes import Structure, POINTER, byref, pointer

libhello_path = os.environ.get('LIBHELLO') or find_library('hello')
libhello = ctypes.cdll.LoadLibrary(libhello_path)

def check_not_null(ret, func, args):
    if ret is not None:
        raise Exception('return value is not null')
    return ret

def check_int(retcode, func, args):
    if retcode < 0:
        raise Exception('return value is < 0')
    return retcode
        

def ffi(name, argtypes, restype, errcheck=None):
    f = getattr(libhello, name)
    f.argtypes = argtypes
    f.restype = restype
    if errcheck:
        f.errcheck = errcheck
    globals()[name] = f
    return f

class PrLicenseInfo(Structure):
    _fields = [
            ('LFVersion', c_ubyte),
            ('AC', c_char*32)
            #('LicenseEnforcementFlag', c_char*2),
            #('ApplicationName', c_char*3),
            #('ProductCode', c_char*3),
            #('LanguageVersion', c_char*2),
            #('VersionType', c_char*2),
            #('OSVersion', c_char*3),
            #('BUCode', c_char*3),
            #('GracePeriod', c_char*2),
            #('ExpirationDate', c_char*9),
            #('SequenceNumber', c_char*9),
            #('SeatsNumber', c_char*7)
            ]

ffi('test_v', [], c_void_p, None)
ffi('test_i', [], c_int, check_int)
ffi('test_cp', [c_char_p], c_int, check_int)
ffi('test_st', [c_void_p], c_int, check_int)

def main():
    s = '1234567890'
    print test_i()
    test_v()
    test_cp(s)

    info = PrLicenseInfo(LFVersion=c_ubyte(2),
                         AC="hahaha")


    #info = PrLicenseInfo(
    #        c_ubyte(1)
    #        c_char_p('c32'),
    #        c_char_p('c2'),
    #        c_char_p('c3'),
    #        c_char_p('c3'),
    #        c_char_p('c2'),
    #        c_char_p('c2'),
    #        c_char_p('c3'),
    #        c_char_p('c3'),
    #        c_char_p('c2'),
    #        c_char_p('c9'),
    #        c_char_p('c9'),
    #        c_char_p('c7')
    #        )
    test_st(pointer(info))

if __name__ == '__main__':
    main()
