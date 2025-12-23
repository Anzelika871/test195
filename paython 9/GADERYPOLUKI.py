def encode(message, key):
    result = ''
    for i in message:
        if i.lower() in key:
            idx = key.index(i.lower())
            new_idx = idx + 1 if idx % 2 == 0 else idx - 1
            new_char = key[new_idx]
            result += new_char.upper() if i.isupper() else new_char
        else:
            result += i
    return result
def decode(encrypted_message, key):
    return encode(encrypted_message, key)
print(encode("ABCD", "agedyropulik"))
print(encode("Ala has a cat", "gaderypoluki"))
print(decode("Dkucr pu yhr ykbir", "politykarenu"))
print(decode("Hmdr nge brres", "regulaminowy"))