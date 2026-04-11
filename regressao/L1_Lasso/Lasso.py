lasso = """
1. O QUE É:
   É uma técnica que adiciona uma penalidade baseada no valor absoluto dos pesos 
   do modelo para evitar o Overfitting.

2. A MATEMÁTICA:
   Loss = MSE + Alpha * (|w1| + |w2| + ... + |wn|)
   
   - Alpha (ou Lambda): Controla a força da regularização.
   - |w|: Valor absoluto (módulo) de cada peso/coeficiente.

3. DIFERENCIAL:
   Diferente de outras regularizações, o Lasso tem a capacidade de zerar (w=0) 
   os coeficientes de variáveis que ele considera irrelevantes ou ruidosas.

4. POR QUE ELE CONSEGE ZERAR?
   - Geometria: A restrição do Lasso tem o formato de um DIAMANTE (quinas).
   - Quando o erro do modelo tenta ser minimizado, ele tende a "bater" nas 
     quinas do diamante, que ficam exatamente em cima dos eixos (onde o peso é 0).
   - Derivada: A "força" que puxa o peso para o zero é constante. Ela não 
     diminui quando o peso fica pequeno, empurrando-o até o zero absoluto.

5. QUANDO USAR:
   - Quando você tem muitas colunas e quer simplificar o modelo.
   - Quando você quer identificar quais variáveis realmente importam.
   - Quando você quer um modelo mais leve e fácil de interpretar.
"""