import matplotlib.pyplot as plt
import textwrap

# Dados dos tempos em segundos
tempos = [353.4, 285.5, 48.4]
labels = ['Sem otimização', 'Com otimização automática', 'Otimização automática + Otimização do código']

# Formata os rótulos com quebra de linha se necessário
labels_wrapped = [textwrap.fill(label, 15) for label in labels]

# Plot do gráfico de barras
plt.bar(labels_wrapped, tempos, color=['red', 'blue', 'green'])
plt.ylabel('Tempo (segundos)')
plt.title('Comparação de Tempos de Execução')
plt.ylim(0, max(tempos) + 50)  # Ajusta os limites do eixo y
plt.xticks(rotation=0, ha='right', fontsize=8)  # Rótulos na horizontal, alinhados à direita e tamanho de fonte reduzido

# Exibe os valores acima de cada barra
for i, valor in enumerate(tempos):
    plt.text(i, valor + 5, str(valor), ha='center')

# Exibe o gráfico
plt.tight_layout()  # Ajusta o layout para evitar que os rótulos fiquem cortados
plt.show()
