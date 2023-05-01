import subprocess, os

#with open("sometexfile.tex","w") as file:
    #file.write("\\documentclass{article}\n")
    #file.write("\\begin{document}\n")
    #file.write("Hello Palo Alto!\n")
    #file.write("\\end{document}\n")

#x = subprocess.call("pdflatex sometexfile.tex")
#if x != 0:
    #print("Exit-code not 0, check result!")
#else:
    #os.system("start sometexfile.pdf")

#place = "Fucking Awesome"

#with open("someplace.tex","r") as myfile:
    #text = myfile.read()
    #text_new = text.replace("Hello", place)

#with open("someplace_new.tex", "w") as output:
    #output.write(text_new)


#Inputs:

#Tag       TAG
#Monat     MON
#Jahr      JAH
#Wie viele Tage hintereinander war ich arbeiten ?   TAGE
#Die Bezeichnung/Beschreibung von meinem Job ?      BES
#Wie viel habe ich Verdient (Tagessatz = 180Euro) ? VER

tag = input("Tag: ")
monat = input("Monat: ")
jahr = input("Jahr: ")
tage = input("Wie viele Tage hintereinander war ich arbeiten ?: ")
beschreibung = input("Die Bezeichnung/Beschreibung von meinem Job ?: ")
verdient = input("Wie viel habe ich Verdient (Tagessatz = 180Euro) ?: ")
rechnungs_nummer1 = (jahr + "_" + monat + "_" + tag)
rechnungs_nummer2 = (tag + "." + monat + "." + jahr)

kv = {
    'TAGE': tage,
    'BES': beschreibung, 
    'VER': verdient,
    'RN1' : rechnungs_nummer1,
    'RN2' : rechnungs_nummer2
    
    }


#print(kv['place'])

with open('Rechnungs_Vorlage_Kabeln.tex','r') as myfile:
    text = myfile.read() 

    for key, value in kv.items():
        text = text.replace('RN1', tage)
        text = text.replace('RN2', value)
        text = text.replace('TAGE', value)
        text = text.replace('BES', value)
        text = text.replace('VER', value)

    with open('../Pdf Dateien/someplace_new2.tex', 'w') as output:
        output.write(text)