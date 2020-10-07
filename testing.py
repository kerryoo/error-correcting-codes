#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:15:51 2020

@author: kerryoo
"""

from Codeword import Codeword


a = Codeword([1, 0, 1, 1, 0, 1])
b = Codeword([0, 1, 0, 0, 1])

c = a + b
print(c)

print(a)
print(b)
print(c.distance(b))