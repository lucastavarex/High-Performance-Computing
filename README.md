
# High Performance Computing
Diretório destinado às atividades do curso de Computação de Alto Desempenho @UFRJ - Engenharia de Computação e Informação


## TASK1

- O primeiro trabalho consiste na implementação de um código que realize as devidas
operações para realização do produto matriz - vetor, A · x = b. A implementação deverá ser feita nas linguagens C e Fortran (deve-se fazer a implementação nas duas linguagens,
e não apenas optar por uma).

                   
- O objetivo ́e investigar como a performance do código é afetada ao mudar a ordem
com que os loops aninhados são realizados nas duas linguagens. Isto deve ser feito para
diversos tamanhos de sistemas.

- Estime o tamanho máximo dos arranjos A, x e b que podem ser alocados no seu
sistema para realização da tarefa ;


- Os arranjos a serem utilizados durante as operações devem ser inicializados com
números aleátorios (A e x no caso acima)               


- Comece com um problema de tamanho pequeno e tente chegar ao tamanho máximo estimado no item 1. Contabilize o tempo para realiza ̧ca ̃o das opera ̧co ̃es para todos
os tamanhos de sistema e para ambas as ordens de execução dos loops


- Apresente curvas mostrando o tempo de execução para cada dimensão do problema
e relacione estas curvas a` complexidade computacional do produto matriz - vetor
(O(n2)

## TASK2

Usando o programa para a solução de um sistema de equações lineares pelo método iterativo de Jacobi, faça:

```
https://github.com/UoB-HPC/intro-hpc-jacobi/blob/master/jacobi.c
```

- Compile e execute o programa para pelo menos 3 tamanhos de matrizes (objetivo - obter tempos significativos, pelo menos da ordem de minutos, para ficar mais fácil ver os efeitos das otimizações) e escolha 1 tamanho para prosseguir
- Recompile e execute o programa com otimização automática 
- Execute a perfilagem do programa usando o gprof ou o Intel VTune
- Analise o resultado da perfilagem
- De posse dos resultados de sua análise, tente 1 ação de otimização 
- Compare os tempos das versões (inicial, com otimização automática, e após perfilagem)
- Faça um relatório descrevendo a sua experiência

## TASK3

- Selecione o loop onde esta a maior parte do trabalho no programa que voces usaram para o mini-projeto de perfilagem;
- Gere um grafico do roofline para esse loop usando uma ferramenta adequada.

## TASK4

- Utilizando o código a seguir, pede-se:

```
https://github.com/UoB-HPC/intro-hpc-jacobi/blob/master/jacobi.c
```

- Identifique os trechos que possam ser paralelizados com o OpenMP
- Compile e execute o programa paralelo otimizado para varias threads 
- Faca os gráficos de escalabilidade forte (tamanho do problema fixo, aumentando o número de threads) e escalabilidade fraca (aumentando o tamanho do problema e o número de threads)
- Faca um relatório descrevendo a sua experiência
                   
