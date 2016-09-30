#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Sep 30, 2016 '
__author__= 'samuel'

import os
import ctypes
from ctypes.util import find_library
from ctypes import (
        c_int, c_void_p
        )

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

ffi('test_v', [], c_void_p, None)
ffi('test_i', [], c_int, check_int)

def main():
    print test_i()
    test_v()

if __name__ == '__main__':
    main()
