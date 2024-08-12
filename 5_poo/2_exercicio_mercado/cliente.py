class Cliente:
    def __init__(self, nome: str, telefone: str, endereco: str):
        """Construtor da classe Cliente:
            Atributos: 
            - nome (str)
            - telefone (str)
            - endereco (str)
        """
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = endereco
        
    @property  
    def nome(self):
        """Getter de nome"""
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """Setter de nome"""
        if nome != None and nome != "" and type(nome) == str:
            self.__nome = nome 
        else:
            raise ValueError("Nome inválido")
    
    @property
    def telefone(self):
        """Getter de telefone"""
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        """Setter de telefone"""
        if telefone != None and telefone != "" and type(telefone) == str:
            self.__telefone = telefone
        else:
            raise ValueError("Telefone inválido")
        
    @property
    def endereco(self):
        """Getter de endereco"""
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        """Setter de endereco"""
        if endereco != None and endereco != "" and type(endereco) == str:
            self.__endereco = endereco
        else:
            raise ValueError("Endereço inválido")
    
    def __str__(self) -> str:
        return f'Nome: {self.__nome}\nTelefone: {self.__telefone}\nEndereço: {self.__endereco}'