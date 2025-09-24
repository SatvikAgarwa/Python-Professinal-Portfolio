from data import MORSE_CODE_DICT

class MorseCodeEncoder:
    def __init__(self):
        self.morse_code_dict = MORSE_CODE_DICT
    
    def encode(self, message):
        encoded_message = []
        for char in message.upper():
            if char in self.morse_code_dict:
                encoded_message.append(self.morse_code_dict[char])
            else:
                raise ValueError(f"Character '{char}' cannot be encoded in Morse code.")
        return ' '.join(encoded_message)