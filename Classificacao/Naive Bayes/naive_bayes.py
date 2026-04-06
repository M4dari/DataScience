naive_bayes = """
O Naive Bayes é um algoritmo de classificação probabilístico rápido e poderoso, fundamentado 
no Teorema de Bayes. Ele calcula a probabilidade de um dado pertencer a uma determinada classe, 
dado os valores de suas características (features).

A principal característica e o motivo do nome "Ingênuo" (Naive) é a sua forte suposição matemática: 
o algoritmo assume que todas as características são condicionalmente independentes entre si, 
dada a classe. Ou seja, a presença de uma característica não afeta a presença de outra. 
Mesmo que essa suposição raramente seja 100% verdadeira no mundo real (ex: em um texto, a palavra 
"muito" costuma vir acompanhada de um adjetivo), o algoritmo funciona surpreendentemente bem na prática.

A equação baseada no Teorema de Bayes é: P(A|B) = [P(B|A) * P(A)] / P(B)
- Onde queremos descobrir a probabilidade da classe A acontecer, dado que os dados B ocorreram.

Existem variações do Naive Bayes no Scikit-Learn adaptadas para diferentes tipos de dados:
Modelo	        Tipo de Dado	            Exemplo Clássico
GaussianNB	    Contínuo (Real)	            Iris dataset (tamanho de pétalas)
MultinomialNB	Contagem (Inteiro)	        Frequência de palavras em e-mails
BernoulliNB	    Binário (0 ou 1)	        Presença/Ausência de termos
CategoricalNB	Categórico	                Tipo de solo, Marca de carro
ComplementNB	Contagem (Desbalanceado)	Fraudes bancárias (casos raros)

Principais Vantagens:
- É extremamente rápido, tanto na fase de treinamento quanto na de previsão.
- Lida excepcionalmente bem com alta dimensionalidade (como textos com milhares de palavras diferentes).
- Precisa de relativamente poucos dados de treinamento para estimar os parâmetros com precisão.
- Fornece probabilidades como saída, não apenas a classe final, ajudando na análise de incerteza.
"""