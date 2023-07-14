import subprocess
import re
import matplotlib.pyplot as plt

# Define o tamanho do problema (tamanho da matriz)
N = 1000

# Define a lista de números de threads

num_threads_list = [1, 2, 4, 6, 8, 10, 12]

# Armazena o tempo de execução do solver para cada número de threads
time_list = []

for num_threads in num_threads_list:
    # Executa o programa jacobi_parallel com o número de threads definido e captura a saída
    cmd = f"export OMP_NUM_THREADS={num_threads}; ./jacobi_parallel -n {N}"
    output = subprocess.check_output(cmd, shell=True)

    # Extrai o tempo de execução do solver a partir da saída com uma expressão regular
    time_str = re.search('Solver runtime\s+=\s+(\d+\.\d+)',
                         output.decode('utf-8')).group(1)
    time = float(time_str)
    time_list.append(time)

# Plota o tempo de execução do solver em função do número de threads
plt.plot(num_threads_list, time_list, 'o-')
plt.xlabel('Número de Threads')
plt.ylabel('Tempo de Execução (s)')
plt.title('Escalabilidade Forte')
plt.show()
