



dic = {"a":"n", "b":"o", "c":"p", "d":"q", "e":"r", "f":"s", "g":"t", "h":"u", "i":"v", "j":"w","k":"x",
 "l":"y", "m":"z", "n":"a", "o":"b", "p":"c", "q":"d","r":"e", "s":"f", "t":"g", "u":"h", "v":"i", "w":"j", "x":"k", "y":"l", "z":"m", " ": " "}

#print(dic["a"])
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

def text_to_rot13():

    text = input("\nType text: ")

    print("\nROT13 code:")
    for c in list(text):
        if c in dic.keys():
            print(dic[c], end="")


def rot13_to_text():
    
    rot = input("\nROT13 code: ")
    
    print("\nText:")
    for c in list(rot):
        if c in dic.keys():
            print(dic[c], end="")
    



if __name__ == '__main__':

    opc = ""
    while opc != "exit":



        print("\n\n===================================================")
        print("                   ROT13 translator")
        print("===================================================")
        print("  [1] - Text to ROT13")
        print("  [2] - ROT13 to text")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            text_to_rot13()
        elif opc == "2":
            rot13_to_text()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")
            
            
    
    