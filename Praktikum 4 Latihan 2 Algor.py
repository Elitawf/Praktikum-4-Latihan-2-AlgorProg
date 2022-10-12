# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:43:52 2022

@author: Elita
"""

import calendar
print("Program menentukan jumlah hari di salah satu bulan")
ulang = "yes"
while ulang == "yes" or ulang == "no": 
    year = int(input("Masukan Tahun : ")) 
    month = int(input("Masukan Bulan : "))
    print("Jumlah hari di bulan ke",month, "Adalah", (calendar.monthrange(year, month)[1]), )
    ulang = input("ketik'yes' untuk melanjutkan, ketik 'no' untuk berhenti ")
    if ulang == "no":
        print("Terimakasih sudah Menggunakan program saya")
        print("Elita Wahyu Firdasari-065002200038")
        break