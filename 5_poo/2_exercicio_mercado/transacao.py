from produto import Produto
from cliente import Cliente
from datetime import datetime

class Transacao:
    def __init__(self, cliente: Cliente, produto: Produto, quantidade_produtos: int):
        """
        Classe Transacao:
        Atributos:
        - cliente (Cliente)
        - produto (Produto)
        - quantidade_produtos (int)
        - data (datetime)
        """
        
        self.__cliente = cliente
        self.__produto = produto
        self.quantidade_produtos = quantidade_produtos
        self.__data = datetime.now()
        
        produto.diminuir_estoque(quantidade_produtos)
        
    @property
    def cliente(self):
        """Getter de cliente"""
        return self.__cliente
    
    @property
    def produto(self):
        """Getter de produto"""
        return self.__produto
    
    @property
    def quantidade_produtos(self):
        """Getter de quantidade de produtos"""
        return self.__quantidade_produtos
    
    @quantidade_produtos.setter
    def quantidade_produtos(self, quantidade_produtos):
        """Setter de quantidade_produtos"""
        if quantidade_produtos < 0 or quantidade_produtos is None or not isinstance(quantidade_produtos, int):
            raise ValueError("Quantidade inválida")
        self.__quantidade_produtos = quantidade_produtos
                
    def __str__(self):
        data_formatada = self.__data.strftime('%d/%m/%Y %H:%M')
        return f'Cliente: {self.__cliente}\nProduto: {self.__produto}\nQuantidade: {self.__quantidade_produtos}\nData da compra: {data_formatada}'
