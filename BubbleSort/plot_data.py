import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir("./TempoMaquinaLG")

tamVetor = np.sort(os.listdir())

tempoExecSequential = np.array([])
tempoExecPThreads = np.array([])
tempoExecOpenMP = np.array([])

speedUpPThreads = np.array([])
speedUpOpenMP = np.array([])

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

        mediaS = np.mean(tS) 
        mediaO = np.mean(tO)
        mediaP = np.mean(tP) 

        tempoExecSequential = np.append(tempoExecSequential, mediaS)
        tempoExecOpenMP = np.append(tempoExecOpenMP, mediaO)
        tempoExecPThreads = np.append(tempoExecPThreads, mediaP)
       
        if mediaS > mediaP:
            speedUpPThreads = np.append(speedUpPThreads, mediaP/mediaS)
        else:
            speedUpPThreads = np.append(speedUpPThreads, mediaS/mediaP)

        if mediaS > mediaO:
            speedUpOpenMP = np.append(speedUpOpenMP, mediaO/mediaS)
        else:
            speedUpOpenMP = np.append(speedUpOpenMP, mediaS/mediaO)

print(f"Tempo Execução Sequencial: {tempoExecSequential}")
print(f"Tempo Execução PThreads: {tempoExecPThreads}")
print(f"Tempo Execução OpenMP: {tempoExecOpenMP}")
print(f'SpeedUp PThreads: {speedUpPThreads}')
print(f'SpeedUp OpenMP: {speedUpOpenMP}')


plt.plot(tamVetor, tempoExecSequential, 'o')
plt.plot(tamVetor, tempoExecOpenMP, 'o')
plt.plot(tamVetor, tempoExecPThreads, 'o')

plt.title("BubbleSort")
plt.ylabel("Tempo")
plt.xlabel("Tamanho")
plt.show()
