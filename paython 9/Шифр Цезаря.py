def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    result = ''
    for i in text:
        if 'a' <= i <= 'z':
            if mode == 'encrypt':
                shift1 = ((ord(i) - ord("a")) + shift) % 26
            else:
                shift1 = ((ord(i) - ord("a")) - shift) % 26
            shifted = chr(shift1 + ord("a"))
            result += shifted
        elif 'A' <= i <= 'Z':
            if mode == 'encrypt':
                shift1 = ((ord(i) - ord("A")) + shift) % 26
            else:
                shift1 = ((ord(i) - ord("A")) - shift) % 26
            shifted = chr(shift1 + ord("A"))
            result += shifted
        else:
            result += i
    return result
print(caesar_cipher("Hello", 3, 'encrypt'))
print(caesar_cipher("Khoor", 3, 'decrypt'))
print(caesar_cipher("XYZ", 5, 'encrypt'))
print(caesar_cipher("Hello, World!", 13, 'encrypt'))