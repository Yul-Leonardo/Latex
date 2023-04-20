counter = 1


for i in range(4):

    if counter == 1:
        tag = input("Am welchen Tag willst du die Rechnung Erstellen (nur der Tag des Monats): ")
        monat = input("Monat: ")
        jahr = input("Jahr: ")
        tage1 = input("Wie viele Tage ging der Job: ")    
        bezeichnung1 = input("Job Bezeichnung: ")
        betrag1 = input("wie viel hast du verdient: ")
        ende = input("Zum abschließen 'q' schreiben, sonst Enter drücken um nächsten Job zu erstellen: ")
        counter = counter + 1

        if ende == "q":
            return(python_to_latex(tag, monat, jahr, tage, bezeichnung, betrag))
    elif counter == 2:
        tage2 = input("Wie viele Tage ging der Job: ")    
        bezeichnung2 = input("Job Bezeichnung: ")
        betrag2 = input("wie viel hast du verdient: ")
        ende = input("Zum abschließen 'q' schreiben, sonst Enter drücken um nächsten Job zu erstellen: ")
        counter = counter + 1

        if ende == "q":
            return(python_to_latex(tag, monat, jahr, tage, bezeichnung, betrag))


    elif counter == 3:
        tage3 = input("Wie viele Tage ging der Job: ")    
        bezeichnung3 = input("Job Bezeichnung: ")
        betrag3 = input("wie viel hast du verdient: ")
        ende = input("Zum abschließen 'q' schreiben, sonst Enter drücken um nächsten Job zu erstellen: ")
        counter = counter + 1

        if ende == "q":
            return(python_to_latex(tag, monat, jahr, tage, bezeichnung, betrag))
    elif counter == 4:
        tage4 = input("Wie viele Tage ging der Job: ")    
        bezeichnung4 = input("Job Bezeichnung: ")
        betrag4 = input("wie viel hast du verdient: ")
        ende = input("Zum abschließen 'q' schreiben, sonst Enter drücken um nächsten Job zu erstellen: ")

        if ende == "q":
            return(python_to_latex(tag, monat, jahr, tage, bezeichnung, betrag))


print(x)
print(y)