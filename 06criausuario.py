from tkinter import *
from usuario import Usuario
import janela
 
class criausuario:
    def __init__(self, master):
        self.master=master
        janela.janela(master)
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
 
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
 
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
 
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        
        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()
 
        self.titulo = Label(self.primeiroContainer, text="Cadastrar Usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
 
        self.nomeLabel = Label(self.segundoContainer,text="Nome",
        font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
 
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
 
        self.senhaLabel = Label(self.terceiroContainer, text="Senha",
        font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
        
        
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Salvar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.cadastrarusuario
        self.autenticar.pack()
 
        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
     

    def cadastrarusuario(self):
        usuario = Usuario()
        usuario.nome = self.nome.get()
        usuario.senha = self.senha.get()
        self.mensagem["text"] = usuario.cadastrar()