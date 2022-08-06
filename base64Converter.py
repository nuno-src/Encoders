import base64




def text_to_base64():

    text = input("\nInsira a mensagem: ")
    b_text = text.encode()
    b64_text = base64.b64encode(b_text)

    print(b64_text.decode('UTF-8'))


def base64_to_text():

    b64_text = input("\nInsira a mensagem(base64): ")
    b_text = base64.b64decode(b64_text)
    text = b_text.decode()

    print(text)



if __name__ == '__main__':

    opc = ""
    while opc != "exit":



        print("\n===================================================")
        print("                     Base64 translator")
        print("===================================================")
        print("  [1] - Text to Base64")
        print("  [2] - Base64 to text")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            text_to_base64()
        elif opc == "2":
            base64_to_text()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")