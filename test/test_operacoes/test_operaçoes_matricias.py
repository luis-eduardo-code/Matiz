from matriz.Inter import Usuario
import pytest
import numpy as np

# Teste para a função de soma de matrizes



class Test_operacoes_matriz:
    """Classe de teste para operações de matrizes."""
    

    """Configuração do teste, cria uma matriz 2x2 com valores de 10."""
    def setup_method(self):
        self.matriz = Usuario.Programa_Criar_Matriz(2, 2, 10)

    """Testanto a soma de matrizes."""
    def test_soma_matriz(self):
        resultado = Usuario.Soma_matriz(self.matriz, self.matriz)
        esperado = np.array([[2, 4], [6, 8]])
        np.testing.assert_array_equal(resultado, esperado)
        
    def test_soma_matriz_dimensoes_diferentes(self):
        matriz1 = Usuario.Programa_Criar_Matriz(2, 2, 10)
        matriz2 = Usuario.Programa_Criar_Matriz(2, 3, 10)
        with pytest.raises(ValueError):
            Usuario.Soma_matriz(matriz1, matriz2)

    """Testando a subtração de matrizes."""
    def test_subtracao_matriz(self):
        resultado = Usuario.Subtrair_matriz(self.matriz, self.matriz)
        esperado = np.array([[0, 0], [0, 0]])
        np.testing.assert_array_equal(resultado, esperado)
        
    def test_subtracao_matriz_dimensoes_diferentes(self):
        matriz1 = Usuario.Programa_Criar_Matriz(2, 2, 10)
        matriz2 = Usuario.Programa_Criar_Matriz(2, 3, 10)
        with pytest.raises(ValueError):
            Usuario.Subtrair_matriz(matriz1, matriz2)

    """Testando a multiplicação de matrizes."""
    def test_multiplicacao_matriz(self):
        matriz1 = Usuario.Programa_Criar_Matriz(2, 2, 10)
        matriz2 = Usuario.Programa_Criar_Matriz(2, 2, 10)
        resultado = Usuario.Multiplicar_matriz(matriz1, matriz2)
        esperado = np.array([[100, 100], [100, 100]])
        np.testing.assert_array_equal(resultado, esperado)
    
    def test_multiplicacao_matriz_dimensoes_incompativeis(self):
        matriz1 = Usuario.Programa_Criar_Matriz(2, 3, 10)
        matriz2 = Usuario.Programa_Criar_Matriz(2, 2, 10)
        with pytest.raises(ValueError):
            Usuario.Multiplicar_matriz(matriz1, matriz2)
