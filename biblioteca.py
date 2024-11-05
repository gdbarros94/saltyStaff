from pprint import pprint
class Autor:
    def __init__ (self,nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
    def get_nome(self):
        return self.__nome
    def get_nacionalidade(self):
        return self.__nacionalidade

class Livro:
    def __init__ (self, titulo, autor, isbn):
        self.__autor = autor
        self.__titulo = titulo
        self.__isbn = isbn
        self.__disponivel = True
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_isbn(self):
        return self.__isbn
    
    def get_disponivel(self):
        return self.__disponivel

    def adicionar(self, biblioteca):
        biblioteca.adicionar_livro(self)
    def buscar (cls, biblioteca, termo):
        return biblioteca.buscar_livro(termo)

    def emprestar (self,usuario):
        if(self.__disponivel):
            self._disponivel = False
            usuario.emprestar_livro(self)
            print(f"Livro {self.__titulo} emprestado a {usuario.get_nome()}")
    def devolver(self, usuario):
        self.__disponivel = True
        usuario.devolver_livro(self)
        print(f"Livro {self.__titulo} devolvido a biblioteca")
    
class Usuario:
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id
        self.__livros_emprestados = []
    
    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id
    
    def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)
    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []
    
    def get_livros(self):
        return pprint(vars(self.__livros))
    
    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        print(f"Livro {livro.get_titulo()} foi adicionado à biblioteca")
    
    def buscar_livros(self,termo):
        resultados = []
        for livro in self.__livros:
            if termo.lower() in livro.get_titulo().lower() or termo.lower() in livro.get_autor().lower():
                resultados.append(livro)
        return resultados

    def adicionar_usuario (self, usuario):
        self.__usuarios.append(usuario)
        print(f"Usuario {usuario.get_nome()} foi adicionado à biblioteca")
    
    def buscar_usuario(self,id):
        for usuario in self.__usuarios:
            if usuario.get_id() == id:
                return usuario
        return None
        

biblioteca = Biblioteca()

autor_1 = Autor("bananinha", "Brazuca")
livro_1 = Livro("Silmarillion", autor_1, "1254879632541")
livro_1.adicionar(biblioteca)

usuario_1 = Usuario("Gabriel", 1)

biblioteca.adicionar_usuario(usuario_1)

livro_1.emprestar(usuario_1)

print(dir(biblioteca))
print(dir(livro_1))

`"Gabriel `; SELECT * FROM Users;"`
 novo_professor = Professor(Nome="", Area=area, CargaHoraria=carga_horaria, TipoContrato=tipo_contrato)
