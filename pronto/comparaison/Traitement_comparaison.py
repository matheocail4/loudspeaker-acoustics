import os
import numpy as np
import matplotlib.pyplot as plt

# Les fichiers de donnees sont dans le meme dossier que ce script
DOSSIER = os.path.dirname(os.path.abspath(__file__))


fichier1 = open(os.path.join(DOSSIER, 'Données_2C_LI_EV.txt'), 'r', encoding='utf-8')
SPL1 = fichier1.readlines()
fichier1.close()

freq1 = []
l2CLIEV = []
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
    l2CLIEV.append(float(don[1]))

fichier2 = open(os.path.join(DOSSIER, 'Données_REC_LI_EV.txt'), 'r', encoding='utf-8')
SPL2 = fichier2.readlines()
fichier2.close()

freq2 = []
lRECLIEV = []
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
    lRECLIEV.append(float(don[1]))

fichier3 = open(os.path.join(DOSSIER, 'Données_2C_LI_FU.txt'), 'r', encoding='utf-8')
SPL3 = fichier3.readlines()
fichier3.close()

freq3 = []
l2CLIFU = []
for ligne in SPL3:
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
    freq3.append(float(don[0]))
    l2CLIFU.append(float(don[1]))

fichier4 = open(os.path.join(DOSSIER, 'Données_REC_LI_FU.txt'), 'r', encoding='utf-8')
SPL4 = fichier4.readlines()
fichier4.close()

freq4 = []
lRECLIFU = []
for ligne in SPL4:
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
    freq4.append(float(don[0]))
    lRECLIFU.append(float(don[1]))    
    

plt.plot(freq1, l2CLIEV, color='blue', label='2 cylindres (évents) : 265.92mm')
plt.plot(freq2, lRECLIEV, color='red', label='Rectangulaire (évent): 245mm')
plt.plot(freq3, l2CLIFU, color='green', label='2 cylindres (full): 265.92mm')
plt.plot(freq4, lRECLIFU, color='black', label='Rectangulaire (full): 245mm')

plt.legend(loc='best')
plt.xlabel('Fréquence en Hz')
plt.ylabel('Niveau SPL en dB')
plt.title('Comparaison du niveau SPL en fonction de la fréquence pour différentes longueurs d\'évents')
plt.xlim(0)
plt.grid()
plt.show()