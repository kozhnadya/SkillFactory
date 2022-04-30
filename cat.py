# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 04:58:59 2022

@author: zbookuser
"""

class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        
    def getName(self):
        return self.name
    
    def getGender(self):
        return self.gender
    
    def getAge(self):
        return self.age