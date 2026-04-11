#O GMM é parecido com o Kmeans- funciona de maneira similar porém consegue lidar melhor com diferentes formas de clusters, inclusive quando estão
# sobrepostos
#Ele assume que os dados são gerados a partir de uma mistura de várias distribuições gaussianas (distribuição normal/formato de sino), cada
# uma representando um cluster diferente.
#Cada cluster é representado por uma gaussiana com seus próprios parâmetros: média (centro do cluster) e covariância (forma e orientação do cluster).
#Ele funciona de maneira similar ao Kmeans pois, na primeira iteração vai escolher clusters de formas aleatórias, e calcular a probabilidade de cada
#ponto fazer parte daquele cluster.
#Depois, recalcula os parâmetros das gaussianas (média e covariância) com base nos pontos atribuídos a cada cluster, ponderados pela probabilidade
# de pertencimento.
#Esse processo de atribuição de pontos e recalculo dos parâmetros é repetido até que os parâmetros se estabilizem ou um critério de parada seja atingido.
#Uma diferença importante é que, ao invés de atribuir cada ponto a um único cluster, o GMM atribui uma probabilidade de pertencimento a cada ponto para
# cada cluster.
#Isso permite que o GMM lide melhor com clusters que se sobrepõem, onde um ponto pode pertencer a múltiplos clusters com diferentes graus de certeza.

#Ele move os centros ($\mu$) e ajusta as formas ($\Sigma$) usando as probabilidades do Passo E como pesos. Quem tem mais "voto" puxa o sino para perto.

#A gente tem como parametros o número de clusters (n_components), o tipo de covariância (covariance_type) que pode ser:
# 'full': cada cluster tem sua própria matriz de covariância completa. (Mais potente e mais caro)
# 'tied': todos os clusters compartilham a mesma matriz de covariância.
# 'diag': cada cluster tem sua própria matriz de covariância diagonal. (elipses só ficam deitadas ou em pé)
# 'spherical': cada cluster tem sua própria variância escalar (covariância isotrópica, clusters são bolas perfeitas, mais simples).
#E o número máximo de iterações (max_iter) que o algoritmo vai fazer antes de parar.

#A principal métrica usada para avaliar a qualidade do GMM é o Akaike Information Criterion (AIC) e o Bayesian Information Criterion (BIC).
#Essas métricas penalizam a complexidade do modelo (número de parâmetros) para evitar overfitting.
#Modelos com valores mais baixos de AIC ou BIC são preferíveis, indicando um melhor equilíbrio entre ajuste e complexidade.

