import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    encode = str()
    for letter in text:
        i_alpha = alpha.index(letter)
        i = (a * i_alpha + b) % 26
        encode += alpha[i]
    return encode

def affine_decode(text, a, b):
    decode = str()
    j = mod_inverse(a, 26)
    for letter in text:
        i_alpha = alpha.index(letter)
        i = (j * (i_alpha - b)) % 26
        decode += alpha[i]
    return decode

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    num = 0
    i = 0
    for letter in  ngram:
        i_alpha = alpha.index(letter)
        num = num + (i_alpha * 26**i)
        i += 1
    return num

def convert_to_text(num, n):
    text = str()
    for i in range(n):
        rem = num % 26
        num = num // 26
        text += alpha[rem]
    return text

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_loops(text, n):
    j = str()
    div = []
    w = 0
    for i in range(len(text)):
        div.append(text[i])
    while w < len(div):
        div.insert(w, "#")
        w = w + n + 1
    for i in range(len(div)):
        j += div[i]
    u = j.split("#")
    u.pop(0)
    return u

def affine_n_encode(text, n, a, b):
    encode = str()
    lst = affine_loops(text, n)
    for i in lst:
        ngram = convert_to_num(i)
        i_alpha = (a*ngram+b)%26**n
        conv_txt = convert_to_text(i_alpha, n)
        encode += conv_txt
    return encode

def affine_n_decode(text, n, a, b):
    decode = str()
    lst = affine_loops(text, n)
    inverse = mod_inverse(a, 26**n)
    for i in lst:
        num = convert_to_num(i)
        i_alpha = inverse * (num - b) % 26**n
        conv_txt = convert_to_text(i_alpha, n)
        decode += conv_txt
    return decode

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 2
a = 3
b = 121
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!