from sklearn.cluster import KMeans


#O algoritmo escolhido foi o Kmeans, que divide os dados em K clusters, onde K é um número
# pré-definido pelo usuário. O algoritmo funciona iterativamente para atribuir cada ponto de dados
# ao cluster mais próximo com base na média dos pontos de dados em cada cluster.
#Ou seja, ele escolhe um ponto aleatório como centroide inicial e atribui cada ponto de dados ao 
# centroide mais próximo. Depois disso, ele calcula a nova média dos pontos de dados em cada cluster
# e atualiza os centroides. Esse processo é repetido até que os centroides não mudem mais ou até que um número máximo
# de iterações seja atingido.


def aplicar_kmeans(dados, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(dados)
    return kmeans.labels_, kmeans.cluster_centers_


# os centroides são escolhidos de forma a minimizar a inertia, que é a soma das distâncias quadráticas
# entre cada ponto de dados e o centroide do cluster ao qual ele pertence. A inertia é uma medida de quão
#  bem os pontos de dados estão agrupados em torno dos centroides.
#Para calcular a inertia, o Kmeans calcula a distância euclidiana entre cada ponto de dados e o
# centroide do cluster,e o resultado é a soma dessas distâncias para todos os pontos em todos os clusters.


def calcular_inertia(dados, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(dados)
    return kmeans.inertia_

#A inertia é utilizada também no método do cotovelo para determinar o número ideal de clusters.
# Nesse método, a inertia é calculada para diferentes valores de K e plotada em um gráfico.
# O ponto onde a taxa de diminuição da inertia começa a desacelerar (formando um "cotovelo") é 
# considerado o número ideal de clusters.

#Esse método parte do ponto de que quanto maior o valor de K menor será a inertia. E seu valor é 
# considerado melhor quanto mais se aproxima de 0. Pois se o valor de K for exatamente a quantidade 
# de pontos de dados, a inertia será 0, já que cada ponto de dados será seu próprio cluster.


#Por ser um algoritmo que visa minimizar a inertia, o Kmeans não funciona bem com clusters de formas
# irregulares ou com tamanhos muito diferentes, pois a inertia pode ser enganosa nesses casos.
#Além disso, o Kmeans é sensível a outliers, que podem distorionar a posição dos centroides e afetar a 
# qualidade da clusterização.

