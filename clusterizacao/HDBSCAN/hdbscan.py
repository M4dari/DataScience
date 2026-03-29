#O DBSCAN trabalha com dois conceitos principais: o eps e o MinPts
#O eps é um valor passado como parâmetro que define a distãncia máxima entre dois 
# pontos para que eles sejam considerados vizinhos, ou seja, defiine se o ponto vai estar considerado "perto" do outro
#Já o MinPts é um número mínimo de pontos/dados necessários para formar um grupo/cluster

#Na prática o DBSCAN, para todos os dados, olha pra todos os pontos dentro da distância eps do ponto atual, tudo que é considerado vizinhos/perto.
#Se a quantidade de pontos for maior ou igual o valor passado como MinPts ele considera como um grupo/cluster, e marca todos esses pontos como parte
#  do cluster.
#Se a quantidade de pontos for menor que o MinPts, o ponto atual é marcado como ruído/outlier, ou seja, não pertence a nenhum cluster.

#O DBSCAN não precisa de um número pré-definido de clusters, ele identifica os clusters com base na densidade dos pontos.
#Ele é capaz de identificar clusters de formas arbitrárias, o que o torna adequado para conjuntos de dados com clusters não esféricos.
#Além disso, o DBSCAN é robusto a outliers, pois os pontos que não pertencem a nenhum cluster são marcados como ruído.

#Mas por analisar todos os pontos, ele acaba sendo ruim em grande escala, porque o custo computacional cresce muito com o número de pontos.

#Por isso, foi criado o HDBSCAN- Hierarquical DBSCAN que usa uma abordagem hierárquica para melhorar a eficiência do DBSCAN.
#Ele calcula para cada ponto uma distância mínima para que ele tenha o MinPts e usa essa distãncia para dividir pontos muito densos (com uma
# distância pequena, ou seja, muitos vizinhos próximos) ou menos densos (distãncia maior, menos vizinhos próximos).

#Além disso, ele também calcula uma distância de alcançabilidade mútua, que é a maior distância entre dois pontos, considerando a densidade
# local de cada ponto.

#A partir disso, nós vamos ter um grafo hierárquico de densidade, que é como se nós conectassemos todos os pontos, mas com as distâncias ajustadas
#pela distãncia de alcançabilidade mútua.
# E ai é criado uma árvore de clusters, onde separamos os clusters de densidades diferentes, removendo conexões mais fracas (com distâncias maiores)
#  primeiro.
# Depois, escolhemos os clusters mais estáveis, que são aqueles que permanecem por mais tempo na árvore, ou seja, que não são facilmente divididos
#  em subclusters.
#Cada cluster recebe um score de estabilidade, que é uma medida de quão bem definido o cluster é em relação aos outros clusters.
# E ai escolhemos os clusters com maior estabilidade como os clusters finais.




