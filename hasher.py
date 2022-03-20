import sha
import md5

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
