import string as s


def caesar_cipher():
    while True:
        message = input('Enter Message to Encrypt : ')
        message_shift = int(input('Enter Number to Shift : '))

        if message_shift > 25 or message_shift < 1 :
            raise("Invalid, message shift must be lower than 25 and greater than 0")
        else:
            alphabet_list = s.ascii_letters
            shifted_alphabet_list = alphabet_list[message_shift:] + alphabet_list[:message_shift]
            table_res = str.maketrans(alphabet_list, shifted_alphabet_list)

            encypt_message = message.translate(table_res)

            split_mess = encypt_message.lower().split(' ')
        return print(f"{''.join(split_mess)}")


caesar_cipher()