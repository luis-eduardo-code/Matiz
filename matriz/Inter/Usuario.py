import re
from ..Verificacao.verificacaoNivel1 import VerificaEntradaDados
from ..coracao.Coracao.Matrix import Matriz
import numpy as np


class MatrizInterUsuario:
    """Classe para interagir com o usuário na criação de matrizes.
    """
    def __init__(self):
            self.VerificaEntradaDados = VerificaEntradaDados()
        
    """Cria uma matriz com o número de linhas,colunas e cada numero digitado pelo  usuário."""""
    def Usuario_cria_matriz_inter(self,linha, coluna):
        Verifica = self.VerificaEntradaDados.VericacaoNivelUm(linha, coluna)
        if Verifica is None:
            return None
        # Cria a matriz com o número de linhas e colunas especificado pelo usuário
        matriz = Matriz.CriarMatriz(linha,coluna)
        if matriz is None: # acoplamento desnecessário
            print("Erro: Não foi possível criar a matriz.")
            return None
        return matriz
        
 
    """Cria uma matriz com o número de linhas, colunas e valor máximo especificado pelo usuário.
    """
    def Programa_cria_matriz_inter(self,linha, coluna,valor):
        verificar = self.VerificaEntradaDados.VericacaoNivelUm(linha, coluna)
        if verificar is None:
            raise ValueError("Número de linhas e colunas inválido.")
            return None
        verificar_valor = self.VerificaEntradaDados.Verifica_Valor(valor)
        if verificar_valor is None:
            raise ValueError("Valor inválido para a matriz.")
        matriz = Matriz.CriarMatriz.Programa_Criar_Matriz(linha, coluna, valor)
        return matriz

    """ soma duas matrizes."""
    def Somar_matriz(self,matriz1, matriz2):

        if matriz1.shape != matriz2.shape: # verificar se as matrizes têm o mesmo tamanho, sem usar acoplamento desnecessário
            raise ValueError("As matrizes devem ter o mesmo tamanho para serem somadas.")
        return Matriz.OperacoesMatriz.Soma_matriz(matriz1, matriz2)
    
    """Subtrai a segunda matriz da primeira."""
    def Subtrair_matriz(self,matriz1, matriz2):
        
        if matriz1.shape != matriz2.shape: # verificar se as matrizes têm o mesmo tamanho, sem usar acoplamento desnecessário
            raise ValueError("As matrizes devem ter o mesmo tamanho para serem subtraídas.")
        return Matriz.OperacoesMatriz.Subtracao_matriz(matriz1, matriz2)
    """Multiplica duas matrizes."""
    def Multiplicar_matriz(self,matriz1, matriz2):  
        if matriz1.shape[1] != matriz2.shape[0]:
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")
        return Matriz.OperacoesMatriz.Multiplicacao_matriz(matriz1, matriz2)    
    
    """Cria uma matriz identidade com o tamanho especificado pelo usuário."""
    def Matriz_identidade(self,matriz):
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("A matriz deve ser quadrada para criar uma matriz identidade.")
        return np.eye(matriz.shape[0])
    
    """Calcula a matriz inversa.""" 
    def Matriz_inversa(self, matriz):
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("A matriz deve ser quadrada para calcular a inversa.")
        try:
            return np.linalg.inv(matriz)
        except np.linalg.LinAlgError:
            raise ValueError("A matriz não é invertível.")
    
    """Calcula o determinante da matriz."""
    def Determinante_matriz(self, matriz):
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("A matriz deve ser quadrada para calcular o determinante.")
        return np.linalg.det(matriz)
        
    """Calcula o traço da matriz."""
    def Traço_matriz(self, matriz):
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("A matriz deve ser quadrada para calcular o traço.")
        return np.trace(matriz)
    
    """Calcula o posto da matriz."""
    def Posto_matriz(self, matriz):
        return np.linalg.matrix_rank(matriz)
    
    """ EScalonar a matriz."""
    def Escalonar_matriz(self, matriz): 
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("A matriz deve ser quadrada para escalonar.")
        return np.linalg.qr(matriz)[0]
    
    """resolver um sistema de equações lineares."""
    def Resolver_sistema_equacoes(self, matriz, vetor):
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("A matriz deve ser quadrada para resolver o sistema.")
        try:
            return np.linalg.solve(matriz, vetor)
        except np.linalg.LinAlgError:
            raise ValueError("O sistema não tem solução única.")
