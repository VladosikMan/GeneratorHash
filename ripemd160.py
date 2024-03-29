﻿#! /usr/bin/python
#coding: UTF-8
import argparse
import hashlib


	
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('inFile')
    parser.add_argument('outFile')
    return parser.parse_args()	

	
# Выравнивание потока и добавление длины сообщения
def alignment(msg):
    msg_len = len(msg) * 8
    msg.append(0x80)
    while len(msg)% 64 != 56:
	    msg += [0]  
    for i in range(8):
        msg.append(msg_len >> i * 8)
    return msg	
	
	
# 5 нелинейных побитовых функций 
def F(j, x, y, z):
    if j < 16:	
        return (x ^ y ^ z)
    if j < 32: 
        return(x & y) | (~x & z)
    if j < 48:	
        return ((x | ~y) ^ z)
    if j < 64:
        return (x & z) | (y & ~z)
    if j < 80:
        return (x ^ (y | ~z))		

		
# Добавляемые шестнадцатеричные константы
def K(j):
    if j < 16:
        return 0x00000000	
    if j < 32:
        return 0x5A827999		
    if j < 48:
        return 0x6ED9EBA1
    if j < 64:
        return 0x8F1BBCDC
    if j < 80:
        return 0xA953FD4E
		
def K1(j):
    if j < 16:
        return 0x50A28BE6
    if j < 32:
        return 0x5C4DD124
    if j < 48:
        return 0x6D703EF3
    if j < 64:
        return 0x7A6D76E9
    if j < 80:
        return 0x00000000
		
		
# циклический сдвиг влево на n бит 
def rotateLeft(x, n):
    x = x & 0xFFFFFFFF   
    return ((x << n) | (x >> (32-n))) & 0xFFFFFFFF	
	
	
def toLittleEndian(word):
    res = 0
    res |= ((word >> 0) & 0xFF) << 24
    res |= ((word >> 8) & 0xFF) << 16
    res |= ((word >> 16) & 0xFF) << 8
    res |= ((word >> 24) & 0xFF) << 0
    return res
	
		
def rounds(buf, x):
    A = buf[0]
    B = buf[1]
    C = buf[2]
    D = buf[3]
    E = buf[4]
	
    A1 = buf[0]
    B1 = buf[1]
    C1 = buf[2]
    D1 = buf[3]
    E1 = buf[4]
	
    # Определяем константы для r(j) и rol(j)
    R = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8,
        3, 10, 14, 4, 9, 15, 8, 1, 2, 7, 0, 6, 13, 11, 5, 12,
        1, 9, 11, 10, 0, 8, 12, 4, 13, 3, 7, 15, 14, 5, 6, 2,
        4, 0, 5, 9, 7, 12, 2, 10, 14, 1, 3, 8, 11, 6, 15, 13
        ]

    R1 = [
        5, 14, 7, 0, 9, 2, 11, 4, 13, 6, 15, 8, 1, 10, 3, 12,
        6, 11, 3, 7, 0, 13, 5, 10, 14, 15, 8, 12, 4, 9, 1, 2,
        15, 5, 1, 3, 7, 14, 6, 9, 11, 8, 12, 2, 10, 0, 4, 13,
        8, 6, 4, 1, 3, 11, 15, 0, 5, 12, 2, 13, 9, 7, 10, 14,
        12, 15, 10, 4, 1, 5, 8, 7, 6, 2, 13, 14, 0, 3, 9, 11
        ]

    S = [
        11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8,
        7, 6, 8, 13, 11, 9, 7, 15, 7, 12, 15, 9, 11, 7, 13, 12,
        11, 13, 6, 7, 14, 9, 13, 15, 14, 8, 13, 6, 5, 12, 7, 5,
        11, 12, 14, 15, 14, 15, 9, 8, 9, 14, 5, 6, 8, 6, 5, 12,
        9, 15, 5, 11, 6, 8, 13, 12, 5, 12, 13, 14, 11, 8, 5, 6
        ]    

    S1 = [
        8, 9, 9, 11, 13, 15, 15, 5, 7, 7, 8, 11, 14, 14, 12, 6,
        9, 13, 15, 7, 12, 8, 9, 11, 7, 7, 12, 7, 6, 15, 13, 11,
        9, 7, 15, 11, 8, 6, 6, 14, 12, 13, 5, 14, 13, 13, 7, 5,
        15, 5, 8, 11, 14, 14, 6, 14, 6, 9, 12, 9, 12, 5, 15, 8,
        8, 5, 12, 9, 12, 5, 14, 6, 8, 13, 6, 5, 15, 13, 11, 11
        ]
	# Выполнение алгоритма происходит по двум параллельным путям	
    for j in range(80):
        T = A + F(j, B, C, D) + x[R[j]] + K(j)
        T = rotateLeft(T, S[j]) + E 
        A = E
        E = D
        D = rotateLeft(C, 10)
        C = B
        B = T
		
        T = A1 + F(79 - j, B1, C1, D1) + x[R1[j]] + K1(j)
        T = rotateLeft(T, S1[j]) + E1 	
        A1 = E1
        E1 = D1
        D1 = rotateLeft(C1, 10)
        C1 = B1
        B1 = T
		
    T = (buf[1] + C + D1) 
    buf[1] = (buf[2] + D + E1)  
    buf[2] = (buf[3] + E + A1) 
    buf[3] = (buf[4] + A + B1)  
    buf[4] = (buf[0] + B + C1) 
    buf[0] = T	
	
    return buf
   
def calc_ripemd160(data):
    data = [ord(i) for i in data]
	
    # Шаг 1 Выравнивание потока
    # Шаг 2 Добавление длины сообщения
    data = alignment(data)

    # Шаг 3 Инициализация буфера
    buf = [0] * 5
    buf[0] = 0x67452301
    buf[1] = 0xefcdab89
    buf[2] = 0x98badcfe
    buf[3] = 0x10325476
    buf[4] = 0xc3d2e1f0
	
	 # поток байт  разбиваем на поток слов
    data_words = []
    for i in range(len(data) // 4): 
        q = 0
        for j in range(4):
            q |= data[i * 4 + j] << j * 8
        data_words.append(q)
	
    # Шаг 4 Вычисление в цикле
    # разбиваем поток на блоки по 16 слов   
    for i in range(0, len(data_words), 16):
	    # i-ый блок заносится в х 
        x = data_words[i:i+16]
        buf = rounds(buf, x)
			
    # Шаг 5 Результат вычислений 

    res = ""
    for i in buf:
        res += "{:08x}".format(toLittleEndian(i))
		
    return res

def call_ripemd160(str):
    b = bytes(str, 'utf-8')
    h = hashlib.new("ripemd160")
    h.update(b)
    return  h.hexdigest()
	

