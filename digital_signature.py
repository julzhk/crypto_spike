# coding=utf-8
import hashlib
from random import randint

def generate_keys(keysize=256):
    # (sk, pk) := generateKeys(​keysize​) ​The generateKeys method takes a key size and generates
    # a key pair. The secret key sk is kept privately and used to sign messages. pk is the public
    # verification key that you give to everybody. Anyone with this key can verify your signature.
    hasher = hashlib.md5()
    rand = str(randint(0,1000))
    hasher.update(rand)
    hasher.update('public')
    pk = hasher.hexdigest()
    hasher.update('secret')
    sk = hasher.hexdigest()
    return sk,pk

def sign(sk, msg):
    # sign(​sk​, ​message​) ​The sign method takes a message, msg, and a secret key, sk, as
    # input and outputs a signature for the msg under sk
    hasher = hashlib.md5()
    hasher.update(sk)
    hasher.update(msg)
    return hasher.hexdigest()

def is_valid(pk,message,signature):
    # isValid := verify(​pk​, ​message​, ​sig​) ​The verify method takes a message, a signature, and a
    # public key as input. It returns a boolean value, isValid, that will be true​if sig is a valid
    # signature for message under public key pk, and false ​otherwise.

    return True

sk, pk = generate_keys()
sign= sign(sk=sk, msg='hello')

print is_valid(pk=pk, message='hello',signature=sign)