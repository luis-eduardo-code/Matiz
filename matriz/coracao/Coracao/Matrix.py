# -*- coding: utf-8 -*-
from Verificacao.verificacaoNivel1 import VerificaEntradaDados
import numpy as np

import matriz
#escondido, a classe de criar matrizes estar "completo" so falta revisar, começar a classe de operacoes da matriz assim que o import tiver certo
class Matriz:
    #classe para criar matrizes
    class CriarMatriz:
        """Classe para criar matrizes de diferentes formas."""
        """"Cria uma matriz com o número de linhas e colunas especificado pelo usuário.

        Returns:
            _type_: _description_
        """
        def Usuario_Cria_matriz(linha,coluna):
            matriz = np.zeros((linha,coluna))
            for i in range(linha):
                for j in range(coluna):
                    numero = VerificaEntradaDados.PedirNumeroX()
                    matriz[i][j] = numero
            return matriz
            
            
        
            """ Cria uma matriz programaticamente com o número de linhas, colunas e valor máximo especificado pelo usuário.
            """
        
        def Programa_Criar_Matriz(linha, coluna,valor):
            matriz = np.random.randint(0,valor,(linha,coluna))
            return matriz
            
        
    
    #classe com as operacoes da matriz
    class OperacoesMatriz:
        """"Classe para realizar operações em matrizes."""
        
        @staticmethod
        def Soma_matriz(matriz1, matriz2):
            """Soma duas matrizes."""
            return np.array(matriz1) + np.array(matriz2)
        
        @staticmethod
        def Subtracao_matriz(matriz1, matriz2):
            """Subtrai a segunda matriz da primeira."""
            return np.array(matriz1) - np.array(matriz2)

        @staticmethod
        def Multiplicacao_matriz(matriz1, matriz2):
            """Multiplica duas matrizes."""
            return np.dot(matriz1, matriz2)
        