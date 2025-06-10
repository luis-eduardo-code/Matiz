class VerificaEntradaDados:
    """Classe para verificar a entrada de dados do usuário.

    Returns:
        None: Se a entrada for inválida.
        tuple: Se a entrada for válida, retorna uma tupla com o número de linhas e colunas.
    """
    #verificar o numero de colunas e linhas
    @staticmethod
    def VericacaoNivelUm(NumeroLinhas,NumeroColunas):
        #casos errados
        # Verifica se o número de linhas e colunas é maior que 0
        if NumeroColunas <1 or  NumeroLinhas<1 :
            return None
        # Verifica se o número de linhas e colunas é um inteiro
        elif not isinstance(NumeroLinhas,int) or not isinstance(NumeroColunas,int):
            return None
        # casos certos
        else:
            return NumeroLinhas , NumeroColunas
    
    #verificar os elementos da coluna
    @staticmethod
    def PedirNumeroX (self):    
        # Pede ao usuário para inserir um número
        try:
            numero = int(input("Digite um número inteiro: "))
            if  isinstance(numero, float):
                return None
            else:
                return numero
        except ValueError:
            return None
        
    #verificar o valor do sorteio do random da matriz programatica
    @staticmethod
    def Verifica_Valor(valor):
        # Verifica se o valor é um inteiro positivo
        if isinstance(valor, int) and valor > 0:
            return valor
        else:
            return None
        