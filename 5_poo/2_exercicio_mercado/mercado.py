from cliente import Cliente
from transacao import Transacao

class Mercado:
    def __init__(self, nome):
        """
        Construtor da classe Mercado:
        Atributos:
        - nome (str)
        - clientes (list)
        - transacoes (list)
        """
        self.nome = nome
        self.__clientes = []
        self.__transacoes = []
    
    @property
    def nome(self):
        """Getter de nome"""
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        """Setter de nome"""
        if nome and isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Nome inválido.")
        
    @property
    def clientes(self):
        """Getter de clientes"""
        return self.__clientes
    
    @property
    def transacoes(self):
        """Getter de transacoes"""
        return self.__transacoes
    
    def adicionar_cliente(self, cliente: Cliente):
        """Método que inclui um cliente"""
        self.__clientes.append(cliente)
    
    def adicionar_transacao(self, transacao: Transacao):
        """Método que inclui uma transação"""
        self.__transacoes.append(transacao)

    def listar_clientes(self):
        """Método que retorna a lista de clientes"""
        return '\n'.join([str(cliente) for cliente in self.__clientes])
    
    def listar_transacoes(self):
        """Método que retorna a lista de transações"""
        return ', '.join([str(transacao) for transacao in self.__transacoes])   
    
    def __str__(self) -> str:
        clientes = self.listar_clientes()
        transacoes = self.listar_transacoes()
        return f'Nome: {self.__nome}\nClientes: {clientes}\nTransações: {transacoes}'
