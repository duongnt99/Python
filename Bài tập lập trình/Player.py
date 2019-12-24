import winsound

print("Select the mode:\n 1.Press 1 to play one file forever \n 2.Press 2 to choose many files to play  ")
mode = int(input())
if(mode == 1):
    print("Enter file name: ")
    file = input()
    while True:
        winsound.PlaySound(file+".wav", winsound.SND_ASYNC)
        print("Press Enter to continue or Press 0 to stop")
        check = input()
        if(check != ''):
            break

elif(mode == 2):
    print("Enter file name: ")
    while True:
        file = input()
        winsound.PlaySound(file+".wav", winsound.SND_ASYNC)
        print("Enter file name: ")
        if(file == ''):
            break

