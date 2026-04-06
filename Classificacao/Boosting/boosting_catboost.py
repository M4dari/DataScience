boosting_explicacao = """
Modelos de Boosting são métodos de Ensemble (combinação de múltiplos modelos) que, diferentemente 
do Bagging (Random Forest), treinam árvores de decisão de forma **sequencial**. Cada nova árvore 
é construída para corrigir os erros cometidos pelas árvores anteriores. 

O Gradient Boosting é a base técnica da maioria dos algoritmos modernos, onde o modelo usa o 
Gradiente Descendente para minimizar a função de perda iterativamente.

CatBoost (Categorical Boosting) é um algoritmo avançado desenvolvido pela Yandex. Seus grandes diferenciais são:
1. Tratamento Nativo de Categóricas: Você não precisa fazer One-Hot Encoding ou Label Encoding. 
   Basta indicar quais colunas são texto/categorias e ele resolve matematicamente usando "Target Statistics".
2. Symmetric Trees (Árvores Simétricas): Constrói árvores balanceadas onde o mesmo critério de 
   divisão é usado em todo um nível da árvore. Isso faz o modelo ser extremamente rápido na hora de 
   fazer a previsão (inferência).
3. Prevenção de Target Leakage: Usa um esquema de permutação aleatória durante o treino (Ordered Boosting) 
   que ajuda a combater fortemente o Overfitting.

Vantagens:
- Geralmente produz a melhor performance "out-of-the-box" (sem muito ajuste de hiperparâmetros).
- Incrivelmente robusto com dados tabulares complexos e categóricos.

Desvantagens:
- Mais pesado e demorado para treinar em comparação com modelos mais simples.
- Menos interpretável que uma única árvore de decisão.
"""
