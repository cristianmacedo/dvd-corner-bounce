## 🤔 Challenge
**Quantas colisões** até chegar em um canto?

(GIF)

Essa foi a pergunta que motivou este projeto.
## 💡 Approach
A solução parece simples:
**1:** Com a posição inicial da logo, obtemos o próximo ponto de colisão;
**2:** Com este ponto, calculamos o próximo, e assim sucessivamente;
**3:** Ao chegar em um canto, temos a contagem de iterações, e consequentemente, a quantidade de colisões restantes.

(GIF)

**❌ Problema:**
Dessa forma, precisamos calcular todos os movimentos da logo, efetivamente realizando uma **simulação completa** para obter o resultado.
Não parece muito efetivo, certo?
## 🔦 Approach #2:
Ao invés de calcular todos os passos da logo, vamos usar um pouco de geometria para obter o próximo ponto de colisão:

**1:** Sabemos que, a partir da direção da logo, existem sempre **duas possíveis bordas** que ele irá colidir:

(IMAGEM)

**2:** A partir das possíveis bordas, calculamos a **distância** entre a logo e cada uma delas:

(IMAGEM)

**3:** Assumindo que a logo se move sempre a **45°**, usamos a **menor** distância como parâmetro de cálculo para a obtenção da coordenada da colisão, alterando as coordenadas em X e Y de acordo com a **distância** obtida e a **direção** atual:

(IMAGEM)

Pronto! Dessa forma, obtemos a coordenada da próxima colisão, sem realizar uma simulação completa do movimento da logo.

## 🚀 Executing
Para executar o projeto, utilize este comando, na pasta raiz do repositório:
```
python game.py
```