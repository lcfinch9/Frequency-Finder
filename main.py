#### ---- SETUP ---- ####

import cipher

cipher_dict = {}
remaining_letters = []
letter_frequency = ["e", "t", "a", "i", "n", "o", "s", "h", "r", "d", "l", "u", "c", "m", "f", "w", "y", "g", "p", "b", "v", "k", "q", "j", "x", "z"]

## -- Select and encode message -- ##

original_message = cipher.get_message().lower()
encoded_message = cipher.encode_message(original_message)
cipher.sort_encoded_letters(encoded_message, remaining_letters)

print("You intercepted the following encoded message:")
print(encoded_message)

#### ---- DECODE FROM CIPHER ---- ####

def decode(encoded):
    for key, value in list(cipher_dict.items()):
        encoded = encoded.replace(key, value)
    return encoded

#### ---- ADD TO CIPHER ---- ####

def add_to_cipher(encode, actual):
    if encode in remaining_letters:
        remaining_letters.remove(encode)
    if actual in letter_frequency:
        letter_frequency.remove(actual)
    if encode not in cipher_dict:
        cipher_dict[encode] = actual

#### ---- DECODING SETUP ---- ####

## -- Decode letters in known message -- ##

dash_index = encoded_message.index("-")
key_string = encoded_message[:dash_index-2]
for i in range(len(key_string)):
    if key_string[i] != " ":
        add_to_cipher(key_string[i], original_message[i])
encoded_message = decode(encoded_message)
print("\nKnowing the message starts with the fragment \"incoming message\", you were able to partially decode the message to:")
print(encoded_message)
print("\nCapital letters represent letters that have not yet been decoded")

#### ---- USER DECODE ---- ####

while len(remaining_letters) > 0:

    ## -- Frequency analysis -- ##

    print("\n-------------------------------")
    print("The next 3 most common encoded letters are:")
    if len(remaining_letters) > 3:
        print(remaining_letters[:3])
    else:
        print(remaining_letters)
    print("Frequency analysis predicts that they may be the following letters:")
    if len(letter_frequency) > 3:
        print(letter_frequency[:3])
    else:
        print(letter_frequency)

    ## -- User guess -- ##

    user_encode = input("Enter the encoded letter you wish to guess: ").upper()
    user_actual = input("Enter the actual letter you think it is: ").lower()

    add_to_cipher(user_encode, user_actual)
    encoded_message = decode(encoded_message)
    print("\nThe encoded message is now:")
    print(encoded_message)

print()
if encoded_message == original_message:
    print("Congratulations! You cracked the code!")
else:
    print("Looks like the message isn't quite right. Here is the original message:")
    print(original_message)
