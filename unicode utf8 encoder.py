

# encode text to \xnn format

my_string = "\x68\x65\x6c\x6c\x6f"
print(my_string)




#Transformar a frase em bytes
#b = bytes(frase, 'UTF-8')


#text = input("\nType text: ")
#
#print("\nascii code:")
#for c in list(text):
#    print(str(chr((ord(c)))), end=" ")
#
#print(ord(text))
#print(chr(40960).encode('utf-8'))
#print(chr(97).encode('utf-8'))
#print(text.encode('utf-8'))
#
#b = bytes(text, 'UTF-8')
#print(b.decode('utf-8'))
#
#print(chr(ord(text)).encode('utf-8'))
#print(frase.encode('ascii', 'backslashreplace'))

def text_to_hexa():

    text = input("\nType text: ")

    print("\nHexadecimal code:")
    for c in list(text):
        print("\\x", end="")
        print(str(hex(ord(c)))[2:].upper(), end="") 



text_to_hexa()



