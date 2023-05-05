

#def input_checker():
    #n = str(input("Datum in (dd.mm.yyyy): "))
    #zahlen = n[0,1,3,4,6,7,8,9,10]
    #punkte = n[2,5]
    #if len(n) == 10:
        #date = True
        #if zahlen.isdigit() == True:
            #date = True
            #if punkte == '.':
                #date = True
            #else:
                #date = False
        #else:
            #date = False
    #else:
        #date = False

    #print(date)

#print(input_checker())
        


n = str(input("DATE: "))
counter = len(n)
print(counter)

for i in range(len(n)):
    word_length  = len(n)
    counter = counter - 1
    if n[counter].isdigit() == True and word_length == 10:
        print("True")
    elif n[counter] == '.' or n[counter] == '/':
        print("True")
    else:
        print("False")
        print("That input is not valid")
        break
