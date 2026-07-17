
#EXERCICIO 1 OOP
class ContaBancaria:
    def __init__ (self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo incuficiente!")
    def mostrar_saldo(self):
        print(f"Saldo atual: {self.saldo:.2f}")

conta1 = ContaBancaria("Luiz")
conta1.depositar(100)
conta1.sacar(30)
conta1.mostrar_saldo()

conta2 = ContaBancaria("Renan")
conta2.depositar(50)
conta2.sacar(100)
conta2.mostrar_saldo()

#EXERCICIO 2 OOP

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
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}.")

livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro2 = Livro("1984", "George Orwell", 328)
livro3 = Livro("O Hobbit", "J.R.R. Tolkien", 310)

livro1.mostrar_info()
livro1.emprestar()
livro1.emprestar()   
livro1.devolver()
livro1.devolver()

livro2.mostrar_info()
    
