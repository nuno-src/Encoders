

def text_to_binary():
    user_input = ""
    while user_input != "0":

        user_input = input("\nType text: ")

        binary_converted = ' '.join(format(ord(i), '08b') for i in user_input)

        print(str(binary_converted))



def binary_to_text():
    user_input = ""
    while user_input != "0":

        user_input = input("\nType binary code: ")

        # text = ''.join(format(ord(i), 'g') for i in user_input)
        text = "".join(chr(int(c, 2)) for c in user_input.split(" "))

        print(str(text))









if __name__ == '__main__':

    opc = ""
    while opc != "exit":



        print("\n===================================================")
        print("                     Binary translator")
        print("===================================================")
        print("  [1] - Text to Binary")
        print("  [2] - Binary to text")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            text_to_binary()
        elif opc == "2":
            binary_to_text()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")