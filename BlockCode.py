#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:55:20 2020

@author: kerryoo
"""

from Codeword import Codeword
from math import *

class BlockCode:
    def __init__(self, *argv):
        if type(argv[0]) is Codeword:
                self.codeLength = len(Codeword)
        
        self.codes = {}
                
        for arg in argv:
            if type(arg) is not Codeword:
                raise Exception("Only accepts Codeword arguments")
            if len(arg) != self.codeLength:
                raise Exception("Inputted arguments are not of same length")
            self.codes.add(arg)
        
        self.length = len(self.codes)
    
    def getInformationRate():
        return (1/self.codeLength) * math.log(self.length, 2)
    
    def isLinearCode();:
        
    