KNN = """
Algoritmo de classificação que utiliza distâncias para classificar novos pontos.
Seu principal conceito é o de "vizinhos mais próximos", onde um novo ponto é classificado com base na maioria dos rótulos dos seus k vizinhos
mais próximos no espaço de características.
Ou seja, na prática, no treino não há um modelo explícito, mas sim uma estrutura de dados (geralmente uma matriz) que armazena os pontos de treinamento.
Então seu treinamento funciona apenas armazenando os dados de treinamento, sem realizar nenhum cálculo ou ajuste de parâmetros.
Durante a fase de teste, o algoritmo calcula a distância entre o ponto de teste e todos os pontos de treinamento, seleciona os k vizinhos mais próximos
 e atribui ao ponto de teste a classe mais comum entre esses vizinhos.

Os seus principais parametros são:
- n_neighbors: número de vizinhos a considerar para a classificação.
- metric: métrica de distância a ser utilizada (ex: 'euclidean', 'manhattan', 'minkowski').

E pra medir as métricas são utilizadas as principais métricas de classificação, como precision, recall e f1. Mas por ser um algoritmo muito visual
é bom também plotar seus resultados.


"""