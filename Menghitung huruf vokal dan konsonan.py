# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 15:06:48 2021

@author: User
"""

print("====== PROGRAM MENGHITUNG HURUF VOKAL DAN KONSONAN DARI KALIMAT ======") 

kalimat = input("Masukkan Kalimat : ").lower()
huruf_vokal = {
  'a': 0,
  'i': 0,
  'u': 0,
  'e': 0,
  'o': 0
}
total_huruf_vokal = 0
total_huruf_konsonan = 0

for karakter in kalimat:
  if karakter in ['a', 'i', 'u', 'e',  'o']:
    huruf_vokal[karakter] += 1
    total_huruf_vokal += 1
  else:
    total_huruf_konsonan += 1

print("Jumlah Huruf Vokal: ",total_huruf_vokal)
print("Jumlah Huruf Konsonan: ",total_huruf_konsonan)
