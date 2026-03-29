#O Spectral Clustering é um algoritmo que utiliza cada ponto, no caso cada dado e mede/compara a sua
# similaridade, fazendo isso virar uma matriz de similaridade, com os scores de similaridade de cada
#  ponto com o restante, essa matriz diz: o quão conectado cada ponto está com todos os outros.

# E isso vira um grafo de similaridade, onde arestas e ligações maiores= são mais iguais, e falta de arestas e
#  ligações = são diferentes.
# Pra quebrar isso em "grupos" a gente usar esse tal de Laplaciano que mostra através dos menores valores
#  do autovalor (não sei o que é isso) onde vamos quebrar esses grupos de acordo com a similaridade dos 
# dados. O Laplaciano não quebra diretamente, ele revela onde o grafo quer ser quebrado

#  Depois usamos os autovetores (não sei o que é também) pra gerar novas coordenadas pros dados/pontos
# onde dados mais similares vão estar mais próximos naquele espaço, e ai aplicamos o Kmeans- que eu já 
# sei como funciona.

from sklearn.cluster import SpectralClustering

def aplicar_spectral_clustering(dados, n_clusters):
    spectral = SpectralClustering(n_clusters=n_clusters, affinity='nearest_neighbors', random_state=42)
    spectral.fit(dados)
    return spectral.labels_

# O Spectral Clustering é bom pra clusters de formas irregulares, porque ele não depende de
# suposições sobre a forma dos clusters, diferente do Kmeans que assume que os clusters são
# esféricos. No entanto, o Spectral Clustering pode sercomputacionalmente mais caro, especialmente 
# para grandes conjuntos de dados, porque envolve a construção e decomposição de matrizes grandes.
#E pode ser sensível a outliers caso eles forneçam alguma ligação errada nos grafos


#No spectral, o número de clusters pode ser estimado pelo eigengap, diferente do K-means.
#O eigengap é a diferença entre autovalores consecutivos.


#No spectral clustering, escolher a afinidade é tão importante quanto escolher o número de clusters.
# A afinidade define como a similaridade entre os pontos é calculada. As opções comuns incluem:
# 'nearest_neighbors': Constrói um grafo de vizinhança k-mais próximos. Bom para dados esparsos.
# 'rbf' (Radial Basis Function): Usa uma função gaussiana para calcular a similaridade. Bom para dados densos.
# A escolha da afinidade pode afetar significativamente os resultados da clusterização, então é importante
# experimentar diferentes opções com base na natureza dos seus dados.

#Suas métricas de avaliação do Spectral Clustering são o gap statistic, silhouette score e Davies-Bouldin index.
#O Gap Statistic compara a variabilidade dentro dos clusters com a variabilidade esperada sob uma distribuição
#  nula.
#O Silhouette Score mede o quão semelhantes os pontos são ao seu próprio cluster em comparação com outros 
# clusters.
#O Davies-Bouldin Index avalia a média da razão entre a soma das dispersões dentro dos clusters e a 
# distância entre os clusters.
#Essas métricas ajudam a determinar a qualidade da clusterização e a escolher o número ideal de clusters.

def calcular_metricas_avaliacao(dados, labels):
    from sklearn.metrics import silhouette_score, davies_bouldin_score
    import numpy as np

    silhouette = silhouette_score(dados, labels)
    davies_bouldin = davies_bouldin_score(dados, labels)

    return {
        'silhouette_score': silhouette,
        'davies_bouldin_index': davies_bouldin
    }