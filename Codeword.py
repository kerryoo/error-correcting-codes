#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:53:34 2020

@author: kerryoo

You can only initialize Codewords from a string or int containing only 0's and
1's or a List containing single digit integers (again only 0's and 1's).

If you try to convert it to a string or print it, it'll be formatted like
a regular integer. For example, while the class saves 1001 as [1, 0, 0, 1],
it will be converted to 1001.

If you use the len function, for example len(codewordA), the length of the codeword
will be returned.

If you use the index function, for example codeword[3], the digit at that index
will be returned.

You can add two codewords together. I've added some protection against adding
things that aren't explicitly defined as codewords. You should be able to add
properly formated integers, strings, and lists to codewords without concern.
It is also not a concern of adding codewords of different lengths. The shorter length
codeword will have 0's attached to the front.

The distance function is built primarily from the addition function, so the same
holds true for this function.
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
            
    def distance(self, rhsWord):
        wordSum = self + rhsWord
        return wordSum.__weight
    
    def cycle(self, offset):
        
        