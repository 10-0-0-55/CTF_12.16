#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

data = [0x8f, 0xaa, 0x85, 0xa0, 0x48, 0xac, 0x40, 0x95, 0xb6, 0x16, 0xbe, 0x40, 0xb4, 0x16, 0x97, 0xb1, 0xbe, 0xbc, 0x16, 0xb1, 0xbc, 0x16, 0x9d, 0x95, 0xbc, 0x41, 0x16, 0x36, 0x42, 0x95, 0x95, 0x16, 0x40, 0xb1, 0xbe, 0xb2, 0x16, 0x36, 0x42, 0x3d, 0x3d, 0x49, 0x00]

ans = ""
for i in xrange(42):
    ans += chr((((data[i] & 0xAA) >> 1) | (2 * (data[i] & 0x55))) - 9)

print ans
