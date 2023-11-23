

letters = list("abcdefghijklmnopqrstuvwxyz")


text = input("\nType numbers code: ")

try:
    ftext = text.split('-')
    #print(ftext)


    for i in list(ftext):
        
        print(letters[int(i)-1], end="")
        
except:
    print("ERROR - Type numbers between 1-26 and use '-' to split ")

