from encode import MorseCodeEncoder
from decode import MorseCodeDecoder

ask_user = input("Would you like to (e)ncode or (d)ecode a message? ").lower()

try:
    if ask_user == 'e':
        message = input("Enter the message to encode: ")
        encoder = MorseCodeEncoder()
        encoded_message = encoder.encode(message=message)
        print(f"Encoded Morse Code: {encoded_message}")

    elif ask_user == 'd':
        morse_code = input("Enter the Morse Code to decode (use spaces between codes): ")
        decoder = MorseCodeDecoder()
        decoded_message = decoder.decode(morse_code=morse_code)
        print(f"Decoded Message: {decoded_message}")

    else:
        print("Invalid option. Please enter 'e' to encode or 'd' to decode.")

except ValueError as e:
    print(e)
