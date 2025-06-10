
import pytest
from matriz.Verificacao import verificacaoNivel1
class TestVerificacaoNivel1: #classe com T maisculo
    
    # teste para a funcao que verifica a entrada de dados, linhas e colunas
    def setup_method(self):
        self.verificacao = verificacaoNivel1.VerificaEntradaDados()
    
    #verificar a funcao as linhas e colunas
    def test_VericacaoNivelUm(self):
        # test com valores válidos
        assert self.verificacao.VericacaoNivelUm(3, 4) == (3, 4)
        assert self.verificacao.VericacaoNivelUm(1, 1) == (1, 1)
        
        # test com valores inválidos
        assert self.verificacao.VericacaoNivelUm(-1, 4) == None
        assert self.verificacao.VericacaoNivelUm(3, -2) == None
        assert self.verificacao.VericacaoNivelUm(0, 0) == None
        assert self.verificacao.VericacaoNivelUm(3.5, 4) == None
        
    def test_Verifica_Valor(self):
        # test com valores válidos
        assert self.verificacao.Verifica_Valor(5) == 5
        assert self.verificacao.Verifica_Valor(1) == 1
        
        # test com valores inválidos
        assert self.verificacao.Verifica_Valor(-1) == None
        assert self.verificacao.Verifica_Valor(0) == None
        assert self.verificacao.Verifica_Valor(3.14) == None
        assert self.verificacao.Verifica_Valor("texto") == None
    
        
        
    
        