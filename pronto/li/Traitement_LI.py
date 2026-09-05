import os
import numpy as np
import matplotlib.pyplot as plt


fichier1 = open('/Users/matheocail/Desktop/1A/PRONTO/LI/Données_2C_LI.txt', 'r') #À changer selon qui utilise le programme
SPL1 = fichier1.readlines()
fichier1.close()

freq1 = []
l2CLI = []
for ligne in SPL1:
    m = list(ligne)
    m.pop()
    for i in range(len(m)-1):
        if i <= len(m)-1 and m[i] == ' ':
            if i == 0:
                k = i
                while m[k] == ' ':
                        k += 1
                m = m[k:]
            else:
                a = 0
                k = i
                while m[k] == ' ':
                        k += 1
                        a += 1
                m = m[:i] + [";"] + m[i+a:]
    z = ''
    for k in range(len(m)):
        z += m[k]
    don = z.strip().split(';')
    freq1.append(float(don[0]))
    l2CLI.append(float(don[1]))

fichier2 = open('/Users/matheocail/Desktop/1A/PRONTO/LI/Données_4C_LI.txt', 'r') #À changer selon qui utilise le programme
SPL2 = fichier2.readlines()
fichier2.close()

freq2 = []
l4CLI = []
for ligne in SPL2:
    m = list(ligne)
    m.pop()
    for i in range(len(m)-1):
        if i <= len(m)-1 and m[i] == ' ':
            if i == 0:
                k = i
                while m[k] == ' ':
                        k += 1
                m = m[k:]
            else:
                a = 0
                k = i
                while m[k] == ' ':
                        k += 1
                        a += 1
                m = m[:i] + [";"] + m[i+a:]
    z = ''
    for k in range(len(m)):
        z += m[k]
    don = z.strip().split(';')
    freq2.append(float(don[0]))
    l4CLI.append(float(don[1]))

    
plt.plot(freq1, l2CLI, color='blue', label='265.92mm')
plt.plot(freq1, l4CLI, color='red', label='89.72mm')

plt.legend(loc='best')
plt.xlabel('Fréquence en Hz')
plt.ylabel('Niveau SPL en dB')
plt.title('Comparaison du niveau SPL en fonction de la fréquence pour différentes longueurs d\'évents')
plt.xlim(0)
plt.grid()
plt.show()