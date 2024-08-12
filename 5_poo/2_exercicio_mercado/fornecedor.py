from produto import Produto

class Fornecedor:
    def __init__(self, nome):
        """
        Construtor da classe Fornecedor:
        Atributos:
        - nome (str)
        - produtos_fornecidos: Produtos (list)
        """
        self.__nome = nome
        self.__produtos_fornecidos = []

    @property
    def nome(self):
        """Getter de nome"""
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        """Setter de nome"""
        if nome is not None and nome != "" and isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Nome inválido")
        
    @property
    def produtos_fornecidos(self):
        """Getter de produtos_fornecidos"""
        return self.__produtos_fornecidos
    
    def incluir_produto_ao_fornecedor(self, produto: Produto):
        """Método que inclui um produto ao fornecedor"""
        self.__produtos_fornecidos.append(produto)
    
    def __str__(self):
        produtos = ', '.join([str(produto) for produto in self.__produtos_fornecidos])
        return f'{self.nome}: {produtos}'
