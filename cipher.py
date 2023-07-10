import random

messages = [
    "Incoming message - The job is done, and the client has recieved the goods. A fake message has been sent and intercepted by the authorities as planned. Lucy will be reaching out to give you the details for next week's task.",
    "Incoming message - Requesting additional backup for the upcoming job. Security has tripled since last time, and they may have already found out about the plan. I'll let you know if I find out more",
    "Incoming message - Request for a new message encoding method is denied. Our current code is way too strong to be cracked. It took me long enough to come up with this one, and I don't want to have to do that again.",
    "Incoming message - Heard of a potential big job, and will be sending Henry over to scout out the place. If this is as good as it sounds we may be set for life. I'll send you location information",
]

def get_message():
    return random.choice(messages)

def encode_message(message):
    code_options = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letter_options = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    random.shuffle(letter_options)
    for i in range(len(letter_options)):
        message = message.replace(letter_options[i], code_options[i])
    return message

def sort_encoded_letters(encoded_message, remaining_letters):
    letter_count = {}
    for letter in encoded_message:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    del letter_count[" "]
    del letter_count[","]
    del letter_count["."]
    del letter_count["'"]
    del letter_count["-"]
    while len(letter_count) > 0:
        for letter, count in letter_count.items():
            current_max = max(letter_count.values())
            if count == current_max:
                remaining_letters.append(letter)
                del letter_count[letter]
                break
