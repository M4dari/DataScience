# 📈 Regression Algorithms Study
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Learning-green)

Este repositório documenta minha jornada de aprendizado em algoritmos de **Machine Learning Supervisionado**, focando em técnicas de **Regressão**.

Aqui você encontrará explicações teóricas detalhadas e implementações práticas em scripts focados em prever valores numéricos contínuos.

---

## 📋 Tabela de Conteúdos
1. [Introdução](#-introdução)
2. [Regressão Linear e Gradiente Descendente](#1-regressão-linear-e-gradiente-descendente)
3. [Regularização L1 (Lasso)](#2-regularização-l1-lasso)
4. [Regularização L2 (Ridge)](#3-regularização-l2-ridge)
5. [ElasticNet](#4-elasticnet)
6. [Métricas e Avaliação](#-estratégias-de-avaliação-em-regressão)

---

## 🧠 Introdução

O objetivo da regressão é prever um valor numérico contínuo ($y$) encontrando a melhor relação matemática entre os dados de entrada ($x$) e a saída esperada. O modelo busca traçar uma linha (ou hiperplano) que minimize a distância entre o que ele previu e o valor real (o Erro).

Enquanto na Classificação buscamos separar as categorias, na Regressão nosso foco principal é entender a **tendência** e **magnitude** dos dados numéricos.

---

## 1. Regressão Linear e Gradiente Descendente
A base matemática dos modelos preditivos contínuos.

### 📖 Resumo Teórico
A fórmula base é $y = w * x + b$, onde $w$ representa os pesos (importância de cada feature) e $b$ o viés (ponto de partida). O processo de aprendizado ocorre em três passos:
1. **Predição (Forward Pass):** Cálculo com pesos atuais.
2. **Cálculo da Perda (Loss):** Medição do erro (ex: MSE).
3. **Otimização (Gradiente Descendente):** Onde o modelo ajusta os pesos indo na direção oposta ao gradiente para encontrar o ponto de erro mínimo.

> **Atenção:** O **Learning Rate** dita o tamanho do passo na descida do gradiente. Valores altos causam divergência, valores muito baixos lentificam o treino. Em larga escala, usamos o **SGD (Gradiente Descendente Estocástico)** para acelerar o processo.

[📂 Ver Prática no Script](./regressao_linear/regressao_linear.ipynb)

---

## 2. Regularização L1 (Lasso)
Técnica de regressão linear que realiza seleção automática de features.

### 📖 Resumo Teórico
O modelo Lasso (Least Absolute Shrinkage and Selection Operator) adiciona uma penalidade à função de custo equivalente ao **valor absoluto** da magnitude dos coeficientes.
* **Formato Geométrico:** O contorno de restrição é um poliedro (diamante) com quinas afiadas.
* **Vantagem:** Essa geometria promove a "esparsidade", ou seja, é capaz de **zerar completamente** os pesos de variáveis que não são importantes. É excelente para *Feature Selection* e lidar com datasets com colunas desnecessárias.
* **Desvantagem:** Se existirem variáveis altamente correlacionadas, o Lasso escolhe uma aleatoriamente e zera as demais, o que pode causar instabilidade.

[📂 Ver Prática no Script](./L1_Lasso/lasso.ipynb)

---

## 3. Regularização L2 (Ridge)
Controle de pesos e combate robusto à multicolinearidade e overfitting.

### 📖 Resumo Teórico
A Regressão Ridge adiciona uma penalidade à Loss Function baseada no **quadrado dos pesos ($w^2$)**: `Loss = MSE + Alpha * (w1² + w2² + ... + wn²)`.
* O hiperparâmetro **Alpha** controla a força da restrição. Ridge cobra "caro" por pesos muito altos, forçando o modelo a distribuir a responsabilidade entre as variáveis (encolhimento dos pesos, ou *shrinkage*).
* **Vantagem:** Lida excepcionalmente bem com multicolinearidade (variáveis preditoras correlacionadas). O contorno de restrição é circular/hiperesférico, então ele nunca zera um coeficiente, apenas o reduz a valores próximos de zero.

[📂 Ver Prática no Script](./L2_Ridge/Ridge.ipynb)

---

## 4. ElasticNet
O equilíbrio perfeito entre a restrição do Lasso e a estabilidade da Ridge.

### 📖 Resumo Teórico
O ElasticNet minimiza uma função de custo que combina as penalidades L1 e L2: `J(w) = MSE(w) + λ₁|w|₁ + λ₂|w|₂²`.

* **Efeito de Agrupamento (Grouping Effect):** Diferente do Lasso que zera uma das variáveis correlacionadas, a convexidade estrita fornecida pela parte Ridge no ElasticNet força estabilidade, mantendo ambas as variáveis no modelo com pesos divididos/similares.
* **Geometria:** O contorno é uma 'esfera-diamante' (*convex hull*). Tem quinas para zerar o que é irrelevante, mas as bordas são convexas para lidar suavemente com correlação.
* **Quando usar:** Principalmente quando o número de features ($p$) é maior que o número de observações ($n$), ou sob forte multicolinearidade.

[📂 Ver Prática no Script](./ElasticNet/ElasticNet.ipynb)

---

## 📊 Estratégias de Avaliação em Regressão

Diferente da classificação (onde avaliamos acertos percentuais), na regressão medimos "o quão longe" nossas previsões estão da realidade contínua.

### 1. MSE (Erro Quadrático Médio)
* Penaliza erros grandes de forma quadrática. Se o modelo errar muito em um ponto (outlier), o MSE "grita" elevando o erro ao quadrado.
* Difícil interpretação direta, pois altera a unidade de medida (ex: reais para reais ao quadrado).

### 2. RMSE (Raiz do Erro Quadrático Médio)
* É a raiz quadrada do MSE. Retorna o erro à unidade de medida original dos dados, mantendo a penalidade severa contra grandes desvios/outliers.

### 3. MAE (Erro Absoluto Médio)
* Média das diferenças absolutas entre as previsões e valores reais.
* Menos sensível a outliers comparado ao MSE/RMSE. Excelente para entender o erro médio "puro" de forma linear.

### 4. R² (Coeficiente de Determinação)
* Métrica relativa que indica a **proporção da variância** na variável dependente que é explicada pelo modelo.
* **Range:** Normalmente vai de 0 a 1 (1.0 indica que o modelo previu tudo perfeitamente). Pode ser negativo se o modelo for pior que simplesmente chutar a média geral.

### 5. Análise de Resíduos
* Estudo direto das diferenças (erros). Em um modelo bem ajustado, os resíduos devem ser distribuídos aleatoriamente ao redor de zero (homocedasticidade), provando que não há viés ou padrão oculto que o modelo deixou escapar.

---
*Desenvolvido como parte dos estudos em Data Science.*
