import matplotlib.pyplot as plt

# Nolasīt datus no faila
filename = 'dati13.txt'
kategorija = []  # uz x ass
vertiba1 = []    # uz y ass
vertiba2 = []
vertiba3 = []

# Atvērt failu un apstrādāt katru rindiņu
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        # Noņemt liekos tukšumus un sadalīt un pielikt tukšajiem sarakstiem
        daljas = line.strip().split("%")
        if len(daljas) == 4:
            kat = daljas[0].strip()
            vert1 = int(daljas[1].strip())
            vert2 = int(daljas[2].strip())
            vert3 = int(daljas[3].strip())
            kategorija.append(kat)
            vertiba1.append(vert1)
            vertiba2.append(vert2)
            vertiba3.append(vert3)

# Aprēķināt vidējo aritmētisko vērtību katram priekšmetam
avg_vertiba1 = sum(vertiba1) / len(vertiba1)
avg_vertiba2 = sum(vertiba2) / len(vertiba2)
avg_vertiba3 = sum(vertiba3) / len(vertiba3)

# Izveidot stabiņu diagrammu ar nobīdēm katrai kategorijai
x = range(len(kategorija))  # x ass pozīcijas katrai kategorijai
width = 0.25  # Stabiņu platums

plt.figure(figsize=(10, 6))

# Katram datu kopumam nobīde uz ass
plt.bar([i - width for i in x], vertiba1, width=width, color="skyblue", label="Matemātika")
plt.bar(x, vertiba2, width=width, color="green", label="Fizika")
plt.bar([i + width for i in x], vertiba3, width=width, color="blue", label="Bioloģija")

# Pievienot līniju diagrammu ar vidējām vērtībām
plt.plot(x, [avg_vertiba1] * len(x), color="skyblue", linestyle="--", marker="o", label="Matemātika - Vidējais")
plt.plot(x, [avg_vertiba2] * len(x), color="green", linestyle="--", marker="o", label="Fizika - Vidējais")
plt.plot(x, [avg_vertiba3] * len(x), color="blue", linestyle="--", marker="o", label="Bioloģija - Vidējais")

# Pievienot ass nosaukumus un nosaukumu grafikai
plt.xlabel("Vārdi")
plt.ylabel("Vērtējumi")
plt.title("Vērtējumi matemātikā, fizikā un bioloģijā")
plt.xticks(x, kategorija)  # Piestiprināt kategoriju nosaukumus pie x ass pozīcijām
plt.legend()  # Pievienot leģendu

plt.show()
