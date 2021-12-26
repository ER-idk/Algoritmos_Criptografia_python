alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encode(text, n):
    encode = str()
    w = len(text)
    for i in range(w):
        # Encontra o indice no alfabeto
        i_alpha = alpha.index(text[i]) + n
        
        # Retorna ao inicio do alfabeto caso necessário
        if i_alpha >= len(alpha):
            i_alpha = i_alpha - len(alpha)
        encode += alpha[i_alpha]

    return encode

# Para decodificar basta repetir o mesmo processo porém diminuindo o deslocamento
def caesar_decode(text, n):
    decode = str()
    w = len(text)
    for i in range(w):
        i_alpha = alpha.index(text[i]) - n
        decode += alpha[i_alpha]
    return decode


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
