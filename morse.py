

morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', " ": "/"}


reverse_morse_dict = {v: k for k, v in morse_dict.items()}

def text_to_morse():

    try:
        msg = input("Insert a message: ")

        msg = " ".join(morse_dict[c] for c in msg.upper())
    except:
        print("ERRO! - Insira apenas caracteres e numeros e não use acentos")
    else:
        print("\nMessage: ", msg)



def morse_to_text():
   
    try:
        morse_code = input("Insert morse code: ")
        reverse_msg = "".join(reverse_morse_dict[c] for c in morse_code.split(" "))

    except:
        print("ERRO! - Insira apenas caracteres e numeros e não use acentos")
    else:
        print("\nMessage: ", reverse_msg)


if __name__ == '__main__':

    opc = ""
    while opc != "exit":



        print("\n===================================================")
        print("                     Morse translator")
        print("===================================================")
        print("  [1] - Text to Morse")
        print("  [2] - Morse to text")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            text_to_morse()
        elif opc == "2":
            morse_to_text()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")

