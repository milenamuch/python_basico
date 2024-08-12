from datetime import datetime, timedelta
from typing import List

class Autor: 
    """
    Classe que representa um autor.
    
    Atributos:
        nome (str): Nome do autor.
    """

    def __init__(self, nome: str):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome
    
    def __str__(self) -> str:
        return self._nome 

class Genero: 
    """
    Classe que representa um gênero.
    
    Atributos:
        nome (str): Nome do gênero.
    """

    def __init__(self, nome: str):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome
    
    def __str__(self) -> str:
        return self._nome 

class Livro:
    """
    Classe que representa um livro.
    
    Atributos:
        titulo (str): Título do livro.
        editora (str): Editora do livro.
        max_renovacoes (int): Número máximo de renovações permitidas.
        autores (List[Autor]): Lista de autores do livro.
        generos (List[Genero]): Lista de gêneros do livro.
    """

    def __init__(self, titulo: str, editora: str, max_renovacoes: int = 0):
        self._titulo = titulo
        self._editora = editora
        self._max_renovacoes = max_renovacoes
        self._autores: List[Autor] = []
        self._generos: List[Genero] = []

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def editora(self) -> str:
        return self._editora

    @property
    def max_renovacoes(self) -> int:
        return self._max_renovacoes

    @property
    def autores(self) -> List[Autor]:
        return self._autores

    @property
    def generos(self) -> List[Genero]:
        return self._generos

    def adicionar_autor(self, autor: Autor):
        """Adiciona um autor à lista de autores do livro."""
        self._autores.append(autor)

    def adicionar_genero(self, genero: Genero):
        """Adiciona um gênero à lista de gêneros do livro."""
        self._generos.append(genero)
    
    def __str__(self) -> str:
        lista_autores = ", ".join(str(autor) for autor in self._autores)
        lista_generos = ", ".join(str(genero) for genero in self._generos)
        return f"Título: {self._titulo} \nEditora: {self._editora} \nAutor(es): {lista_autores} \nGênero(s): {lista_generos}" 

class Usuario:
    """
    Classe que representa um usuário da biblioteca.

    Atributos:
        nome (str): Nome do usuário.
        telefone (str): Telefone do usuário.
        nacionalidade (str): Nacionalidade do usuário.
    """

    def __init__(self, nome: str, telefone: str, nacionalidade: str):
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def telefone(self) -> str:
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor: str):
        if isinstance(valor, str):  
            self._telefone = valor
        
    @property
    def nacionalidade(self) -> str:
        return self._nacionalidade
    
    def __str__(self) -> str:
        return f"Nome: {self._nome}, Telefone: {self._telefone}, Nacionalidade: {self._nacionalidade}"
    
class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario, data_emprestimo: datetime, data_devolucao: datetime):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def __str__(self) -> str:
        return (f"Livro: {self.livro.titulo}, Usuário: {self.usuario.nome}, "
                f"Data de Empréstimo: {self.data_emprestimo}, Data de Devolução: {self.data_devolucao}")
        
class Biblioteca:
    """
    Classe que representa uma biblioteca.

    Atributos:
        livros_disponiveis (List[Livro]): Lista de livros disponíveis.
        livros_emprestados (List[Livro]): Lista de livros emprestados.
        usuarios (List[Usuario]): Lista de usuários.
    """

    def __init__(self):
        self._livros_disponiveis: List[Livro] = []
        self._livros_emprestados: List[Livro] = []
        self._usuarios: List[Usuario] = []
        
    @property
    def livros_disponiveis(self) -> List[Livro]:
        return self._livros_disponiveis

    @property
    def livros_emprestados(self) -> List[Livro]:
        return self._livros_emprestados

    @property
    def usuarios(self) -> List[Usuario]:
        return self._usuarios

    def adicionar_livro(self, livro: Livro):
        """Adiciona um livro à lista de livros disponíveis."""
        self._livros_disponiveis.append(livro)

    def adicionar_usuario(self, usuario: Usuario):
        """Adiciona um usuário à lista de usuários."""
        self._usuarios.append(usuario)
    
    def mostrar_usuarios(self) -> str:
        lista_usuarios = "\n".join(str(usuario) for usuario in self._usuarios)
        return lista_usuarios

    def emprestar_livro(self, livro: Livro, usuario: Usuario):
        if livro in self._livros_disponiveis:
            self._livros_disponiveis.remove(livro)
            data_emprestimo = datetime.now()
            data_devolucao = data_emprestimo + timedelta(days=3)
            emprestimo = Emprestimo(livro, usuario, data_emprestimo, data_devolucao)
            self._livros_emprestados.append(emprestimo)
        else:
            raise ValueError("Livro não disponível para empréstimo")
        
    def mostrar_livros_emprestados(self) -> str:
        livros_emprestados = "\n".join(str(livro) for livro in self._livros_emprestados)
        return livros_emprestados

    def mostrar_livros_disponiveis(self) -> str:
        livros_disponiveis = "\n".join(str(livro) for livro in self._livros_disponiveis)
        return livros_disponiveis
    
    def devolver_livro(self, livro: Livro):
        """Devolve um livro para a biblioteca."""
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)
            self._livros_disponiveis.append(livro)
        else:
            raise ValueError("Livro não encontrado na lista de emprestados")
