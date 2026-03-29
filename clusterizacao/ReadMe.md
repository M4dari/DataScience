# 🔍 Clustering Algorithms Study
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Learning-green)

Este repositório documenta minha jornada de aprendizado em algoritmos de **Machine Learning Não Supervisionado**, focando em técnicas de agrupamento (Clustering).

Aqui você encontrará explicações teóricas (resumidas dos meus estudos) e implementações práticas em notebooks Jupyter.

---

## 📋 Tabela de Conteúdos
1. [Introdução](#-introdução)
2. [K-Means](#1-k-means)
3. [Spectral Clustering](#2-spectral-clustering)
4. [DBSCAN & HDBSCAN](#3-dbscan--hdbscan)
5. [Clusterização Hierárquica](#4-clusterização-hierárquica)
6. [Gaussian Mixture Models (GMM)](#5-gaussian-mixture-models-gmm)
7. [Métricas e Avaliação](#-estratégias-de-avaliação-e-definição-de-k)

---

## 🧠 Introdução

Algoritmos de aprendizado não supervisionado buscam padrões em dados não rotulados. O objetivo principal da clusterização é garantir que, baseado em algum critério, **dados mais similares estejam mais próximos entre si** do que de outros grupos.

Os critérios para agrupamento variam entre os algoritmos:
* **Densidade:** (ex: DBSCAN)
* **Distâncias/Centróides:** (ex: K-Means)
* **Conectividade em Grafos:** (ex: Spectral)

> **Aplicações:** Além de segmentação, essas técnicas são fundamentais para detecção de anomalias (outliers) e redução de dimensionalidade. Aceitam matrizes de diferentes tipos como input.

---

## 1. K-Means
O algoritmo mais clássico de clusterização baseada em centróides.

### 📖 Resumo Teórico
O K-Means divide os dados em **K** clusters pré-definidos. Ele opera iterativamente:
1.  Escolhe centróides iniciais aleatórios.
2.  Atribui cada ponto ao centróide mais próximo (menor distância Euclidiana).
3.  Recalcula a posição do centróide (média dos pontos do cluster).
4.  Repete até que os centróides estabilizem.

* **Objetivo:** Minimizar a **Inertia** (soma das distâncias quadráticas intra-cluster).
* **Pontos de Atenção:**
    * Assume que os clusters são esféricos/convexos ("bonitinhos").
    * Sensível a outliers (eles puxam a média/centróide).
    * Exige que você defina o número de clusters ($K$) antecipadamente.

[📂 Ver Prática no Notebook](./kmeans/kmeans.ipynb)

---

## 2. Spectral Clustering
Uma abordagem baseada em grafos e álgebra linear para formas complexas.

### 📖 Resumo Teórico
Ao contrário do K-Means, o Spectral Clustering não assume formas esféricas. Ele transforma a similaridade entre dados em um problema de conectividade de grafos.
1.  Cria uma **Matriz de Similaridade** (grafo onde arestas fortes = dados similares).
2.  Calcula o **Laplaciano** do grafo.
3.  Usa autovalores e autovetores para projetar os dados em um novo espaço dimensional onde clusters são mais facilmente separáveis.
4.  Aplica o K-Means nesse novo espaço.

* **Afinidade:** A escolha de como medir similaridade é crucial (`nearest_neighbors` para esparsos, `rbf` para densos).
* **Ideal para:** Clusters de formas irregulares (anéis, luas, etc).
* **Custo:** Computacionalmente caro para grandes datasets devido à decomposição de matrizes.

[📂 Ver Prática no Notebook](./SpectralClustering/spectral_clustering.ipynb)

---

## 3. DBSCAN & HDBSCAN
Clusterização baseada em densidade (sem necessidade de definir K).

### 📖 Resumo Teórico
**DBSCAN (Density-Based Spatial Clustering of Applications with Noise):**
Trabalha com dois conceitos: `eps` (raio de vizinhança) e `MinPts` (mínimo de pontos para formar um núcleo).
* Agrupa pontos densos e separa regiões esparsas.
* Classifica pontos isolados como **Ruído/Outlier** (excelente para limpeza de dados).
* Não requer número de clusters pré-definido.

**HDBSCAN (Hierarchical DBSCAN):**
Uma evolução que lida melhor com clusters de **densidades variadas**.
* Constrói uma hierarquia de clusters e usa um "score de estabilidade" para decidir o corte ideal.
* Simplifica a parametrização (frequentemente só precisa do `min_cluster_size`).

[📂 Ver Prática no Notebook](./HDBSCAN/hdbscan.ipynb)

---

## 4. Clusterização Hierárquica
Cria uma árvore de clusters (Dendrograma).

### 📖 Resumo Teórico
Pode ser **Aglomerativa (Bottom-up)**, onde cada dado começa como um cluster e vai se juntando, ou **Divisiva (Top-down)**. O resultado é um dendrograma onde o eixo Y representa a distância de fusão.

**Critérios de Ligação (Linkage):**
* `single`: Menor distância entre pontos dos grupos (tende a formar "correntes").
* `complete`: Maior distância entre pontos.
* `average`: Média das distâncias.
* `ward`: Minimiza a variância interna (só funciona com distância Euclidiana).

> **Visualização:** O corte no dendrograma define o número final de clusters. Linhas verticais longas indicam grupos bem definidos/isolados.

[📂 Ver Prática no Notebook](./hierarchical.ipynb)

---

## 5. Gaussian Mixture Models (GMM)
Uma generalização probabilística do K-Means.

### 📖 Resumo Teórico
Assume que os dados são gerados por uma mistura de distribuições Gaussianas (normais). Ao contrário do K-Means (que é "duro", 0 ou 1), o GMM atribui uma **probabilidade** de pertencimento de cada ponto a cada cluster.

* **Parâmetros:** Ajusta a Média ($\mu$) e a Covariância ($\Sigma$).
* **Tipos de Covariância:**
    * `full`: Cada cluster tem forma livre (elipses em qualquer direção).
    * `diag`: Elipses alinhadas aos eixos.
    * `spherical`: Esferas (comporta-se como K-Means).
* **Vantagem:** Lida bem com clusters sobrepostos.

[📂 Ver Prática no Notebook](./gmm.ipynb)

---

## 📊 Estratégias de Avaliação e Definição de K

Como não temos os "rótulos reais" (unsupervised), usamos métricas matemáticas para validar a qualidade da separação.

### 1. Método do Cotovelo (Elbow Method)
Utilizado principalmente no K-Means.
* Plotamos a **Inertia** (eixo Y) vs **Número de Clusters K** (eixo X).
* A inertia sempre cai conforme K aumenta. O objetivo é encontrar o ponto onde a queda desacelera bruscamente (o "cotovelo"). Isso indica que adicionar mais clusters deixou de trazer ganhos significativos de compactação.

### 2. Silhouette Score
Mede o quão parecido um ponto é com seu próprio cluster (coesão) comparado aos outros clusters (separação).
* **Range:** De -1 a +1.
* **+1:** O ponto está longe dos clusters vizinhos (Ótimo).
* **0:** O ponto está na borda de decisão (Indiferente).
* **-1:** O ponto pode ter sido atribuído ao cluster errado.
* *Útil para ajudar a definir o corte no Cluster Hierárquico e K-Means.*

### 3. Calinski-Harabasz Index
Também conhecido como critério de razão de variância.
* É a razão entre a dispersão **entre** clusters e a dispersão **dentro** dos clusters.
* **Interpretação:** Quanto maior o valor, melhor (clusters densos e bem separados). Funciona melhor para clusters convexos.

### 4. Davies-Bouldin Index
* Mede a similaridade média de cada cluster com seu cluster mais semelhante.
* **Interpretação:** Quanto **menor** o valor, melhor (indica que os clusters são distintos entre si).

### 5. Métricas Específicas
* **Dendrograma (Hierárquico):** Usamos o coeficiente de **Correlação Cofenética** para ver se a árvore preservou as distâncias originais dos dados (próximo de 1 é ideal).
* **GMM:** Usamos **AIC** (Akaike Information Criterion) e **BIC** (Bayesian Information Criterion). Ambos penalizam modelos complexos demais. Buscamos o valor **mínimo** dessas métricas para evitar overfitting.

---
*Desenvolvido como parte dos estudos em Data Science.*