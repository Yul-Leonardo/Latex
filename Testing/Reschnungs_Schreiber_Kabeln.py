import subprocess, os

n = input("n: ")
kv = {'place': n , 'month':'August'}

#print(kv['place'])

with open('someplace.tex','r') as myfile:
    text = myfile.read()

    for key, value in kv.items():
        text = text.replace('place', value)

    with open('../Pdf Dateien/someplace_new2.tex', 'w') as output:
        output.write(text)