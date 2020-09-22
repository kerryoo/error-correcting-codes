#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:53:34 2020

@author: kerryoo
"""

class Codeword:
    def __init__(self, word = None):
        if type(word) is int or type(word) is str:
            self.word = []
            self.__weight = 0
            for x in str(word):
                if x != '0' and x != '1':
                    raise Exception("Sorry, we can only support 1's and 0's")
                if x == '1':
                    self.__weight += 1
                self.word.append(int(x))
        elif type(word) is list:
            self.__weight = 0
            for digit in word:
                if digit != 0 and digit != 1:
                    raise Exception("Sorry, the list is invalid")
                if digit == 1:
                    self.__weight += 1
            self.word = word
        else:
            raise Exception("Sorry, you can only init with int, list of ints, or string")
    
    def __repr__(self):
        pretty = ''
        for digit in self.word:
            pretty += str(digit)
        return pretty;
    
    def __len__(self):
        return len(self.word)
    
    def __getitem__(self, index):
        return self.word[index]
    
    def __add__(self, rhsWord):
        if type(rhsWord) is not Codeword:
            rhsWord = Codeword(rhsWord)
        
        localWord = self.word
        
        if len(localWord) != len(rhsWord):
            difference = len(localWord) - len(rhsWord)
            extraZeros = [0 for i in range(abs(difference))]
            
            if difference > 0:
                rhsWord = extraZeros + rhsWord.word
            else:
                localWord = extraZeros + localWord
        
        result = []
        
        for i, digit in enumerate(localWord):
            if digit == rhsWord[i]:
                result.append(0)
            else:
                result.append(1)
        return Codeword(result)
            
                
        