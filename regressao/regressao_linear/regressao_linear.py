regressao_linear = """O objetivo da regressão linear é prever um valor numérico contínuo (y) encontrando a melhor relação matemática entre os dados 
de entrada (x) 
 e a saída esperada. O modelo busca traçar uma linha (ou um plano, no caso de múltiplas variáveis) que minimize a distância entre o que ele 
 previu e o valor real. Essa distância é o que chamamos de erro.
A fórmula base é y = w * x + b. O 'w' representa os pesos (weights), que determinam a importância de cada característica. O 'b' é o viés (bias),
  o ponto de partida da previsão. Em modelos com várias características (features), cada uma terá seu próprio peso: y = w1x1 + w2x2 + ... + wn*xn + b.

O processo de treinamento segue um ciclo iterativo de três passos principais:
Predição (Forward Pass): O modelo faz o cálculo com os pesos atuais.
Cálculo da Perda (Loss): Mede-se o erro usando geralmente o MSE (Mean Squared Error), elevando a diferença ao quadrado para punir erros grandes e 
 evitar valores negativos.
Otimização (Gradiente Descendente): O modelo calcula a derivada da função de erro para entender em qual direção deve ajustar os pesos para diminuir
  o erro.
O Learning Rate (taxa de aprendizado) é um parâmetro vital nesse ajuste. Ele define o tamanho do passo que o modelo dá na direção do acerto. Se for 
 muito alto, o modelo pula o ponto ideal e diverge; se for muito baixo, o treinamento fica lento demais.
O treinamento continua até que o modelo atinja um número definido de iterações ou até que a mudança na perda seja mínima, indicando que o modelo
  está suficientemente treinado.
"""

gradiente_descendente = """
O processo de aprendizado em inteligência artificial baseia-se na minimização de uma função de custo/erro, e o mecanismo principal para isso é o Gradiente 
Descendente. Para compreender este algoritmo, é necessário distinguir três conceitos interdependentes: a estratégia de busca (o algoritmo), a bússola 
de direção (o gradiente) e a ferramenta de medição de inclinação (a derivada).
No centro da análise está a Derivada, que representa a taxa de variação 
instantânea de uma função em relação a uma de suas variáveis. Matematicamente, ela nos diz o quanto o resultado de uma função se altera diante de uma 
mudança infinitesimal no valor de entrada. 
Quando lidamos com modelos complexos que possuem múltiplos parâmetros, estendemos esse conceito para as 
Derivadas Parciais, que medem a inclinação da função em relação a cada parâmetro individualmente, mantendo os demais constantes.O Gradiente é, por 
definição, um vetor que agrupa todas essas derivadas parciais. Em um espaço multidimensional, o vetor gradiente aponta exatamente para a direção de 
maior crescimento local da função. No contexto da otimização, o Gradiente Descendente utiliza essa informação para mover os parâmetros do modelo na 
direção oposta (daí o sinal negativo na fórmula de atualização), buscando o ponto de mínimo onde o erro é menor. 
A magnitude do passo dado nessa direção
é controlada pela Taxa de Aprendizado (Learning Rate), que escala o vetor gradiente para garantir uma convergência estável.Quanto ao cálculo desses
valores, existem duas abordagens fundamentais: a analítica e a numérica. A Diferenciação Analítica utiliza regras simbólicas do cálculo para obter 
uma expressão exata da derivada, sendo o método mais eficiente para processamento em larga escala. 
Já a Diferenciação Numérica, frequentemente 
referida como Quociente Diferencial, é uma estimativa baseada na definição formal de limite. Ela calcula a inclinação aproximando a função por meio
da diferença entre dois pontos muito próximos: $f(x + h) - f(x) / h$. Embora tenha um custo computacional mais elevado, o quociente diferencial é uma 
ferramenta indispensável para o Gradient Checking, servindo como prova real para garantir que as implementações analíticas complexas de algoritmos de 
aprendizagem estão operando sem erros matemáticos.
Em resumo, enquanto a derivada e o quociente diferencial fornecem a medida da inclinação, o gradiente
organiza essas medidas em um mapa de navegação, permitindo que o algoritmo de Gradiente Descendente conduza o modelo de forma iterativa até o estado 
de erro mínimo.
"""

def gradient_descent_univariado(gradiente_fn, theta_inicial, learning_rate, iteracoes):
    theta = theta_inicial
    
    for i in range(iteracoes):
        # 1. Calcula a inclinação no ponto atual
        gradiente = gradiente_fn(theta)
        
        # 2. Atualiza o parâmetro (anda na direção oposta ao gradiente)
        theta = theta - (learning_rate * gradiente)
        
        # Opcional: print para acompanhar a descida
        # print(f"Iteração {i}: theta = {theta:.4f}")
        
    return theta

# Exemplo de uso para f(x) = x^2 (onde a derivada é 2x)
# derivada_x2 = lambda x: 2 * x
# resultado = gradient_descent_univariado(derivada_x2, theta_inicial=10, learning_rate=0.1, iteracoes=50)

import numpy as np

def gradient_descent_multivariado(X, y, theta_inicial, learning_rate, iteracoes):
    """
    X: Matriz de dados (features)
    y: Vetor de respostas reais
    theta: Vetor de parâmetros (pesos)
    """
    theta = theta_inicial
    m = len(y) # número de amostras
    
    for i in range(iteracoes):
        # 1. Calcula a previsão do modelo (Produto Escalar)
        previsoes = X.dot(theta)
        
        # 2. Calcula o erro (resíduos)
        erro = previsoes - y
        
        # 3. Calcula o gradiente médio (Derivada parcial da MSE)
        # A fórmula matemática é: (1/m) * X^T * erro
        gradiente = (1/m) * X.T.dot(erro)
        
        # 4. Atualização simultânea de todos os thetas
        theta = theta - (learning_rate * gradiente)
        
    return theta

gd_estocatico= """
O Gradiente Descendente Estocástico (SGD) surge como uma solução para o principal gargalo da otimização em larga escala: o custo computacional. No 
método tradicional, para realizar um único ajuste nos parâmetros ($\theta$), o algoritmo precisa processar o erro de todas as amostras do conjunto
de dados, o que se torna inviável em datasets com milhões de registros. No SGD, a lógica é invertida: o algoritmo seleciona uma única amostra 
aleatória, calcula o gradiente baseado apenas nela e atualiza os pesos imediatamente. Esse ciclo se repete para cada amostra do conjunto, fazendo
com que o modelo aprenda de forma muito mais dinâmica e frequente.A principal característica visual e matemática do SGD é o seu comportamento
"ruidoso". Como cada exemplo individual pode ter particularidades ou ruídos, o gradiente não aponta sempre diretamente para o mínimo global de 
forma suave, como ocorre no método tradicional. Em vez disso, o caminho percorrido pelos parâmetros é oscilante e parece "bêbado", saltando de um 
lado para o outro. Embora isso pareça ineficiente, esse comportamento errático tem uma vantagem técnica oculta: ele ajuda o algoritmo a saltar para
fora de mínimos locais (buracos rasos na função de erro) que poderiam prender um algoritmo mais conservador, permitindo que ele encontre regiões de
mínimo global com mais facilidade.Com o tempo, à medida que o algoritmo processa muitas amostras, essa trajetória oscilante converge para a mesma 
região do mínimo que o método tradicional alcançaria. No entanto, para garantir que o modelo realmente pare de "saltar" quando chegar perto do objetivo,
é comum utilizar uma Taxa de Aprendizado Variável, que começa maior para permitir exploração e diminui gradualmente conforme o treino avança. Em 
aplicações modernas de Ciência de Dados e Deep Learning, o SGD (ou sua variante Mini-batch, que usa pequenos grupos de dados) é o padrão absoluto
, pois permite que o treinamento de modelos complexos ocorra em tempo real, utilizando a memória do computador de forma muito mais eficiente.

"""