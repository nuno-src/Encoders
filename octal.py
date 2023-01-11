

def text_to_octal():

    text = input("\nType text: ")

    print("\nOctal code:")
    for c in list(text):
        print(str(oct(ord(c)))[2:], end=" ")



def octal_to_text():
    hexatext = input("\nType Octal code: ")

    print("\nText:")
    for c in list(hexatext.split()):
        print(chr(int(c, 8)), end="")




if __name__ == '__main__':

    opc = ""
    while opc != "exit":



        print("\n\n===================================================")
        print("                   Octal translator")
        print("===================================================")
        print("  [1] - Text to Octal")
        print("  [2] - Octal to text")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            text_to_octal()
        elif opc == "2":
            octal_to_text()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")