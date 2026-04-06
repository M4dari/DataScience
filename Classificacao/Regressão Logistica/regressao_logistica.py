regressao_logistica_explicacao = """
Apesar do nome "Regressão", este é um algoritmo fundamental de CLASSIFICAÇÃO.

A base matemática é parecida com a da Regressão Linear (uma reta calculando pesos: y = wX + b), 
porém a Regressão Logística pega o resultado dessa reta e passa por uma função matemática chamada 
Função Sigmoide (curva em formato de "S").

A Função Sigmoide mapeia qualquer número real (de menos infinito a mais infinito) para um valor 
entre 0 e 1. Com isso, o algoritmo retorna não um número absoluto, mas sim uma PROBABILIDADE.
- Se a probabilidade for > 0.5, a classe prevista é 1.
- Se for < 0.5, a classe prevista é 0.

Para medir os erros (Loss Function) e ajustar os pesos usando o Gradiente Descendente, ela utiliza a 
Log Loss (Binary Cross-Entropy), que pune fortemente o modelo quando ele está muito confiante de uma 
previsão errada.

Vantagens:
- É um modelo simples, ultra rápido e fácil de interpretar (pesos maiores = maior importância).
- Entrega probabilidades reais confiáveis, não apenas a classe final.

Desvantagens:
- Constrói fronteiras de decisão estritamente LINEARES. Se o seu problema for muito complexo 
  e os dados não puderem ser separados por uma reta/hiperplano, a acurácia será ruim.
"""