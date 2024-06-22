import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir("./tempo-maquina-1/")

tamVetor = np.sort(os.listdir())

tempoExecSequential = np.array([])
tempoExecPThreads = {2: np.array([]), 4: np.array([]), 8: np.array([]), 16: np.array([])}
tempoExecOpenMP = {2: np.array([]), 4: np.array([]), 8: np.array([]), 16: np.array([])}

for t in tamVetor:
    with open(f"./{t}/tempos.out") as file:
        line = file.readline()
        tS = np.array([])
        tO = {2: np.array([]), 4: np.array([]), 8: np.array([]), 16: np.array([])}
        tP = {2: np.array([]), 4: np.array([]), 8: np.array([]), 16: np.array([])}
        while line:
            tempo = line.split(":")[1]
            if line[0] == "S":
                tS = np.append(tS, float(tempo))
            elif line[0] == "O":
                if line.split(":")[0][-1] == "2":
                    tO[2] = np.append(tO[2], float(tempo))
                elif line.split(":")[0][-1] == "4":
                    tO[4] = np.append(tO[4], float(tempo))
                elif line.split(":")[0][-1] == "8":
                    tO[8] = np.append(tO[8], float(tempo))
                else:
                    tO[16] = np.append(tO[16], float(tempo))
            else:
                if line.split(":")[0][-1] == "2":
                    tP[2] = np.append(tP[2], float(tempo))
                elif line.split(":")[0][-1] == "4":
                    tP[4] = np.append(tP[4], float(tempo))
                elif line.split(":")[0][-1] == "8":
                    tP[8] = np.append(tP[8], float(tempo))
                else:
                    tP[16] = np.append(tP[16], float(tempo))

            line = file.readline()


        if len(tS) > 0:
            mediaS = np.mean(tS) 
            tempoExecSequential = np.append(tempoExecSequential, mediaS)

        if len(tO[16]) > 0 and len(tP[16]) > 0:
            mediaO = {2: np.mean(tO[2]), 4: np.mean(tO[4]), 8: np.mean(tO[8]), 16: np.mean(tO[16])}
            mediaP = {2: np.mean(tP[2]), 4: np.mean(tP[4]), 8: np.mean(tP[8]), 16: np.mean(tP[16])} 
        else:
            mediaO = {2: np.mean(tO[2]), 4: np.mean(tO[4]), 8: np.mean(tO[8])}
            mediaP = {2: np.mean(tP[2]), 4: np.mean(tP[4]), 8: np.mean(tP[8])}

        tempoExecPThreads[2] = np.append(tempoExecPThreads[2], mediaP[2])
        tempoExecPThreads[4] = np.append(tempoExecPThreads[4], mediaP[4])
        tempoExecPThreads[8] = np.append(tempoExecPThreads[8], mediaP[8])
        # tempoExecPThreads[16] = np.append(tempoExecPThreads[16], mediaP[16])

        tempoExecOpenMP[2] = np.append(tempoExecOpenMP[2], mediaO[2])
        tempoExecOpenMP[4] = np.append(tempoExecOpenMP[4], mediaO[4])
        tempoExecOpenMP[8] = np.append(tempoExecOpenMP[8], mediaO[8])
        # tempoExecOpenMP[16] = np.append(tempoExecOpenMP[16], mediaO[16])

print(f"Tempo Execução Sequencial: {tempoExecSequential}")
print(f"Tempo Execução PThreads: {tempoExecPThreads}")
print(f"Tempo Execução OpenMP: {tempoExecOpenMP}")

plt.plot(tamVetor, tempoExecSequential, label="Sequencial")
plt.plot(tamVetor, tempoExecOpenMP[2], label="OpenMP 2 Threads")
plt.plot(tamVetor, tempoExecOpenMP[4], label="OpenMP 4 Threads")
plt.plot(tamVetor, tempoExecOpenMP[8], label="OpenMP 8 Threads")
# plt.plot(tamVetor, tempoExecOpenMP[16], label="OpenMP 16 Threads")
plt.plot(tamVetor, tempoExecPThreads[2], label="PThreads 2 Threads")
plt.plot(tamVetor, tempoExecPThreads[4], label="PThreads 4 Threads")
plt.plot(tamVetor, tempoExecPThreads[8], label="PThreads 8 Threads")
# plt.plot(tamVetor, tempoExecPThreads[16], label="PThreads 16 Threads")

plt.legend()

# Calculate and print the speedup between each execution
speedupOpenMP = {2: np.array([]), 4: np.array([]), 8: np.array([]), 16: np.array([])}
speedupPThreads = {2: np.array([]), 4: np.array([]), 8: np.array([]), 16: np.array([])}

for i in range(len(tempoExecSequential)):
    speedupOpenMP[2] = np.append(speedupOpenMP[2], tempoExecSequential[i] / tempoExecOpenMP[2][i])
    speedupOpenMP[4] = np.append(speedupOpenMP[4], tempoExecSequential[i] / tempoExecOpenMP[4][i])
    speedupOpenMP[8] = np.append(speedupOpenMP[8], tempoExecSequential[i] / tempoExecOpenMP[8][i])
    # speedupOpenMP[16] = np.append(speedupOpenMP[16], tempoExecSequential[i] / tempoExecOpenMP[16][i])

    speedupPThreads[2] = np.append(speedupPThreads[2], tempoExecSequential[i] / tempoExecPThreads[2][i])
    speedupPThreads[4] = np.append(speedupPThreads[4], tempoExecSequential[i] / tempoExecPThreads[4][i])
    speedupPThreads[8] = np.append(speedupPThreads[8], tempoExecSequential[i] / tempoExecPThreads[8][i])
    # speedupPThreads[16] = np.append(speedupPThreads[16], tempoExecSequential[i] / tempoExecPThreads[16][i])

print(f"Speedup OpenMP: {speedupOpenMP}")
print(f"Speedup PThreads: {speedupPThreads}")

plt.title("BubbleSort")
plt.ylabel("Tempo")
plt.xlabel("Tamanho")
plt.show()
