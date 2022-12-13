def text_to_ascii():

    text = input("\nType text: ")

    print("\nascii code:")
    for c in list(text):
        print(str(ord(c)), end=" ")



def ascii_to_text():
    asciitext = input("\nType ascii number: ")

    print("\nText:")
    for c in list(asciitext.split()):
        print(chr(int(c)), end="")




if __name__ == '__main__':

    opc = ""
    while opc != "exit":



        print("\n\n===================================================")
        print("                   Ascii translator")
        print("===================================================")
        print("  [1] - Text to Ascii number")
        print("  [2] - Ascii number to text")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            text_to_ascii()
        elif opc == "2":
            ascii_to_text()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")