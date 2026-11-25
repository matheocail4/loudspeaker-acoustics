import os
import numpy as np
import matplotlib.pyplot as plt

# Les fichiers de donnees sont dans le meme dossier que ce script
DOSSIER = os.path.dirname(os.path.abspath(__file__))


fichier1 = open(os.path.join(DOSSIER, 'Données_2C_200.txt'), 'r', encoding='utf-8')
SPL1 = fichier1.readlines()
fichier1.close()

freq1 = []
l200 = []
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
    l200.append(float(don[1]))

fichier2 = open(os.path.join(DOSSIER, 'Données_2C_220.txt'), 'r', encoding='utf-8')
SPL2 = fichier2.readlines()
fichier2.close()

freq2 = []
l220 = []
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
    l220.append(float(don[1]))

fichier3 = open(os.path.join(DOSSIER, 'Données_2C_2462.txt'), 'r', encoding='utf-8')
SPL3 = fichier3.readlines()
fichier3.close()

freq3 = []
l2462 = []
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
    l2462.append(float(don[1]))

fichier4 = open(os.path.join(DOSSIER, 'Données_2C_260.txt'), 'r', encoding='utf-8')
SPL4 = fichier4.readlines()
fichier4.close()

freq4 = []
l260 = []
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
    l260.append(float(don[1]))
    
    
plt.plot(freq1, l200, color='blue', label='200mm')
plt.plot(freq1, l220, color='red', label='220mm')
plt.plot(freq1, l2462, color='green', label='246.2mm')
plt.plot(freq1, l260, color='purple', label='260mm')

plt.legend(loc='best')
plt.xlabel('Fréquence en Hz')
plt.ylabel('Niveau SPL en dB')
plt.title('Comparaison du niveau SPL en fonction de la fréquence pour différentes longueurs d\'évents')
plt.xlim(0)
plt.grid()
plt.show()

l = l200[0]
for k in range(len(l200)):
    if l200[k] > l:
        l = l200[k]
        b = freq1[k]

m = l220[0]
for k in range(len(l220)):
    if l220[k] > m:
        m = l220[k]
        c = freq2[k]

n = l2462[0]
for k in range(len(l2462)):
    if l2462[k] > n:
        n = l2462[k]
        d = freq3[k]

o = l260[0]
for k in range(len(l260)):
    if l260[k] > o:
        o = l260[k]
        e = freq4[k]


def moindres_carres(x, y):
    n = len(x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    a = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
    b = mean_y - a * mean_x
    return a, b

x = np.array([b, c, d, e])
y = np.array([200, 220, 246.2, 260])

a, b = moindres_carres(x, y)

plt.scatter(x, y, color='red', label='Données')
plt.plot(x, a * x + b, color='blue', label=f'Droite de régression: y = {a:.2f}x + {b:.2f}')
plt.xlabel('Fréquence en Hz')
plt.ylabel('Longueur de l\'évent')
plt.legend(loc='best')
plt.grid()
plt.show()

print("La longueur idéale de l'évent se trouve à :", 50*a+b, "mm")