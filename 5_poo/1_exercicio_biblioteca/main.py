from Biblioteca import Autor, Genero, Livro, Biblioteca, Usuario
import os

autor1 = Autor("J. K. Rolling")
autor2 = Autor("John Joe")
genero1 = Genero("Fantasia")
genero2 = Genero("Aventura")
genero3 = Genero("Suspense")

livro1 = Livro("Harry Potter e a fada do dente", "Abril")
livro2 = Livro("Harry Potter e Harry Styles", "Abril")

livro1.adicionar_autor(autor1)
livro2.adicionar_autor(autor2)

livro1.adicionar_genero(genero1)
livro1.adicionar_genero(genero2)
livro2.adicionar_genero(genero3)


usuario1 = Usuario("jose", "12345678", "brasileiro")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_usuario(usuario1)
biblioteca.emprestar_livro(livro1, usuario1)

print("--- LIVROS DISPONÍVEIS --- ")
print(biblioteca.mostrar_livros_disponiveis())
print()
print("--- LIVROS EMPRESTADOS --- ")
print(biblioteca.mostrar_livros_emprestados())

