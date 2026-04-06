random_forest_explicacao = """
O Random Forest é um dos algoritmos de Ensemble mais populares e amados na Ciência de Dados.
Ele utiliza a técnica de Bagging (Bootstrap Aggregating) combinada com Árvores de Decisão.

Como funciona:
1. Bootstrap: O algoritmo não treina apenas 1 árvore em todos os dados. Ele cria "K" árvores 
   diferentes. Para cada árvore, ele sorteia subconjuntos de dados do dataset original (com reposição).
2. Randomização de Features: Na hora de decidir como quebrar o nó de uma árvore, ele não olha 
   para todas as colunas. Ele sorteia apenas algumas variáveis. Isso força as árvores a serem 
   diferentes entre si e focarem em características variadas.
3. Votação (Aggregating): Para classificação, quando um novo dado chega, ele passa por todas as 
   árvores. A classe que receber mais "votos" das árvores é a decisão final do modelo.

Por que funciona tão bem?
Uma árvore de decisão sozinha tende a decorar os dados (Overfitting) ou ser muito sensível a mudanças. 
Ao juntar centenas de árvores que viram "partes" diferentes dos dados, a Floresta Aleatória anula 
os erros individuais, reduzindo drasticamente a variância do modelo.

Vantagens:
- Robusto a outliers e dados não-lineares.
- Não precisa de escalonamento/normalização das variáveis.
- Fornece nativamente a importância das variáveis (Feature Importance).
"""