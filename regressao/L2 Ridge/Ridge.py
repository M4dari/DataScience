explicacao = """A Regressão Ridge (L2) adiciona uma penalidade à Loss Function baseada no quadrado dos pesos (w²). Isso impede que os coeficientes 
fiquem muito grandes, combatendo o overfitting. O parâmetro Alpha controla essa força: quanto maior o Alpha, menores serão os pesos. É ideal para 
quando você tem muitas variáveis que podem estar correlacionadas, pois ela distribui o impacto entre elas em vez de deixar uma única variável dominar 
o modelo.
A fórmula da Regressão Ridge é: Loss = MSE + Alpha * (w1² + w2² + ... + wn²). O processo de treinamento é semelhante ao da regressão linear, mas
com a adição da penalidade L2, o que ajuda a manter os pesos sob controle e melhora a generalização do modelo.

*MSE = (soma dos erros quadráticos) / (número de amostras)

O Alpha é um hiperparâmetro definido pelo desenvolvedor antes do treino. Para encontrar seu valor ideal, utiliza-se o Grid Search com Validação 
Cruzada, testando diferentes valores e selecionando o que melhor generaliza para dados novos. Na prática, a Ridge "cobra caro" por pesos altos. 
No cálculo do Gradiente Descendente, isso se traduz em um ajuste que puxa os pesos em direção a zero sempre que eles tentam crescer demais para
compensar um erro nos dados de treino.
"""
