#1. feladat

utolso_het_szamai = []

for i in range(5):
    utolso_het_szamai.append(input(f"Utolsó hét {i+1}. száma:")+" ")

#2. feladat

utolso_het_szamai.sort()

print("A számok növekvő sorrendben: ", end ="")

for elemek in range(len(utolso_het_szamai)):
    print(utolso_het_szamai[elemek], end="")

# 3. feladat

bekert_egy_szam = input("\nAdjon meg egy egész számot 1 és 50 között: ")

txt = open(r'..\scratches\lottosz.dat', 'r')

for i in range(int(bekert_egy_szam)):
    sor = txt.readline()

#4. feladat

print(f"{bekert_egy_szam}. hét számai: {sor}")

txt.close()

#5. feladat

kilencven_szam = []

for i in range(90):
    kilencven_szam.append(i+1)

txt = open(r'..\scratches\lottosz.dat', 'r')
osszes_kihuzott = []
sor = txt.readline()
van = False

while sor != "":
    for i in range(5):
        osszes_kihuzott.append(sor.split()[i])
    sor = txt.readline()

nem_kihuzottak = []

for i in range(90):
    if str(kilencven_szam[i]) not in osszes_kihuzott:
        van = True
        nem_kihuzottak.append(i+1)

if van:
    print("Van olyan szám, melyet egyszer sem húztak ki.")
if not van:
    print("Nincs olyan szám, melyet egyszer sem húztak ki.")

txt.close()

#6. feladat

paratlan = 0

for i in range(len(osszes_kihuzott)):
    if int(osszes_kihuzott[i]) % 2 != 0:
        paratlan += 1

print("Páratlanok száma: ", paratlan)

#7. feladat

txt = open(r'..\scratches\lottosz.dat', 'r')
osszes_kihuzott_fajlba = []
sor = txt.readline()

while sor != "":

    osszes_kihuzott_fajlba.append(sor)
    sor = txt.readline()

lotto52 = open(r'..\scratches\lotto52.dat', 'w')

lotto52.write("".join(osszes_kihuzott_fajlba))
lotto52.write("\n")
lotto52.write("".join(utolso_het_szamai))

txt.close()
lotto52.close()

#8. feladat
"""
osszes_kihuzott.sort()

print(osszes_kihuzott)
for i in range(len(osszes_kihuzott)):
    print(osszes_kihuzott.count(str(i+1)), end =" ")
"""
#9. feladat

primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
print(f"\nA prímek melyeket nem húztak ki: ")
for i in range(len(nem_kihuzottak)):
    if int(nem_kihuzottak[i]) in primek:
        print(f"{nem_kihuzottak[i]}", end=" ")