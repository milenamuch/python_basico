class Produto:
    def __init__(self, nome: str, categoria: str, quantidade_disponivel: int):
        """Classe de produto:
        Atributos:
        - nome (str)
        - categoria (str)
        - quantidade_disponivel (int) """
        self.nome = nome
        self.categoria = categoria
        self.quantidade_disponivel = quantidade_disponivel
        
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
    def categoria(self):
        """Getter de categoria"""
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        """Setter de categoria"""
        if categoria is not None and categoria != "" and isinstance(categoria, str):
            self.__categoria = categoria
        else:
            raise ValueError("Categoria inválida")
    
    @property
    def quantidade_disponivel(self):
        """Getter de quantidade disponivel"""
        return self.__quantidade_disponivel
    
    @quantidade_disponivel.setter
    def quantidade_disponivel(self, quantidade_disponivel):
        """Setter de quantidade disponivel"""
        if quantidade_disponivel is None or quantidade_disponivel < 0 or not isinstance(quantidade_disponivel, int):
            raise ValueError("Quantidade inválida.")
        else:
            self.__quantidade_disponivel = quantidade_disponivel
    
    def diminuir_estoque(self, quantidade):
        """Método para diminuir o estoque"""
        if quantidade > self.quantidade_disponivel:
            raise ValueError("Quantidade indisponível.")
        else:
            self.__quantidade_disponivel -= quantidade
        return self.__quantidade_disponivel
    
    def __str__(self):
        return f'Nome: {self.nome}\nCategoria: {self.categoria}\nQuantidade disponível: {self.quantidade_disponivel}'