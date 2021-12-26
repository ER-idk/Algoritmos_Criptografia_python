alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
    encode = str()
    # Repete a palavra-chave até que tenha o mesmo tamanho da frase a ser criptografada
    while len(keyword) < len(text):
        keyword += keyword
    if len(keyword) > len(text):
        keyword = keyword[:len(text)]
    for i in range(len(text)):
        # Encontra o indice no alfabeto
        i_alpha = alpha.index(text[i]) + alpha.index((keyword[i]))
        if i_alpha >= len(alpha):
            i_alpha = i_alpha - len(alpha)
        encode += alpha[i_alpha]
    return encode


def vig_decode(text, keyword):
    decode = str()
    while len(keyword) < len(text):
        keyword += keyword
    if len(keyword) > len(text):
        keyword = keyword[:len(text)]
    for i in range(len(text)):
        i_alpha = alpha.index(text[i]) - alpha.index((keyword[i]))
        decode += alpha[i_alpha]
    return decode


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
