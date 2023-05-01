import subprocess, os

tag = input("Tag: ")
monat = input("Monat: ")
jahr = input("Jahr: ")
tage = input("Wie viele Tage hintereinander war ich arbeiten ?: ")
beschreibung = input("Die Bezeichnung/Beschreibung von meinem Job ?: ")
verdient = input("Wie viel habe ich Verdient (Tagessatz = 180Euro) ?: ")
rechnungs_nummer1 = (jahr + "\_" + monat + "\_" + tag)
rechnungs_nummer2 = (tag + "." + monat + "." + jahr)
rechnungs_name = ('Rechnung' + tag + "_" + monat + "_" + jahr)

kv = {
    'TAGE': tage,
    'BES': beschreibung, 
    'VER': verdient,
    'RN1' : rechnungs_nummer1,
    'RN2' : rechnungs_nummer2
    
    }


with open('rechnungsvorlagekabeln.tex','r') as myfile:
    text = myfile.read() 

    for key, value in kv.items():
        text = text.replace('RN1', rechnungs_nummer1)
        text = text.replace('RN2', rechnungs_nummer2)
        text = text.replace('TAGE', tage)
        text = text.replace('BES', beschreibung)
        text = text.replace('VER', verdient)

    with open(rechnungs_name + '.tex', 'w') as output:
        output.write(text)

x = subprocess.call('pdflatex' + " " + rechnungs_name + '.tex')
if x != 0:
    print('Exit-code not 0, check result!')
else:
    os.system('start' + ' ' + rechnungs_name + '.pdf')