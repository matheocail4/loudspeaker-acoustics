import os
import numpy as np
import matplotlib.pyplot as plt

# Les fichiers de donnees sont dans le meme dossier que ce script
DOSSIER = os.path.dirname(os.path.abspath(__file__))


fichier1 = open(os.path.join(DOSSIER, 'Données_4C_818.txt'), 'r', encoding='utf-8')
SPL1 = fichier1.readlines()
fichier1.close()

freq1 = []
l818 = []
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
    l818.append(float(don[1]))

fichier2 = open(os.path.join(DOSSIER, 'Données_4C_90.txt'), 'r', encoding='utf-8')
SPL2 = fichier2.readlines()
fichier2.close()

freq2 = []
l90 = []
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
    l90.append(float(don[1]))

fichier3 = open(os.path.join(DOSSIER, 'Données_4C_100.txt'), 'r', encoding='utf-8')
SPL3 = fichier3.readlines()
fichier3.close()

freq3 = []
l100 = []
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
    l100.append(float(don[1]))

fichier4 = open(os.path.join(DOSSIER, 'Données_4C_110.txt'), 'r', encoding='utf-8')
SPL4 = fichier4.readlines()
fichier4.close()

freq4 = []
l110 = []
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
    l110.append(float(don[1]))
    
    
plt.plot(freq1, l818, color='blue', label='81.8mm')
plt.plot(freq1, l90, color='red', label='90mm')
plt.plot(freq1, l100, color='green', label='100mm')
plt.plot(freq1, l110, color='purple', label='110mm')

plt.legend(loc='best')
plt.xlabel('Fréquence en Hz')
plt.ylabel('Niveau SPL en dB')
plt.title('Comparaison du niveau SPL en fonction de la fréquence pour différentes longueurs d\'évents')
plt.xlim(0)
plt.grid()
plt.show()

l = l818[0]
for k in range(len(l818)):
    if l818[k] > l:
        l = l818[k]
        b = freq1[k]

m = l90[0]
for k in range(len(l90)):
    if l90[k] > m:
        m = l90[k]
        c = freq2[k]

n = l100[0]
for k in range(len(l100)):
    if l100[k] > n:
        n = l100[k]
        d = freq3[k]

o = l110[0]
for k in range(len(l110)):
    if l110[k] > o:
        o = l110[k]
        e = freq4[k]


def moindres_carres(x, y):
    n = len(x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    a = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
    b = mean_y - a * mean_x
    return a, b

x = np.array([b, c, d, e])
y = np.array([81.8, 90, 100, 110])

a, b = moindres_carres(x, y)

plt.scatter(x, y, color='red', label='Données')
plt.plot(x, a * x + b, color='blue', label=f'Droite de régression: y = {a:.2f}x + {b:.2f}')
plt.xlabel('Fréquence en Hz')
plt.ylabel('Longueur de l\'évent')
plt.legend(loc='best')
plt.grid()
plt.show()

print("La longueur idéale de l'évent se trouve à :", 50*a+b, "mm")