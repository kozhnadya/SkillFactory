# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:18:52 2022

@author: n.m.kozhevnikova
"""

per_cent = {'ТБК': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму, которую планируете положить: "))
per_cent_list = list(map(float, per_cent.values()))
deposit = [];
for i in per_cent_list:
    deposit.append(money * i/100)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))

