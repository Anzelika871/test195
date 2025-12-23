def rot13(text: str) -> str:
    result = ''
    for i in text:
        if 'a' <= i <= 'z':
            shift = chr((ord(i) - ord('a') + 13) % 26 + ord('a'))
            result += shift
        elif 'A' <= i <= 'Z':
            shift = chr((ord(i) - ord('A') + 13) % 26 + ord('A'))
            result += shift
        else:
            result += i
    return result
print(rot13("Hello, World!"))
print(rot13("Uryyb, Jbeyq!"))
print(rot13(rot13("Test")))
print(rot13("123!@#"))