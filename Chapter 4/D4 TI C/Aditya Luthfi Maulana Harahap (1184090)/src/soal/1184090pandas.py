# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:52:58 2019

@author: Aditya Luthfi
"""

import pandas

#Jawaban No. 3
def bukaModeListPandas():
    df = pandas.read_csv('praktikum1.csv')
    print(df)

#Jawaban No. 4
def bukaModeDictPandas():
    df = pandas.read_csv('praktikum1.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)
    
#Jawaban No. 5
def ubahFormatTanggal():
    df = pandas.read_csv('praktikum1.csv', parse_dates=['tanggal lahir'])
    print(df)

#Jawaban No. 6
def ubahIndexKolom():
    df = pandas.read_csv('praktikum1.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)

#Jawaban No. 7
def ubahNamaKolom():
    df = pandas.read_csv('praktikum1.csv')
    df.columns =['Col_1', 'Col_2', 'Col_3', 'Col_4'] 
    print(df)
    
def tulisCsvPandas():
    df = pandas.read_csv('praktikum1.csv', 
            index_col='NPM', 
            parse_dates=['Tanggal Lahir'],
            header=0, 
            names=['NPM', 'Nama', 'Kelas', 'Tanggal Lahir'])
    df.to_csv('praktikum6.csv')