# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 07:47:58 2022

@author: zbookuser
"""

from cat import Cat

cats = [
        {
            "name": "Барон",
            "gender": "мальчик",
            "age": 2
        },
        {
            "name": "Сэм", 
            "gender": "мальчик", 
            "age": 2
        }        
        ]

for cat_i in cats:
    cat_obj = Cat(name = cat_i.get("name"), 
                  gender = cat_i.get("gender"), 
                  age = cat_i.get("age"))
    print(f"Кот {cat_obj.getName()} {cat_obj.getGender()} {cat_obj.getAge()} года")
    