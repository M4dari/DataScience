svm_explicacao = """
Support Vector Machine (SVM) é um modelo de aprendizado poderoso baseado em fronteiras geométricas.

O objetivo do SVM não é apenas traçar uma linha que separe as classes (como faz a Regressão Logística), 
mas sim traçar uma linha que tenha a MAIOR MARGEM possível de separação. 

Conceitos Principais:
1. Hiperplano: A linha ou plano que separa os dados. Em 2D é uma linha, em 3D é um plano.
2. Vetores de Suporte (Support Vectors): São os pontos de dados mais próximos do hiperplano. 
   Eles são os únicos pontos que importam para o algoritmo. Se você mover ou remover pontos que 
   estão longe, a fronteira não muda. A fronteira "apoia" nesses pontos críticos.
3. Margem: A distância entre o hiperplano e os vetores de suporte. O SVM busca maximizar isso.

O "Kernel Trick" (O truque do Kernel):
Quando os dados são impossíveis de separar por uma reta (não lineares, ex: formato circular), 
o SVM usa funções chamadas "Kernels" (como o RBF ou Polinomial). O Kernel mapeia os dados para 
uma dimensão superior virtualmente onde seja possível traçar um plano reto de separação, sem 
precisar fazer o cálculo real nas dimensões altas (o que custaria muita memória).

Parâmetro C (Regularização):
- C Alto (Hard Margin): Tenta classificar todos os dados de treino perfeitamente, criando uma 
  margem muito apertada. Pode gerar Overfitting e ser sensível a ruídos.
- C Baixo (Soft Margin): Permite que alguns pontos errem a classificação em troca de uma margem 
  maior e mais suave. Generaliza melhor.

Vantagens: Altamente efetivo em espaços de alta dimensionalidade e muito preciso usando os Kernels certos.
Desvantagens: Consome muita memória e CPU em datasets gigantes (>100.000 linhas) e não entrega 
probabilidades nativamente de forma tão eficiente quanto outros modelos.
"""