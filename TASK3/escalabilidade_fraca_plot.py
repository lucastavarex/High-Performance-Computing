import subprocess
import re
import matplotlib.pyplot as plt

# Define o número de threads fixo
num_threads = 4

# Define a lista de tamanhos de matriz
matrix_sizes = [500, 1000, 1500, 2000, 2500]

# Armazena o tempo de execução do solver e a quantidade de trabalho por processador para cada tamanho de matriz
time_list = []
work_per_thread_list = []

for matrix_size in matrix_sizes:
    # Executa o programa jacobi_parallel com o tamanho de matriz definido e o número de threads fixo
    cmd = f"export OMP_NUM_THREADS={num_threads}; ./jacobi_parallel -n {matrix_size}"
    output = subprocess.check_output(cmd, shell=True)

    # Extrai o tempo de execução do solver a partir da saída com uma expressão regular
    time_str = re.search('Solver runtime\s+=\s+(\d+\.\d+)',
                         output.decode('utf-8')).group(1)
    time = float(time_str)

    # Calcula a quantidade de trabalho por processador (threads)
    work_per_thread = matrix_size**2 / num_threads

    # Armazena o tempo de execução e a quantidade de trabalho por processador na lista correspondente
    time_list.append(time)
    work_per_thread_list.append(work_per_thread)

# Plota o tempo de execução em função do tamanho da matriz
plt.plot(matrix_sizes, time_list, 'o-')
plt.xlabel('Tamanho da Matriz')
plt.ylabel('Tempo de Execução (s)')
plt.title('Escalabilidade Fraca')
plt.show()
