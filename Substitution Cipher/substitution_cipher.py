alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def sub_encode(text, codebet):
    encode = str()
    w = len(text)
    for i in range(w):
        encode += codebet[alpha.index(text[i])]
    return encode


def sub_decode(text, codebet):
    decode = str()
    w = len(text)
    for i in range(w):
        decode += alpha[codebet.index(text[i])]
    return decode


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
