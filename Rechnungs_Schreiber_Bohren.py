
n = 0

def text_einfügen():
    print("Herzlich wilkommen zu Yul's Rechnungen Ersteller!")
    print("")
    for i in range(10):
        pos = n + 1
        tag = input("Am welchen Tag willst du die Rechnung Erstellen (nur der Tag des Monats): ")
        monat = input("Monat: ")
        jahr = input("Jahr: ")
        tage = input("Wie viele Tage ging der Job: ")    
        bezeichnung0 = input("Job Bezeichnung: ")
        bezeichnung1 = bezeichnung0.replace("ö", '\\"o')
        bezeichnung2 = bezeichnung1.replace("ä", '\\"a')
        bezeichnung3 = bezeichnung2.replace("ü", '\\"u')
        bezeichnung = bezeichnung3.replace("ß", '\\ss ')

        betrag = input("wie viel hast du verdient: ")
        ende = input("Zum abschließen 'q' schreiben, sonst Enter drücken um nächsten Job zu erstellen: ")

        print(pos)
        if ende == "q":
            return(python_to_latex(tag, monat, jahr, tage, bezeichnung, betrag))

def python_to_latex(tag, monat, jahr, tage, bezeichnung, betrag):
    with open("Pdf Dateien/name_rechnung_bohren.tex","w") as file:
        file.write('\\documentclass[12pt]{article}\n')
        file.write('\\usepackage[ngerman]{babel}\n')
        file.write('\\usepackage[utf8]{inputenc}\n')
        file.write('\\usepackage[T1]{fontenc}\n')
        file.write('\\usepackage[german=guillemets]{csquotes}\n')
        file.write('\\usepackage[breaklinks=true,\n')
        file.write('colorlinks,\n')
        file.write('linkcolor=black,\n')
        file.write('citecolor=black\n')
        file.write(']{hyperref}\n')
        file.write('\\usepackage{caption}\n')
        file.write('\\usepackage{lmodern}\n')
        file.write('\\usepackage[table]{xcolor}\n')
        file.write('\\usepackage{graphicx}\n')
        file.write('\\usepackage{amsmath}\n')
        file.write('\\usepackage{listings}\n')
        file.write('\\usepackage[a4paper, total={16cm, 25cm}]{geometry}\n')
        file.write('\\usepackage{tabularray}\n')
        file.write('\\usepackage{uarial}\n')
        file.write('\\renewcommand{\\familydefault}{\sfdefault}\n')
        file.write('\\pagestyle{empty}\n')

        file.write('\n')

        file.write('\\begin{document}\n')

        file.write('\n')

        file.write('\\definecolor{lightgrey}{rgb}{0.94,0.94,0.94}\n')

        file.write('\n')

        file.write('\\begin{flushright}\n')
        file.write('\n')
        file.write('Yul Leonardo Rusch Godoy\\\ \n')
        file.write('Friesenstrase 18\\\ \n')
        file.write('10965 Berlin\\\ \n')
        file.write('Email: yulrusch@gmail.com\\\ \n')

        file.write('\n')
        file.write('\\vspace{0.5cm}\n')

        file.write('\n')
        file.write('IBAN: DE73 1001 1001 2628 6508 73\\\ \n')
        file.write('Verwendungszweck: (Rechnungsnummer)\\\ \n')
        file.write('Steuernummer: 14/501/00160\\\ \n')

        file.write('\n')
        file.write('\\end{flushright}\n')
        file.write('\\vspace{0.5cm}\n')
        file.write('\\begin{flushleft}\n')
        file.write('\n')

        file.write('\\textbf{bbr-baugrund}\\\ \n')
        file.write('Hagelbergerstra\ss e 57\\\ \n')
        file.write('10965 Berlin\\\ \n')
        file.write('030 - 43073146\\\ \n')
        file.write('0179 - 5274947\\\ \n')
        file.write('info@bbr-baugrund.de\\\ \n')

        file.write('\n')
        
        file.write('\\vspace{2cm}\n')
        file.write('\\textbf{Rechnung'+ " " + (jahr) + '\_' + (monat) + '\_' + (tag) + '}\\\ \n')
        file.write('\\vspace{0.5cm}\n')
        file.write('\n')
        
        file.write('Berlin,' + " " + (tag) + '.' + (monat) + '.' + (jahr) + '\\\ \n')
        file.write('Sehr geehrte Damen und Herren,\\\ \n')
        file.write('Ich erlaube mir, meine Dienstleistungen als Bohrhelfer,\\\ \n')
        file.write('wie folgt in Rechnung zu stellen:\\\ \n')
        file.write('\n')

        file.write('\\end{flushleft}\n')
        file.write('\\begin{flushleft}\n')
        file.write('\\begin{tabular}{c c c p{9.7cm} c}\n')
        file.write('\n')

        file.write('Pos & Tage & Einheit & Bezeichnung & Gesamt\\\ \n')
        file.write('\\rowcolor{lightgrey}\n')
        file.write('\\textbf{1.} &' + (tage) + '& Psch. &' + (bezeichnung) + " " + '(1x' +(betrag) + '\\texteuro) &' + (betrag) + " " + '\\texteuro \\\ \n')
        file.write('\\textbf{2.} & 1 & Psch. &  & \\\ \n')
        file.write('\\rowcolor{lightgrey}\n')
        file.write('\\textbf{3.} & 1 & Psch. &  & \\\ \n')
        file.write('\\textbf{4.} & 1 & Psch. &  & \\\ \n')
        file.write('\n')

        file.write('\\end{tabular}        \n')
        file.write('\\end{flushleft}\n')
        file.write('\\vspace{2cm}\n')
        file.write('\\begin{flushleft}\n')
        file.write('\\textbf{Summe: \mbox{\hspace{12.7cm}}' + (betrag) + ' \\texteuro}\n')
        file.write('\\vspace{0.2cm}\n')
        file.write('\n')

        file.write('Gem\"a\ss \ 19 UstG wird keine Umsatzsteuer berechnet.\\\ \n')
        file.write('Zahlungsziel 14 Tage ohne Abzug\\\ \n')
        file.write('\n')
        file.write('\\vspace{0.5cm}\n')
        file.write('\n')

        file.write('Mit freundlichen Gr\"u\ss en\\\ \n')
        file.write('Yul Rusch\ \n')
        file.write('\n')
        
        file.write('\\end{flushleft}\n')
        file.write('\n')

        file.write('\\end{document}\n')

print(text_einfügen())