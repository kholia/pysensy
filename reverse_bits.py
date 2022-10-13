#!/usr/bin/env python3

"""
$ python reverse_bits.py 0xFD023000
0xc40bf
"""

import sys

n = int(sys.argv[1], 16)

print(hex(int('{:08b}'.format(n)[::-1], 2)))
