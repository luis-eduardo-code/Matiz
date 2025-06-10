oi :)

````markdown
# 🧮 MatrizInterUsuario

Este módulo fornece uma interface para que o usuário interaja com **operações matriciais** de forma estruturada, usando `NumPy` como base. Ele é útil para manipulação de matrizes, validação de entrada e resolução de problemas de álgebra linear.

#

## 🚀 Funcionalidades da Classe `MatrizInterUsuario`

### 📥 Criação de Matrizes

* `Usuario_cria_matriz_inter(linha, coluna)`

  * Cria uma matriz com valores digitados pelo usuário.
  * Valida número de linhas e colunas.

* `Programa_cria_matriz_inter(linha, coluna, valor)`

  * Cria uma matriz com valores aleatórios até um valor máximo.
  * Valida linhas, colunas e valor.

---

### ➕ Operações Básicas

* `Somar_matriz(matriz1, matriz2)`
* `Subtrair_matriz(matriz1, matriz2)`
* `Multiplicar_matriz(matriz1, matriz2)`

Cada função valida se as dimensões das matrizes são compatíveis antes de realizar a operação.

---

### 🧠 Propriedades de Matrizes

* `Matriz_identidade(matriz)`

  * Cria uma matriz identidade do mesmo tamanho da matriz quadrada fornecida.

* `Matriz_inversa(matriz)`

  * Calcula a matriz inversa, se possível.

* `Determinante_matriz(matriz)`

  * Retorna o determinante da matriz.

* `Traço_matriz(matriz)`

  * Retorna a soma dos elementos da diagonal principal.

* `Posto_matriz(matriz)`

  * Retorna o posto (rank) da matriz.

---

### 📐 Álgebra Linear

* `Escalonar_matriz(matriz)`

  * Aplica decomposição QR e retorna a matriz `Q`.
  * Útil para aproximar a forma escalonada.

* `Resolver_sistema_equacoes(matriz, vetor)`

  * Resolve o sistema linear `Ax = b` usando `np.linalg.solve`.

---

## ✅ Testes

Todas as funções da classe possuem **testes automatizados** para garantir sua robustez, incluindo:

* Validação de entrada.
* Comparação com resultados esperados usando `np.testing.assert_array_equal`.
* Cobertura de erros (e.g., matrizes não quadradas, inversão impossível, dimensões incompatíveis).

---



## 📁 Exemplo de Uso

```python
obj = MatrizInterUsuario()
A = obj.Programa_cria_matriz_inter(3, 3, 10)
B = obj.Programa_cria_matriz_inter(3, 3, 10)

C = obj.Somar_matriz(A, B)
print("Soma:", C)

det = obj.Determinante_matriz(A)
print("Determinante:", det)
```

---

## 📚 Licença

Este projeto é acadêmico e livre para uso educacional.

---



