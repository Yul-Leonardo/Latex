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

place = "Palo Alto"

with open("someplace.tex","r") as myfile:
    text = myfile.read()
    text_new = text.replace("Hello", place)

with open("someplace_new.tex", "w") as output:
    output.write(text_new)