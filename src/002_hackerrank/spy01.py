# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:10:31 2018

@author: viper
"""
def bit_length_s(number):
    bs = bin(number)
    print(bs)
    s = bs.lstrip('-0b')
    return len(s)
print(bit_length_s(8))
print((8).bit_length())
