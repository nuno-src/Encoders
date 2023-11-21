

def text_to_hexa():

    text = input("\nType text: ")

    print("\nHexadecimal code:")
    for c in list(text):
        print(str(hex(ord(c)))[2:].upper(), end=" ")



def hexa_to_text():
    hexatext = input("\nType Hexadecimal code: ")

    print("\nText:")
    for c in list(hexatext.split()):
        print(chr(int(c, 16)), end="")


def decimal_to_hex():
    decimalt = 1
    while decimalt != 0:
    
        try:
            decimalt = int(input("\nType decimal numbers: "))

            print("\nHexadecimal code:", hex(decimalt)[2:].upper())
            print("\nPress 0 to exit")
        except:
            print("Insira apenas numeros!")
  


def hex_to_decimal():
    hexat = ""
    while hexat != "0":
        
        hexat = input("\nType Hexadecimal code: ")
        dec_output = str(int(hexat, 16))
        print("\nDecimal :", dec_output)
        print("Press 0 to exit")
    




if __name__ == '__main__':

    opc = ""
    while opc != "exit":



        print("\n\n===================================================")
        print("                   Hexadecimal translator")
        print("===================================================")
        print("  [1] - Text to Hexadecimal")
        print("  [2] - Hexadecimal to text")
        print("  [3] - Decimal to Hex")
        print("  [4] - Hex to Decimal")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            text_to_hexa()
        elif opc == "2":
            hexa_to_text()
        elif opc == "3":   
            decimal_to_hex()
        elif opc == "4":   
            hex_to_decimal()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")
            
            
            
            
            