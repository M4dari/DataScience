elastic_net = """
==============================================================
ESTUDO DE PROFUNDIDADE: ELASTIC== NET REGULARIZATION
================================================================

1. A FUNÇÃO OBJETIVO (O 'CORAÇÃO' DO MODELO)
O Elastic Net minimiza a seguinte função de custo:

J(w) = MSE(w) + λ₁|w|₁ + λ₂|w|₂²

Onde:
- MSE(w): Erro Quadrático Médio (fidelidade aos dados).
- λ₁|w|₁: Penalidade L1 (Lasso) - Soma dos valores absolutos.
- λ₂|w|₂²: Penalidade L2 (Ridge) - Soma dos quadrados.

No Scikit-Learn, a parametrização é simplificada para:
Alpha * L1_ratio * ||w||₁ + 0.5 * Alpha * (1 - L1_ratio) * ||w||₂²

----------------------------------------------------------------
2. O EFEITO DE AGRUPAMENTO (GROUPING EFFECT)
Este é o maior diferencial do Elastic Net frente ao Lasso:

- Problema do Lasso: Se você tem variáveis altamente correlacionadas (ex: x1 ≈ x2),
  o Lasso tende a selecionar uma e zerar a outra de forma instável (depende do ruído).
- Solução Elastic Net: Graças à curvatura da componente L2 (Ridge), se x1 e x2 
  forem parecidas, o modelo tende a manter AMBAS no modelo com pesos similares.
  Matematicamente, a convexidade estrita da penalidade L2 força essa estabilidade.

----------------------------------------------------------------
3. GEOMETRIA E OTIMIZAÇÃO
- Lasso (L1): O contorno é um poliedro (diamante). As quinas nos eixos 
  promovem a 'esparsidade' (pesos = 0).
- Ridge (L2): O contorno é uma hiperesfera (círculo). Não possui quinas,
  logo não zera coeficientes, apenas os encolhe (shrinkage).
- Elastic Net: O contorno é uma 'esfera-diamante' (convex hull). 
  Ele possui as quinas do Lasso (para zerar o que é lixo), mas as bordas 
  são convexas como o Ridge (para lidar com correlação).



----------------------------------------------------------------
4. COMPORTAMENTO DE SELEÇÃO (BIAS vs VARIANCE TREADEOFF)
- O Elastic Net introduz um 'Viés' (Bias) proposital para reduzir a 'Variância'.
- Ele é particularmente superior quando o número de preditores (p) é maior 
  que o número de observações (n), ou quando há forte multicolinearidade.

5. IMPLEMENTAÇÃO PRÁTICA (XGBOOST vs LINEAR MODELS)
- Em Modelos Lineares: O Elastic Net é resolvido via algoritmos de 
  'Coordinate Descent'.
- No XGBoost: Você controla o Elastic Net ajustando simultaneamente 
  'reg_lambda' (L2) e 'reg_alpha' (L1). Não há um parâmetro único 'l1_ratio',
  você define as forças individualmente.
================================================================
"""
