MORSE_CODE = {'..-.': 'F', '-..-': 'X',
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}


def decodeMorse(morse):
    '''
    Simple MorseCode decoder
    INPUT
    morse: str

    OUTPUT
    message: str
    '''

    message = ''
    ls_coded_words = morse.strip().split('   ')
    for coded_word in ls_coded_words:
        ls_coded_chars = coded_word.split()
        for coded_char in ls_coded_chars:
            message += MORSE_CODE[coded_char]
        message += ' '

    return message.strip()


print(decodeMorse('.... . -.--   .--- ..- -.. .'))
#should return "HEY JUDE"
