import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir("./tempo-maquina-2")

tamVetor = np.sort(os.listdir())

tempoExecSequential = np.array([])
tempoExecPThreads = np.array([])
tempoExecOpenMP = np.array([])

for t in tamVetor:
    with open(f"./{t}/tempos.out") as file:
        line = file.readline()
        tS = np.array([])
        tO = np.array([])
        tP = np.array([])
        while line:
            tempo = line.split(":")[1]
            if line[0] == "S":
                tS = np.append(tS, float(tempo))
            elif line[0] == "O":
                tO = np.append(tO, float(tempo))
            else:
                tP = np.append(tP, float(tempo))

            line = file.readline()

        tempoExecSequential = np.append(tempoExecSequential, np.mean(tS))
        tempoExecOpenMP = np.append(tempoExecOpenMP, np.mean(tO))
        tempoExecPThreads = np.append(tempoExecPThreads, np.mean(tP))


plt.plot(tamVetor, tempoExecSequential, 'o')
plt.plot(tamVetor, tempoExecOpenMP, 'o')
plt.plot(tamVetor, tempoExecPThreads, 'o')

plt.title("QuickSort")
plt.ylabel("Tempo")
plt.xlabel("Tamanho")
plt.show()
