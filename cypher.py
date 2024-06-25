# TODO-9: Import and print the logo from art.py when the program starts.
from logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(message, shift_amount):
#     coded_message = ''
#     # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     # e.g.
#     # plain_text = "hello"
#     # shift = 5
#     # cipher_text = "mjqqt"
#     # print output: "The encoded text is mjqqt"
#     for letter in message:
#         if letter not in alphabet:
#             coded_message += letter
#         if letter in alphabet:
#             print(letter, 'letter')
#             code = alphabet.index(letter) + shift_amount
#             coded_message += alphabet[code]
#             print(code)
#     print(coded_message)


# TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decode(message, shift_amount):
#     # TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#     # e.g.
#     # cipher_text = "mjqqt"
#     # shift = 5
#     # plain_text = "hello"
#     # print output: "The decoded text is hello"
#     coded_message = ''
#     for letter in message:
#         if letter not in alphabet:
#             coded_message += letter
#
#         if letter in alphabet:
#             print(letter, 'letter')
#             code = alphabet.index(letter) - shift_amount
#             coded_message += alphabet[code]
#             print(code)
#     print(coded_message)
#     return coded_message


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == "decode":
#     decode(text, shift)
# else:
#     print('Wrong')

# TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar().
def ceaser(message, shift_number, direction_type):
    result = ''

    for letter in message:
        if letter in alphabet:
            if direction_type == 'decode':
                print(letter, 'letter')
                code = alphabet.index(letter) - shift_number
                result += alphabet[code]
                print(code)
            elif direction_type == 'encode':
                code = alphabet.index(letter) + shift_number
                result += alphabet[code]
            else:
                print('Something went wrong!')

    print(f"The {direction_type}d message is {result}")


# TODO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceaser(text, shift, direction)


# TODO-12: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

# TODO-11: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"
# TODO-10: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).