

def text_to_hexa():

    text = input("\nType text: ")

    for c in list(text):
        print(str(hex(ord(c)))[2:], end=" ")



def hexa_to_text():
    hexatext = input("\nType text: ")

    for c in list(hexatext.split()):
        print(chr(int(c, 16)), end="")




if __name__ == '__main__':

    opc = ""
    while opc != "exit":



        print("\n===================================================")
        print("                   Hexadecimal translator")
        print("===================================================")
        print("  [1] - Text to Hexadecimal")
        print("  [2] - Hexadecimal to text")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            text_to_hexa()
        elif opc == "2":
            hexa_to_text()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")