alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

"""
def encrypt(plain_text, shift_amount):
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            index += shift_amount
            plain_text = plain_text.replace(letter, alphabet[index])
    print(plain_text)
"""    


#encrypt(plain_text=text, shift_amount=shift)

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        # if letter in alphabet:
        index = alphabet.index(letter)
        index -= shift_amount
        cipher_text += alphabet[index]
    print(f"The decoded text is {cipher_text}")


decrypt(plain_text=text, shift_amount=shift)

