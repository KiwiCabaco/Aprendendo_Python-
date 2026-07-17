class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = True
    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f"Livro {self.titulo} emprestado com sucesso!")
        else:
            print(f"Livro {self.titulo} já esta emprestado!")
    def devolver(self):
        if self.disponivel == False:
            print(f"Livro {self.titulo} devolvido!")
            self.disponivel = True
        else:
            print("Este livro não estava emprestado.")
    def mostrar_info(self):
        status = "Disponivel" if self.disponivel == True else "Emprestado"
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}, Status: {status}.")

class Biblioteca:
    def __init__(self, titulo):
        self.titulo = titulo
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def buscar_livro(self, titulo):
        for item in self.acervo:
            if item.titulo == titulo:
                print(f"O livro {titulo} esta na biblioteca!")
                return item
        print(f"O livro {titulo} não esta na biblioteca!")
        return None


    def emprestar_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        if livro is not None:
            livro.emprestar()
        else:
            print(f"O livro {titulo} não encontrado no acervo.")
        
    def listar_disponiveis(self):
        for item in self.acervo:
            if item.disponivel: 
                item.mostrar_info()

    def listar_todos(self):
        for item in self.acervo:
            item.mostrar_info()


biblioteca = Biblioteca("Biblioteca Central")

livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro2 = Livro("1984", "George Orwell", 328)
livro3 = Livro("O Hobbit", "J.R.R. Tolkien", 310)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_todos()

print()
biblioteca.emprestar_livro("1984")
biblioteca.emprestar_livro("1984")  # deve avisar que já está emprestado
biblioteca.emprestar_livro("Livro Fantasma")  # deve avisar que não foi encontrado

print()
biblioteca.listar_disponiveis()


            


