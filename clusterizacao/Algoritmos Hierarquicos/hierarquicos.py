#É o tipo de algoritmo que cria uma hierarquia pra definir os clusters, tipo uma árvore genealógica, onde cada nó representa um cluster. Existem
# dois tipos principais: aglomerativo (bottom-up) e divisivo (top-down).

#O Bottom up é quando nós começamos com cada dado sendo um único cluster, e a partir disso, vamos juntando os clusters mais próximos até que reste
#  apenas um cluster ou até que um critério de parada seja atingido.
#Já o Top down é o oposto, começamos com todos os dados em um único cluster e vamos dividindo os clusters em subclusters até que cada dado esteja
#  em seu próprio cluster ou até que um critério de parada seja atingido.

#Antes de iniciar o algoritmo, como parametro, nós vamos passar a distância que vai ser usada(ex: euclidiana), e o linkage(single, average, complete,
#  ward)
#Nós passamos os dados, e vamos considerar cada dado como sendo um cluster, em seguida, utilizamos a distância fornecida para calcular a distância 
#fornecida para calcular a distância de todos os clusters entre si, e ai juntamos o par mais próximo como sendo um único cluster.
#Depois dessa primeira iteração, nós vamos recalcular as distâncias, porém agora, como distância, vamos utlizar o conceito de linkage

#Cada Linkage vai considerar um tipo de distância:
#single- vai utilizar o ponto mais próximo, ou seja, a menor distância entre os pontos dos dois clusters
#complete- vai utilizar o ponto mais distante, ou seja, a maior distância entre os pontos dos dois clusters
#average- vai utilizar a média das distâncias entre todos os pontos dos dois clusters
#ward- só funciona com dados numéricos e distância Euclidiana, e junta os clusters que causam menor aumento da variância interna.

#O algoritmo vai juntando, passo a passo, os dois clusters mais próximos em cada iteração, recalculando distâncias a cada vez, até que reste apenas
#um cluster contendo todos os pontos. Nos dividimos os grupos no final, onde, depois de visualizarmos o dendograma, escolhemos o "corte"
# que melhor dividide nossos dados.


#As métricas mais usadas para avaliar a qualidade do agrupamento são:
#Silhouette- mede quão bem cada ponto está dentro do seu cluster e está longe dos outros clusters. Quanto mais próximo de 1 melhor- Ajuda a
# escolher o ponto de "corte"
#Calinski-Harabasz - ele compara a variância entre os clusters e dentro de cada cluster, quanto maior melhor, mas funciona bem apenas para
# clusters convexos

#Cophenetic Correlation- essa é uma métrica específica para algoritmos hierarquicos, pois vai medir se o dendograma representa bem as
# distâncias originais. Ele compara a distância entre os pontos e a distância no dendograma(altura da junção). Quanto mais próximo de 1 mais fiel
# é o dendograma, se for muito baixa= dendograma ruim