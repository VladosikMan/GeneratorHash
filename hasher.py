import sha
import md5
import whirlpool
import ripemd160
import adler32
import crc32

def call_sha1(str):
    return sha.call_sha1(str)

def call_sha224(str):
    return sha.call_sha224(str)

    
def call_sha256(str):
    return sha.call_sha256(str)


def call_sha384(str):
    return sha.call_sha384(str)

def call_sha512(str):
    return sha.call_sha512(str)

def call_md5(str):
    s = md5.call_md5(str)
    return s[0:32]

def call_whirlpool(str):
    return whirlpool.call_whirlpool(str)

def call_ripemd160(str):
    return ripemd160.call_ripemd160(str)

def call_adler32(str):
    s =  adler32.call_adler32(str)
    if len(s) != 8:
         s = "0" + s
    return s
def call_crc32(stre):
    s = crc32.call_crc32(stre)
    ss = str(s)
    if len(s)!=10:
        ss = ss[:2] + "0" + ss[2:]
    return ss



