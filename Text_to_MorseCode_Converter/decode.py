from data import MORSE_CODE_DICT

class MorseCodeDecoder:
    def __init__(self):
        self.morse_dict = MORSE_CODE_DICT
        self.inverse_morse_dict  = {v: k for k, v in self.morse_dict.items()}
    
    def decode(self, morse_code):
        decode_message = []
        for code in morse_code.split():
            if code in self.inverse_morse_dict:
                decode_message.append(self.inverse_morse_dict[code])
            elif code == '/':
                decode_message.append(' ')
            else:
                raise ValueError(f"Morse code '{code}' cannot be decoded.")
        return ''.join(decode_message)