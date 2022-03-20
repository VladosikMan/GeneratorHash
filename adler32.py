import sys
import os

def adler32(string):
    MOD = 65521
    a,b = 1,0
    for c in string:
        a = (a + ord(c)) % MOD
        b = (b+a) % MOD
    return format((b << 16) + a,'X')

def call_adler32(str):
    return adler32(str)


