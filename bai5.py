# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:26:04 2024

@author: KIEUNHI
"""

a = int(input("Nhập số giờ: "))
b = int(input("Nhập số phút: "))
c = int(input("Nhập số giây: "))
# Tính
tong_giay = a*3600 + b*60 + c 
# In ra kết quả
print("Tổng đổi ra giây: ", tong_giay)